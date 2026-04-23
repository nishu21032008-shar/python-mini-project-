# Project 3: Library Management System

class Library:
    def __init__(self, list_of_books):
        # Initial list of books in the library
        self.books = list_of_books

    def display_available_books(self):
        print("\n--- Available Books in Library ---")
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            print(f"SUCCESS: You have borrowed '{book_name}'.")
            self.books.remove(book_name)
        else:
            print("ERROR: This book is not available or already borrowed.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"SUCCESS: You have returned '{book_name}'. Thank you!")

# Main Program Loop
def main():
    # Creating a library object with some books
    my_library = Library(["Python Crash Course", "Digital Electronics", "Data Structures", "Web Design"])
    
    while True:
        print("\n========== LIBRARY MENU ==========")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            my_library.display_available_books()
        elif choice == '2':
            book = input("Enter the name of the book to borrow: ")
            my_library.borrow_book(book)
        elif choice == '3':
            book = input("Enter the name of the book to return: ")
            my_library.return_book(book)
        elif choice == '4':
            print("Closing the Library System. Goodbye!")
            break
        else:
            print("Invalid Option! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()