class Ranks:
    def __init__(self):
        self.__ranks = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, -1: 0}

    def add_rank(self, rank: int) -> None:
        self.__ranks[rank] += 1

    @property
    def values(self) -> tuple:
        return (
            self.__ranks.get(1),
            self.__ranks.get(2),
            self.__ranks.get(3),
            self.__ranks.get(4),
            self.__ranks.get(5),
        )
