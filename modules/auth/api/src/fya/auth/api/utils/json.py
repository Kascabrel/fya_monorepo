from dataclasses import asdict, fields, is_dataclass
import json
from typing import Type, TypeVar

T = TypeVar("T")


def to_json(event) -> str:
    """Convert a dataclass event to a JSON string."""
    return json.dumps(asdict(event), default=str)


def from_json(json_str: str, cls: Type[T]) -> T:
    """
    Reconstruct a dataclass event from a JSON string.

    Ignores extra fields that are not in the dataclass.
    """
    data = json.loads(json_str)

    if not is_dataclass(cls):
        raise TypeError(f"{cls.__name__} is not a dataclass")

    # Keep only fields defined in the dataclass
    field_names = {f.name for f in fields(cls)}
    filtered_data = {k: v for k, v in data.items() if k in field_names}

    return cls(**filtered_data)
