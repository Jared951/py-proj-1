### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. 
# Follow the instructions to create and call a function to add a book, 
#based off of the previous dictionaries for our library, 
# to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book(library):
    title = input('What is the title of the book you would like to add? - ')
    author = input('Who is the author of the book you would like to add? - ')
    try: 
        year = int(input('What year was this book published? - '))
    except: 
        year = int(input("Please type a number for the year? - "))
    try:
        rating = float(input('What rating out of 5 would you give this book? - '))
    except:
        rating = float(input('Please type a number for the rating? - '))
    try:
        pages = int(input('What is the page count of the book? - '))
    except:
        pages = int(input('Please type a number for the page count? - '))

    book = {
        'title': title,
        'author': author,
        'year': year,
        'rating': rating,
        'pages': pages
    }

    library.append(book)

    with open('library.txt', 'a') as f:
        f.write("title, author, year, rating, pages\n")

    return library


library = []
print(create_new_book(library))


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, 
#but gets the info from a list, 
# and make it work by reading the information in your home library's .txt document. 
#This will take some new logic, but you can do it.

# Code here

def view_list(my_book_list):
    with open(my_book_list, 'r') as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(', ')
            library.append = {
                'title': title,
                'author': author,
                'year': int(year),
                'rating': float(rating),
                'pages': int(pages)
            }
    return library

            


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement 
#to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. 
# Expand your project. 
# Clean up the code. 
# Make your application functional. 
# Great job getting your first Python application finished!

def book_pages_are_even(library):
    if library["pages"] % 2 == 0:
        return True
    else:
        return False
    
def uppercase_book_title(library):
    for book in library:
        book['title'] = book['title'].upper()
    return library

def lowercase_book_title(library):
    for book in library:
        book['title'] = book['title'].lower()
    return library

if __name__ == "__main__":
    main_menu()