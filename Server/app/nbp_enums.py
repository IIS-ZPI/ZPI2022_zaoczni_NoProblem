import enum


class TableName(enum.Enum):
    A = "A"
    B = "B"
    C = "C"


class Period(str, enum.Enum):
    WEEK = "week",
    TWO_WEEKS = "two_weeks",
    MONTH = "month",
    QUARTER = "quarter",
    HALF_YEAR = "half_year",
    YEAR = "year"
