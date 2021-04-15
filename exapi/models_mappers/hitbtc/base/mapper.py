"""Has hitbtc base models mapper."""

from typing import Union

from exapi.models.hitbtc import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                                 HitbtcRawErrorModel)


class HitbtcBaseModelsMapper:
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

        code = raw_error["code"]
        message = raw_error["message"]
        description = raw_error.get("description")  # type: ignore
        return HitbtcErrorModel(code=code, message=message, description=description)
