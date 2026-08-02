from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union, Literal
from .security import Security


# Describes HTTP Bearer authentication, typically using a bearer token (e.g., JWT).
class SecurityHttpBearer(Security):
    type: Literal["httpBearer"] = Field(alias="type")
    pass


