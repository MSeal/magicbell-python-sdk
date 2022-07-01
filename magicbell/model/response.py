import typing

import orjson
from pydantic.generics import GenericModel

from ._base import BaseModel

ResponseBodyT = typing.TypeVar("ResponseBodyT", bound=BaseModel)


class Response(GenericModel, typing.Generic[ResponseBodyT]):
    status_code: int
    content: bytes
    headers: typing.MutableMapping[str, str]
    parsed: typing.Optional[ResponseBodyT]

    def json_content(self) -> typing.Any:
        """Load `self.content` as JSON and return the parsed object"""
        return orjson.loads(self.content)
