from ._base import BaseModel


class Workspace(BaseModel):
    """Represents a workspace in MagicBell."""

    id: int
    title: str
