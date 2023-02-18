"""Module main. Checks for debug mode variable and executes removit function."""
import os
from src import removit
from src import configuration as c
from src import utils

debug_mode = c.config.get("DEFAULT", "REDDIT_DEBUG_MODE", vars=os.environ)
print("REDDIT_DEBUG_MODE:", debug_mode)
if debug_mode == "True":
    utils.debug_mode()


# pass True to rmvit function to use a reddit instance with permission to delete comments.
removit.rmvit()
