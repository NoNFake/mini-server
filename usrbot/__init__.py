# 
from rich.traceback import install
install()

from .utils.log import log
from usrbot.sample_config import Config

import functools

log.info(f"Load config: {Config.session_string}")
log.info("Logger is set up")


def autostart(func):
    @functools.wraps(func)

    def wrapper(*args, **kwargs):
        log.critical(f"start func {func.__name__}")
        return func(*args, **kwargs)
    
    return wrapper



