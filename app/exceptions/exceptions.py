class DatabaseError(Exception):
    pass


class NotFoundError(Exception):
    pass


class ServiceError(Exception):
    pass


class RepositoryError(Exception):
    pass


class InternalError(Exception):
    pass


class BadInputError(Exception):
    pass


class TokenError(Exception):
    pass


class CredentialsError(Exception):
    pass


class ApiError(Exception):
    pass
