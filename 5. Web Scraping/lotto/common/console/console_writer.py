from lotto.common.config.constants import EMPTY_LINE


class ConsoleWriter:
    @staticmethod
    def print_error(e: Exception):
        print("Error: ", e)

    @classmethod
    def print_empty_line(cls):
        print(EMPTY_LINE)

    @classmethod
    def print(cls, pattern):
        print(pattern)
