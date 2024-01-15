from lotto.common.config.constants import *


class Command:
    def __init__(self, command: str):
        self.validate_command(command)
        self.__command = int(command)

    def validate_command(self, command: str) -> None:
        if not command.isdigit():
            raise ValueError(NUMBER_FORMAT_ERROR)

        if self.is_valid_command_range(command):
            raise ValueError(NUMBER_RANGE_ERROR)

    @staticmethod
    def is_valid_command_range(command: str) -> bool:
        return int(command) < MINIMUM_INPUT_VALUE or int(command) > MAXIMUM_INPUT_VALUE

    def is_show_win_numbers(self) -> bool:
        return self.__command == SHOW_WIN_NUMBERS

    def is_generate_numbers(self) -> bool:
        return self.__command == GENERATE_NUMBERS

    def is_check_win_numbers(self) -> bool:
        return self.__command == CHECK_WIN_NUMBERS

    def is_exit(self) -> bool:
        return self.__command == EXIT
