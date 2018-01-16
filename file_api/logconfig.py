import logging
import logging.config

logConfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },

    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "python_logging.log",
            "encoding": "utf8"
        }
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["file_handler"]
    }
}


def register_logging():
    logging.config.dictConfig(logConfig)
    logger = logging.getLogger(__name__)
    logger.info("Completed configuration of logger")



