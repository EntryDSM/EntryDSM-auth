from sanic.exceptions import add_status_code, SanicException


@add_status_code(400)
class BadRequest(SanicException):
    ...


@add_status_code(401)
class Unauthorized(SanicException):
    ...


@add_status_code(403)
class Forbidden(SanicException):
    ...


@add_status_code(404)
class NotFound(SanicException):
    ...


@add_status_code(409)
class Conflict(SanicException):
    ...


@add_status_code(500)
class InternalServerError(SanicException):
    ...


class InvalidSyntaxException(Exception):
    ...


class DuplicateDetectedException(Exception):
    ...


class BadRequestFromInterService(Exception):
    def __init__(self):
        self.message = "bad request from inter service"

    def __str__(self):
        return self.message


class ForbiddenFromInterService(Exception):
    def __init__(self):
        self.message = "forbidden from inter service"

    def __str__(self):
        return self.message


class NotFoundFromInterService(Exception):
    def __init__(self):
        self.message = "not found from inter service"

    def __str__(self):
        return self.message


class NotFoundFromCache(Exception):
    def __init__(self):
        self.message = "not found from cache"

    def __str__(self):
        return self.message
