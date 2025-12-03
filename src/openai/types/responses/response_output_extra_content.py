# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResponseOutputExtraContent"]


class ResponseOutputExtraContent(BaseModel):
    extra_content: Dict[str, object]
    """The extra content such as though_signature from gemini 3"""

    type: Literal["extra_content"]
    """The type of the refusal. Always `refusal`."""
