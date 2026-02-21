import logging

from good_ass_pydantic_integrator.utils import rebuild_models

import diving_board

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    rebuild_models(diving_board)
