import logging
from logging.handlers import RotatingFileHandler
from config import LOGGING_DIR

def setup():
    """Configure application-wide logging"""

    # Create logs directory if it doesn't exist
    LOGGING_DIR.mkdir(exist_ok=True)

    # Common formatter
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler
    file_handler = RotatingFileHandler(
        filename = LOGGING_DIR / "app.log",
        maxBytes = 5 * 1024 * 1024, # 5 MB
        backupCount = 5,
        encoding = "utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter) 

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Prevent duplicate handlers when restarting with --reload
    root_logger.handlers.clear()


    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    logger = logging.getLogger(__name__)
    logger.info("Logger started successfully")