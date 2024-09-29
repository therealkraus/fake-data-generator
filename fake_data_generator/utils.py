# Standard imports
import datetime
import shutil
from pathlib import Path

# Related third party imports

# Local application/library specific imports


def reset_output_directory(output_dir: str):
    """Remove the output directory if it exists.

    Args:
        output_dir (Path): The output directory to remove.
    """
    if Path(output_dir).exists() and Path(output_dir).is_dir():
        shutil.rmtree(output_dir)
    Path(output_dir).mkdir(parents=True, exist_ok=False)


def generate_timestamp() -> str:
    utc_datetime = datetime.datetime.now(datetime.timezone.utc)
    year = utc_datetime.strftime("%Y")
    month = utc_datetime.strftime("%m")
    day = utc_datetime.strftime("%d")
    time = utc_datetime.strftime("T%H%M%S%fZ")

    return f"{year}-{month}-{day}-{time}"
