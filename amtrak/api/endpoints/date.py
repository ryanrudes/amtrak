from datetime import datetime
from typing import Optional

import pytz

def get_timezone_from_character(timezone: str) -> str:
    """
    Returns the corresponding timezone based on the given character.

    Parameters:
    - timezone (str): A single character representing a timezone.

    Returns:
    - str: The corresponding timezone as a string.

    Example:
    >>> get_timezone_from_character("P")
    'America/Los_Angeles'
    >>> get_timezone_from_character("M")
    'America/Denver'
    >>> get_timezone_from_character("C")
    'America/Chicago'
    >>> get_timezone_from_character("E")
    'America/New_York'

    If the given character is not recognized, the function will default to
    eastern time.
    """
    match timezone.upper():
        case "P":
            # Pacific
            return "America/Los_Angeles"
        case "M":
            # Mountain
            return "America/Denver"
        case "C":
            # Central
            return "America/Chicago"
        case "E":
            # Eastern
            return "America/New_York"
        case _:
            # Default
            return "America/New_York"

def parse_date(date: str, tz: str = "America/New_York") -> Optional[str]:
    """
    Parses the given date string and returns it in ISO8601 format with the specified timezone.

    Parameters:
    - date (str): The date string to parse.
    - tz (str): The timezone to use for the parsed date. Defaults to "America/New_York".

    Returns:
    - Optional[str]: The parsed date in ISO8601 format with the specified timezone, or None if the date is empty.

    Example:
    >>> parse_date("12/31/2022 23:59:59", "America/Los_Angeles")
    '2022-12-31T23:59:59-08:00'
    >>> parse_date("01/01/2023 00:00:00", "America/Denver")
    '2023-01-01T00:00:00-07:00'
    >>> parse_date("", "America/Chicago")
    None
    """
    if not date:
        return None

    dt = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
    dt = pytz.timezone(tz).localize(dt)
    return dt.isoformat()