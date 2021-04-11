"""Has utils for work with urls."""

from yarl import URL

from exapi.requesters.typedefs import Params


def create_query_string(params: Params) -> str:
    """Creates query string from dictionary of params.

    Args:
        params (Params)

    Returns:
        str
    """

    return URL().with_query(params).query_string
