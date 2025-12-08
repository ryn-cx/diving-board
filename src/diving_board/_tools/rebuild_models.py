from diving_board import DivingBoard
from diving_board.schedule import (
    SCHEDULE_CUSTOMIZATIONS,
    SCHEDULE_GROUP_LIST_CUSTOMIZATIONS,
)

if __name__ == "__main__":
    client = DivingBoard()

    client.rebuild_models("adjacent_series")
    client.rebuild_models("schedule", SCHEDULE_CUSTOMIZATIONS)
    client.rebuild_models("schedule/group_list", SCHEDULE_GROUP_LIST_CUSTOMIZATIONS)
    client.rebuild_models("season")
    client.rebuild_models("season/bucket/related")
    client.rebuild_models("season/bucket/season")
    client.rebuild_models("season/series")
    client.rebuild_models("vod")
    client.rebuild_models("vod/bucket")
    client.rebuild_models("vod/hero")
    client.rebuild_models("vod/tabs")
    client.rebuild_models("vod/text_block")
