"""Module utils. Provides utilitary functions."""
import logging


def debug_mode() -> None:
    """debug_mode function implements the function which
    will activate and log info for when mode bool is set to True.
    """
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    for logger_name in ("praw", "prawcore"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
