from abc import ABC, abstractmethod
from typing import Protocol

class LibraryItem(Protocol):
    @abstractmethod
    def book1(self) -> str:
        pass

    @abstractmethod
    def book2(self) -> str:
        pass

class Fantasy:
    def book1(self) -> str:
        return "A Court of Thorns and Roses by Sarah J. Maas"

    def book2(self) -> str:
        return "The Cruel Prince by Holly Black"

class Dystopian:
    def book1(self) -> str:
        return "The Hunger Games by Suzanne Collins"

    def book2(self) -> str:
        return "Divergent by Veronica Roth"

def main():  
    fantasy = Fantasy()
    dystopian = Dystopian()

    print(fantasy.book1())
    print(fantasy.book2())
    print(dystopian.book1())
    print(dystopian.book2())

if __name__ == '__main__':
    main()