from dataclasses import dataclass   
@dataclass


class library:
    title: str
    author: str
    numPages: int = 0

    def __repr__(self):
        return ("library (title={}, author={}, numPages={})"
                .format(self.title, self.author, self.numPages))
    