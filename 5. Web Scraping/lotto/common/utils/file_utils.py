import os
import sys


class FileUtils:
    @classmethod
    def make_directories(cls, path) -> None:
        os.makedirs(cls.get_root_path() + path, exist_ok=True)

    @classmethod
    def find_by_path(cls, path) -> str:
        return cls.get_root_path() + path

    @classmethod
    def get_root_path(cls) -> str:
        return os.path.dirname(sys.modules["__main__"].__file__)

    @classmethod
    def readline(cls, filepath: str) -> str:
        with open(filepath, "r") as file:
            return file.readline()

    @classmethod
    def readall(cls, filepath: str) -> str:
        with open(filepath, "r") as file:
            return file.read()

    @classmethod
    def is_exists(cls, filepath: str) -> bool:
        return os.path.exists(filepath) and os.path.isfile(filepath)

    @classmethod
    def write_line(cls, filepath: str, lines: list[str]) -> None:
        with open(filepath, "w") as file:
            file.writelines(",".join(lines))

    @classmethod
    def write_lines(cls, filepath: str, lines: list[list[str]]) -> None:
        flatten_data = [",".join(line) + "\n" for line in lines]
        with open(filepath, "a") as file:
            file.writelines(flatten_data)
