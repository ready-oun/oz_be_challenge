import re
from datetime import datetime

from typing_extensions import Self

from lotto.common.config.constants import DATE_FORMAT_ERROR


class Date:
    def __init__(self, date: str):
        self.__value = self.parse_dates(date)

    @staticmethod
    def parse_dates(date: str) -> datetime.date:
        date_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")
        match = re.match(date_pattern, date)

        if not match:
            raise ValueError(DATE_FORMAT_ERROR)

        return match.group(1)

    @property
    def value(self) -> datetime.date:
        return self.__value

    @classmethod
    def today(cls) -> Self:
        return Date(datetime.today().strftime("%Y-%m-%d"))

    def to_datetime_date(self) -> datetime.date:
        return datetime.strptime(self.__value, "%Y-%m-%d").date()
