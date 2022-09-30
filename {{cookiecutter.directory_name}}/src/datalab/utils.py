import logging
from pathlib import Path

import git


logger = logging.getLogger(f"main.{__name__}")


# ----------------------  CONFIG MANAGEMENT  ------------------------#


def get_logger(name: str = "main") -> logging.Logger:
    """Get a logger based on config file

    Args:
        name: Name of the logger to load. Defaults to "main".

    Returns:
        logger object
    """

    repo_path = Path(git.Repo(__file__, search_parent_directories=True))
    log_path = repo_path / "conf" / "logging.conf"
    logging.config.fileConfig(str(log_path))
    logger = logging.getLogger(name)

    return logger