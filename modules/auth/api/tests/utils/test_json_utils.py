from fya.auth.api.events import UserRegisteredEvent
from fya.auth.api.utils.json import to_json, from_json


def test_json_serialization_deserialization():
    original_event = UserRegisteredEvent(user_id="123", email="user@example.com")

    json_str = to_json(original_event)
    new_event = from_json(json_str, UserRegisteredEvent)

    assert isinstance(new_event, UserRegisteredEvent)
    assert new_event.user_id == original_event.user_id
    assert new_event.email == original_event.email
