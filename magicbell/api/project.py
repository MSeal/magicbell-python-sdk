"""Defines a `ProjectAPI` class to interact with projects in MagicBell."""
import typing

from ..model.project import WrappedProject, WrappedProjectInput, WrappedProjects
from ..model.response import Response
from ._base import BaseAPI
from ._parsing import build_request_content, build_response


class ProjectAPI(BaseAPI):
    """Magicbell API methods for projects."""

    async def list_projects(self, workspace_id: int) -> WrappedProjects:
        """List all projects in a workspace, returning `WrappedProjects`."""
        return (await self.list_projects_detailed(workspace_id)).parsed

    async def list_projects_detailed(self, workspace_id: int) -> Response[WrappedProjects]:
        """List all projects in a workspace, returning a `Response`."""
        url = f"/workspaces/{workspace_id}/projects"
        response = await self.client.get(url, headers=self.configuration.get_user_headers())
        return build_response(response=response, out_type=WrappedProjects)

    async def get_project(self, workspace_id: int, project_id: int) -> WrappedProject:
        """Get a project, returning `WrappedProject`."""
        return (await self.get_project_detailed(workspace_id, project_id)).parsed

    async def get_project_detailed(
        self, workspace_id: int, project_id: int
    ) -> Response[WrappedProject]:
        """Get a project, returning a `Response`."""
        url = f"/workspaces/{workspace_id}/projects/{project_id}"
        response = await self.client.get(url, headers=self.configuration.get_user_headers())
        return build_response(response=response, out_type=WrappedProject)

    async def create_project(
        self, workspace_id: int, project_input: typing.Union[WrappedProjectInput, typing.Dict]
    ) -> WrappedProject:
        """Create a project, returning `WrappedProject`."""
        return (await self.create_project_detailed(workspace_id, project_input)).parsed

    async def create_project_detailed(
        self, workspace_id: int, project_input: typing.Union[WrappedProjectInput, typing.Dict]
    ) -> Response[WrappedProject]:
        """Create a project, returning a `Response`."""
        url = f"/workspaces/{workspace_id}/projects"
        response = await self.client.post(
            url,
            content=build_request_content(project_input),
            headers=self.configuration.get_user_headers(),
        )
        return build_response(response=response, out_type=WrappedProject)

    async def update_project(
        self,
        workspace_id: int,
        project_id: int,
        project_input: typing.Union[WrappedProjectInput, typing.Dict],
    ) -> WrappedProject:
        """Update a project, returning `WrappedProject`."""
        return (await self.update_project_detailed(workspace_id, project_id, project_input)).parsed

    async def update_project_detailed(
        self,
        workspace_id: int,
        project_id: int,
        project_input: typing.Union[WrappedProjectInput, typing.Dict],
    ) -> Response[WrappedProject]:
        """Update a project, returning a `Response`."""
        url = f"/workspaces/{workspace_id}/projects/{project_id}"
        response = await self.client.put(
            url,
            content=build_request_content(project_input),
            headers=self.configuration.get_user_headers(),
        )
        return build_response(response=response, out_type=WrappedProject)

    async def delete_project(self, workspace_id: int, project_id: int) -> None:
        """Delete a project."""
        await self.delete_project_detailed(workspace_id, project_id)

    async def delete_project_detailed(
        self, workspace_id: int, project_id: int
    ) -> Response[typing.Type[None]]:
        """Delete a project, returning a `Response`."""
        url = f"/workspaces/{workspace_id}/projects/{project_id}"
        response = await self.client.delete(url, headers=self.configuration.get_user_headers())
        return build_response(response=response, out_type=None)
