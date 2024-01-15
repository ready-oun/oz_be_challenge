import random
from datetime import datetime, timedelta, date as dt

import requests
from bs4 import BeautifulSoup

from lotto.common.config.constants import (
    LOTTO_URL,
    WIN_NUMBER_FILE_PATTERN,
    USER_NUMBER_FILE_PATTERN,
)
from lotto.domain.date import Date
from lotto.domain.lotto_numbers import LottoNumbers
from lotto.domain.ranks import Ranks
from lotto.repository.file_repository import FileRepository


class LottoService:
    @classmethod
    def get_win_number(cls, date: Date) -> tuple:
        draw_round = cls.get_draw_round(date)
        filepath = FileRepository.find_filepath_by_round(
            WIN_NUMBER_FILE_PATTERN, draw_round
        )

        if not FileRepository.has_file(filepath):
            lotto_numbers = cls._fetch_lotto_numbers(draw_round)
            FileRepository.save(filepath, lotto_numbers)

        lotto_numbers = LottoNumbers(FileRepository.find_one_by_file_path(filepath))
        return draw_round, lotto_numbers.win_number, lotto_numbers.bonus_number

    @classmethod
    def create_user_number(cls, count: int) -> tuple:
        draw_round = cls.get_draw_round(Date.today())
        filepath = FileRepository.find_filepath_by_round(
            USER_NUMBER_FILE_PATTERN, draw_round
        )

        FileRepository.save_all(filepath, cls.create_numbers(count))
        numbers = FileRepository.find_all_by_file_path(filepath)

        return draw_round, numbers

    @classmethod
    def check_win_numbers(cls, draw_round: int) -> Ranks:
        win_filepath = FileRepository.find_filepath_by_round(
            WIN_NUMBER_FILE_PATTERN, draw_round
        )
        user_filepath = FileRepository.find_filepath_by_round(
            USER_NUMBER_FILE_PATTERN, draw_round
        )

        round_number = LottoNumbers(FileRepository.find_one_by_file_path(win_filepath))
        user_numbers = FileRepository.find_all_by_file_path(user_filepath)

        return round_number.matches(user_numbers)

    @classmethod
    def create_numbers(cls, count: int) -> list:
        return [list(map(str, random.sample(range(1, 46), 6))) for _ in range(count)]

    @classmethod
    def get_draw_round(cls, date: Date) -> int:
        return cls._calculate_round(date.to_datetime_date())

    @classmethod
    def _calculate_round(cls, date: datetime.date) -> int:
        while date.weekday() != 5:
            date += timedelta(days=1)
        start_date = dt(2002, 12, 7)
        weeks = (date - start_date).days // 7
        return 1 + weeks

    @classmethod
    def _fetch_lotto_numbers(cls, draw_round: int) -> list:
        response = requests.get(LOTTO_URL % draw_round)
        bs = BeautifulSoup(response.text, "html.parser")

        win_numbers = [number.get_text() for number in bs.select(".num.win span")]
        bonus_number = bs.select_one(".num.bonus span").get_text()

        win_numbers.append(bonus_number)
        return win_numbers
