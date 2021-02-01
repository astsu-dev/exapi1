"""Has hitbtc base models mapper interface."""

from typing import Protocol, Union

from exapi.api.hitbtc.models import (HitbtcRawDetailedErrorModel,
                                     HitbtcRawErrorModel)
from exapi.api.hitbtc.models.error import HitbtcErrorModel


class IHitbtcBaseModelsMapper(Protocol):
    """Has methods for mapping json models to dataclass models."""

    def map_to_error(self, raw_error: Union[HitbtcRawErrorModel,
                                            HitbtcRawDetailedErrorModel]
                     ) -> HitbtcErrorModel:
        """Maps error json model to error dataclass model.

        Args:
            raw_error (Union[HitbtcRawErrorModel, HitbtcRawDetailedErrorModel])

        Returns:
            HitbtcErrorModel
        """
