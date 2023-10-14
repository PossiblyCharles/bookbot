from modules.book import Book

def main():
    book = None
    try:
        book = Book("frankenstein")
    except FileNotFoundError as e:
        print(e)
        return
    print(book)

if __name__ == "__main__":
    main()