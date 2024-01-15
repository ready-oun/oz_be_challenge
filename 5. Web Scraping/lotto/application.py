from lotto.common.config.constants import (
    LOTTO_MENU,
    WIN_NUMBER_DIRECTORY,
    USER_NUMBER_DIRECTORY,
)
from lotto.common.console.console_reader import ConsoleReader
from lotto.common.console.console_writer import ConsoleWriter
from lotto.common.utils.file_utils import FileUtils
from lotto.domain.command import Command
from lotto.service.console_service import ConsoleService
from lotto.service.lotto_service import LottoService


class Application:
    def __init__(self):
        self.__running = True

    @staticmethod
    def read_command() -> Command:
        try:
            return Command(ConsoleReader.read(LOTTO_MENU))
        except ValueError as e:
            ConsoleWriter.print_error(e)

    def handle_command(self, command: Command) -> None:
        if not command:
            return

        if command.is_show_win_numbers():
            date = ConsoleService.read_date()
            draw_round, win_number, bonus_number = LottoService.get_win_number(date)
            ConsoleService.print_draw_data(draw_round, win_number, bonus_number)

        if command.is_generate_numbers():
            count = ConsoleService.read_count()
            draw_round, numbers = LottoService.create_user_number(count)
            ConsoleService.print_user_data(draw_round, numbers)

        if command.is_check_win_numbers():
            draw_round = ConsoleService.read_round()
            ranks = LottoService.check_win_numbers(draw_round)
            ConsoleService.print_rank(draw_round, ranks)

        if command.is_exit():
            self.__running = False

    def run(self) -> None:
        # 폴더 생성
        FileUtils.make_directories(WIN_NUMBER_DIRECTORY)
        FileUtils.make_directories(USER_NUMBER_DIRECTORY)

        while self.__running:
            try:
                ConsoleWriter.print_empty_line()
                command = self.read_command()
                self.handle_command(command)
            except ValueError as e:
                ConsoleWriter.print_error(e)
            except FileNotFoundError as e:
                ConsoleWriter.print_error(e)


if __name__ == "__main__":
    Application().run()
