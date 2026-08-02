from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .security import Security


# Describes HTTP Basic authentication, requiring a base64-encoded username and password.
class SecurityHttpBasic(Security):
    type: Literal["httpBasic"] = Field(alias="type")
    pass


