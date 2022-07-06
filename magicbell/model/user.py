import typing

from pydantic import Field

from ._base import BaseModel


class User(BaseModel):
    id: typing.Optional[str] = Field(description="The user's MagicBell ID (readonly).")
    external_id: typing.Optional[str] = Field(
        description="A unique string that MagicBell can utilize to identify the user uniquely. "
        "We recommend setting this attribute to the ID of the user in your database. "
        "Provide the external id if the user's email is unavailable."
    )
    email: typing.Optional[str] = Field(description="The user's email.")
    first_name: typing.Optional[str] = Field(description="The user's first name.")
    last_name: typing.Optional[str] = Field(description="The user's last name.")
    custom_attributes: typing.Optional[typing.Dict[str, typing.Any]] = Field(
        description="Any customer attributes that you'd like to associate with the user. "
        "You may want to use these attributes later when writing email templates, for example."
    )


class WrappedUser(BaseModel):
    user: User
