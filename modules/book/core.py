from . import helpers

class Book:
    defaultPath = "books/"

    def __init__(self, name:str, path:str = defaultPath):
        self.name = name
        self.path = path
        self.content = helpers.readBook(path + name)
        self.wordCount = helpers.countWords(self.content)
        self.letterCounts = helpers.countEachLetter(self.content)

    def __str__(self):
        return (f"Book: {self.name}\n"
                + "Stats:\n"
                + f" Word Count: {self.wordCount}\n"
                + " Letter Counts (Descending): \n  "
                + "  ".join([f"'{c}' : {self.letterCounts[c]}\n" for c in self.letterCounts])
                )
