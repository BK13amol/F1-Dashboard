class OpenF1Exception(Exception):
    """Base OpenF1 exception."""
    pass


class APIConnectionError(OpenF1Exception):
    pass


class APITimeoutError(OpenF1Exception):
    pass


class APIResponseError(OpenF1Exception):
    pass
