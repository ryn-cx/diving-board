from diving_board.protocol import DivingBoardProtocol
from diving_board.season import models as season_models
from diving_board.season_bucket import models


# Having this as a seperate mixin makes the types more accurate than just returning the
# model from the season mixin.
class SeasonBucketMixin(DivingBoardProtocol):
    def extract_season_bucket_from_season(
        self,
        data: season_models.Season,
        *,
        update: bool = False,
    ) -> models.SeasonBucket:
        matching_elements = [
            element
            for element in data.elements
            if element.field_type == "bucket" and element.attributes.type == "season"
        ]

        if len(matching_elements) == 0:
            msg = "No season bucket element found"
            raise ValueError(msg)

        if len(matching_elements) > 1:
            msg = (
                f"Expected exactly one season bucket element, "
                f"found {len(matching_elements)}"
            )
            raise ValueError(msg)

        season_data = matching_elements[0].model_dump()

        if update:
            return self.parse_response(
                models.SeasonBucket,
                season_data,
                "season_bucket",
            )

        return models.SeasonBucket.model_validate(season_data)
