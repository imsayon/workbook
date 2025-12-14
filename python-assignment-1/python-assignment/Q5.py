import pprint

library = {} # {BookID: {title, author, year}}

def add_book(bid, title, author, year):
    library[bid] = {'title': title, 'author': author, 'year': year}

def search_author(author):
    results = {bid: data for bid, data in library.items() if data['author'] == author}
    pprint.pprint(results)

add_book("B1", "Python Basics", "John Doe", 2021)
add_book("B2", "Advanced AI", "Jane Smith", 2023)
print("Library Data:"); pprint.pprint(library)
print("\nSearch 'John Doe':"); search_author("John Doe")