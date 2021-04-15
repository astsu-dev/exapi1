import abc


class BaseRequestCreator(abc.ABC):
    """Base request creator."""

    BASE_URL: str

    def _create_url(self, path: str) -> str:
        return self.BASE_URL + path
