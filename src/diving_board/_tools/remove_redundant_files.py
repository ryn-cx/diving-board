import logging
from logging import getLogger

from gapi import recursively_remove_redundant_files

from diving_board.constants import FILES_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger = getLogger(__name__)
if __name__ == "__main__":
    recursively_remove_redundant_files(FILES_PATH, logger=logger)
