from lotto.common.config.constants import NOT_WIN_RANK, DRAW_NUMBER_COUNT_ERROR
from lotto.domain.ranks import Ranks


class LottoNumbers:
    def __init__(self, numbers: list[str]):
        self.validate_numbers(numbers)
        self.__numbers = numbers

    @staticmethod
    def validate_numbers(numbers: list[str]) -> None:
        if len(numbers) != 7:
            raise ValueError(DRAW_NUMBER_COUNT_ERROR)

    @property
    def win_number(self) -> str:
        return ", ".join(self.__numbers[0:-1])

    @property
    def bonus_number(self) -> str:
        return self.__numbers[-1]

    def matches(self, user_numbers: str) -> Ranks:
        ranks = Ranks()
        games = user_numbers.split("\n")
        for game in games:
            ranks.add_rank(self.match(game))

        return ranks

    def match(self, game: str) -> int:
        game_number = game.split(",")
        count = 0

        for number in game_number:
            count += self.contains(number)
        bonus = game_number.count(self.bonus_number) > 0

        return self.rank(count, bonus)

    def contains(self, number: str) -> int:
        win_number = self.win_number.split(", ")
        if number in win_number:
            return 1
        return 0

    def is_bonus(self, number: str) -> bool:
        return number == self.bonus_number

    @staticmethod
    def rank(count: int, bonus: bool) -> int:
        if count == 6:
            return 1
        elif count == 5 and bonus:
            return 2
        elif count == 5:
            return 3
        elif count == 4:
            return 4
        elif count == 3:
            return 5

        return NOT_WIN_RANK
