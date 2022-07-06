"""Contains a mock HTTP server for testing"""
import typing
import uuid
from datetime import datetime, timezone

from starlette import status
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

api_key = "my-api-key"
api_secret = "my-api-secret"
user_jwt = "my-user-jwt"


def verify_api_key_and_secret(request: Request):
    if request.headers.get("X-MAGICBELL-API-KEY") != api_key:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            {
                "errors": [
                    {
                        "code": "api_key_not_provided",
                        "message": "API key not provided",
                    }
                ]
            },
        )
    if request.headers.get("X-MAGICBELL-API-SECRET") != api_secret:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            {
                "errors": [
                    {
                        "code": "api_secret_not_provided",
                        "message": "API secret not provided",
                    }
                ]
            },
        )


def verify_user_jwt(request: Request):
    if request.headers.get("Authorization") != f"Bearer {user_jwt}":
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            {
                "errors": [
                    {
                        "code": "forbidden",
                    }
                ]
            },
        )


def verify_user_hmac(request: Request):
    external_id = request.headers.get("X-MAGICBELL-USER-EXTERNAL-ID")
    user_email = request.headers.get("X-MAGICBELL-USER-EMAIL")

    if request.headers.get("X-MAGICBELL-USER-HMAC") != "hmac_123":
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            {
                "errors": [
                    {
                        "code": "forbidden",
                    }
                ]
            },
        )

    if request.headers.get("X-MAGICBELL-API-KEY") != api_key:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            {
                "errors": [
                    {
                        "code": "api_key_not_provided",
                        "message": "API key not provided",
                    }
                ]
            },
        )

    if not (external_id or user_email):
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            {
                "errors": [
                    {
                        "code": "external_id_or_email_required",
                    }
                ]
            },
        )


async def http_exception(request: Request, exc: HTTPException):
    return JSONResponse(exc.detail, status_code=exc.status_code, headers=exc.headers)


app = Starlette(debug=True, exception_handlers={HTTPException: http_exception})


@app.route("/notifications", methods=["POST"])
async def create_notifications(request: Request):
    verify_api_key_and_secret(request)

    data = await request.json()
    if "notification" not in data:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            {
                "errors": [
                    {
                        "message": "Param 'notification' is required",
                    }
                ]
            },
        )

    notification = data["notification"]
    if not ("title" in notification and "recipients" in notification):
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            {
                "errors": [
                    {
                        "message": "Param 'notification.title' is required",
                    },
                    {
                        "message": "Param 'notification.recipients' is required",
                    },
                ]
            },
        )

    return JSONResponse(
        {
            "notification": {
                "id": str(uuid.uuid4()),
                "title": notification["title"],
                "content": notification.get("content"),
                "action_url": notification.get("action_url"),
                "category": notification.get("category"),
                "topic": notification.get("topic"),
                "custom_attributes": notification.get("custom_attributes"),
                "sent_at": datetime.now(timezone.utc).timestamp(),
            }
        }
    )


def make_example_project(workspace_id: int, project_id: int = 1) -> typing.Dict:
    return {
        "id": 1,
        "name": "My first project",
        "hmac_enabled": True,
        "api_key": "api_key_123",
        "api_secret": "api_secret_123",
        "workspace": {
            "id": workspace_id,
            "title": "My first workspace",
        },
    }


@app.route("/workspaces/{workspace_id:int}/projects", methods=["GET"])
async def get_projects(request: Request):
    verify_user_jwt(request)
    return JSONResponse({"projects": [make_example_project(request.path_params["workspace_id"])]})


@app.route("/workspaces/{workspace_id:int}/projects", methods=["POST"])
async def create_project(request: Request):
    verify_user_jwt(request)
    return JSONResponse({"project": make_example_project(request.path_params["workspace_id"])})


@app.route(
    "/workspaces/{workspace_id:int}/projects/{project_id:int}",
    methods=["GET", "PUT", "DELETE"],
)
async def manage_project(request: Request):
    verify_user_jwt(request)

    if request.method in {"GET", "PUT"}:
        return JSONResponse(
            {
                "project": make_example_project(
                    request.path_params["workspace_id"], request.path_params["project_id"]
                )
            }
        )
    elif request.method == "DELETE":
        return JSONResponse({"message": "Successfully deleted project"})


@app.route("/users", methods=["POST"])
async def create_user(request: Request):
    verify_api_key_and_secret(request)
    body = await request.json()

    if "user" not in body:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            {
                "errors": [
                    {
                        "message": "Param 'user' is required",
                    }
                ]
            },
        )

    if body["user"]["email"] == "500@example.com":
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error")

    return JSONResponse(body)


@app.route("/users/{user_id}", methods=["PUT", "DELETE"])
async def manage_user(request: Request):
    verify_api_key_and_secret(request)

    if request.method == "PUT":
        body = await request.json()

        if "user" not in body:
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {
                    "errors": [
                        {
                            "message": "Param 'user' is required",
                        }
                    ]
                },
            )

        return JSONResponse(body)
    elif request.method == "DELETE":
        return JSONResponse(None, status_code=status.HTTP_204_NO_CONTENT)


@app.route("/channels", methods=["POST", "GET"])
async def manage_channels(request: Request):
    verify_api_key_and_secret(request)
    if request.method == "POST":
        return JSONResponse(None, status_code=status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        return JSONResponse(
            {
                "channels": [
                    {
                        "slug": "email",
                        "configuration": {
                            "providers": {
                                "mailgun": {
                                    "enabled": True,
                                    "sender_domain": "example.com",
                                    "api_key": "1234",
                                    "from": {
                                        "email": "notification@example.com",
                                        "name": "Example",
                                    },
                                }
                            }
                        },
                    },
                    {"slug": "slack"},
                    {"slug": "web_push"},
                    {"slug": "mobile_push"},
                    {"slug": "sms"},
                    {"slug": "in_app"},
                ]
            }
        )


@app.route("/graphql", methods=["POST"])
async def graphql(request: Request):
    body = await request.json()
    if "notifications" in body["query"]:
        verify_user_hmac(request)
    else:
        verify_api_key_and_secret(request)

    return JSONResponse({"data": {"notifications": [{"id": str(uuid.uuid4())}]}})
