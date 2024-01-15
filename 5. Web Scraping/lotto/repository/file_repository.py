from lotto.common.utils.file_utils import FileUtils


class FileRepository:
    @classmethod
    def find_filepath_by_round(cls, prefix: str, draw_round: int) -> str:
        return FileUtils.find_by_path(prefix % draw_round)

    @classmethod
    def has_file(cls, filepath: str) -> bool:
        return FileUtils.is_exists(filepath)

    @classmethod
    def save(cls, filepath: str, numbers: list) -> None:
        FileUtils.write_line(filepath, numbers)

    @classmethod
    def find_one_by_file_path(cls, filepath: str) -> list[str]:
        return FileUtils.readline(filepath).split(",")

    @classmethod
    def save_all(cls, filepath: str, numbers: list[list[str]]) -> None:
        FileUtils.write_lines(filepath, numbers)

    @classmethod
    def find_all_by_file_path(cls, filepath: str) -> str:
        return FileUtils.readall(filepath)
