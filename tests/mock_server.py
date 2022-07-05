"""Contains a mock HTTP server for testing"""
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


@app.route("/workspaces/{workspace_id:int}/projects", methods=["GET"])
async def get_projects(request: Request):
    verify_user_jwt(request)

    return JSONResponse(
        {
            "projects": [
                {
                    "id": 1,
                    "name": "My first project",
                    "hmac_enabled": True,
                    "api_key": "api_key_123",
                    "api_secret": "api_secret_123",
                    "workspace": {
                        "id": request.path_params["workspace_id"],
                        "title": "My first workspace",
                    },
                }
            ]
        }
    )
