from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ArkoudaRequest(_message.Message):
    __slots__ = ["args", "cmd", "format", "request_id", "size", "token", "user"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    args: str
    cmd: str
    format: str
    request_id: str
    size: int
    token: str
    user: str
    def __init__(self, user: _Optional[str] = ..., token: _Optional[str] = ..., cmd: _Optional[str] = ..., format: _Optional[str] = ..., size: _Optional[int] = ..., args: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ArkoudaResponse(_message.Message):
    __slots__ = ["args", "cmd", "message", "request_id", "request_status", "user"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    args: str
    cmd: str
    message: str
    request_id: str
    request_status: str
    user: str
    def __init__(self, message: _Optional[str] = ..., request_id: _Optional[str] = ..., request_status: _Optional[str] = ..., user: _Optional[str] = ..., cmd: _Optional[str] = ..., args: _Optional[str] = ...) -> None: ...
