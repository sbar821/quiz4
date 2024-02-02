from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def book1(self):
        pass

    @abstractmethod
    def book2(self):
        pass

class Fantasy(Library):
    def book1(self):
        return "Fantasy book: A Court of Thorns and Roses by Sarah J. Maas"

    def book2(self):
        return "Fantasy book: The Cruel Prince by Holly Black"

class Dystopian(Library):
    def book1(self):
        return "Dystopian book: The Hunger Games by Suzanne Collins"

    def book2(self):
        return "Dystopian book: Divergent by Veronica Roth"

def main():  
    fantasy = Fantasy()
    dystopian = Dystopian()

    print(fantasy.book1())
    print(fantasy.book2())
    print(dystopian.book1())
    print(dystopian.book2())

if __name__ == '__main__':
    main()