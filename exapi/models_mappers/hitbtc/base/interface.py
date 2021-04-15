"""Has hitbtc base models mapper interface."""

from typing import Protocol, Union

from exapi.models.hitbtc import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                                 HitbtcRawErrorModel)


class IHitbtcBaseModelsMapper(Protocol):
    """Base hitbtc models mapper.

    Has method for map json error to error model.
    """

    def map_to_error(self, raw_error: Union[HitbtcRawErrorModel,
                                            HitbtcRawDetailedErrorModel]
                     ) -> HitbtcErrorModel:
        """Maps error json model to error dataclass model.

        Args:
            raw_error (Union[HitbtcRawErrorModel, HitbtcRawDetailedErrorModel])

        Returns:
            HitbtcErrorModel
        """
