from lotto.common.config.constants import (
    READ_DATE,
    PRINT_DRAW_NUMBER_PATTERN,
    PRINT_DRAW_ROUND_PATTERN,
    READ_COUNT,
    PRINT_USER_NUMBER_PATTERN,
    READ_ROUND,
    PRINT_RANK_TITLE_PATTERN,
    PRINT_RANK_DETAIL_PATTERN,
    NUMBER_FORMAT_ERROR,
)
from lotto.common.console.console_reader import ConsoleReader
from lotto.common.console.console_writer import ConsoleWriter
from lotto.domain.date import Date
from lotto.domain.ranks import Ranks


class ConsoleService:
    @classmethod
    def read_date(cls) -> Date:
        return Date(ConsoleReader.read(READ_DATE))

    @classmethod
    def read_count(cls) -> int:
        try:
            return int(ConsoleReader.read(READ_COUNT))
        except:
            ConsoleWriter.print_error(ValueError(NUMBER_FORMAT_ERROR))

    @classmethod
    def read_round(cls) -> int:
        try:
            return int(ConsoleReader.read(READ_ROUND))
        except:
            ConsoleWriter.print_error(ValueError(NUMBER_FORMAT_ERROR))

    @classmethod
    def print_draw_data(
        cls, draw_round: str, win_number: str, bonus_number: str
    ) -> None:
        ConsoleWriter.print(PRINT_DRAW_ROUND_PATTERN % draw_round)
        ConsoleWriter.print(PRINT_DRAW_NUMBER_PATTERN % (win_number, bonus_number))

    @classmethod
    def print_user_data(cls, draw_round: str, numbers: list[str]) -> None:
        ConsoleWriter.print(PRINT_USER_NUMBER_PATTERN % draw_round)
        ConsoleWriter.print(numbers)

    @classmethod
    def print_rank(cls, draw_round: int, ranks: Ranks) -> None:
        ConsoleWriter.print(PRINT_RANK_TITLE_PATTERN % draw_round)
        ConsoleWriter.print(PRINT_RANK_DETAIL_PATTERN % ranks.values)
