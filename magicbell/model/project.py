import typing

from ._base import BaseModel
from .workspace import Workspace


class Project(BaseModel):
    """Represents a project in MagicBell."""

    id: int
    name: str
    hmac_enabled: bool
    api_key: str
    api_secret: str
    workspace: Workspace


class WrappedProject(BaseModel):
    """Represents a project in MagicBell (wrapped)."""

    project: Project


class WrappedProjects(BaseModel):
    """Represents a list of projects in MagicBell (wrapped)."""

    projects: typing.List[Project]


class ProjectInput(BaseModel):
    """Fields for creating or updating a project."""

    name: str
    hmac_enabled: typing.Optional[bool]


class WrappedProjectInput(BaseModel):
    """Fields for creating or updating a project (wrapped)."""

    project: ProjectInput
