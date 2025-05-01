from tkinter import *
from tkinter import messagebox

class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.genre}, {self.publication_year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added:", book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book Removed:", title)
                return True
        return False

    def search_book(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                print(book)

# === GUI Section ===
library = Library()

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    genre = genre_entry.get()
    year = year_entry.get()
    if title and author and genre and year:
        book = Book(title, author, genre, year)
        library.add_book(book)
        messagebox.showinfo("Success", "Book added!")
        clear_entries()
        display_books()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def remove_book():
    title = title_entry.get()
    if library.remove_book(title):
        messagebox.showinfo("Success", "Book removed.")
        clear_entries()
        display_books()
    else:
        messagebox.showwarning("Not Found", "Book not found.")

def search_books():
    keyword = search_entry.get()
    results = library.search_book(keyword)
    listbox.delete(0, END)
    if results:
        for book in results:
            listbox.insert(END, str(book))
    else:
        listbox.insert(END, "No books found.")

def display_books():
    listbox.delete(0, END)
    for book in library.books:
        listbox.insert(END, str(book))

def save_and_exit():
    root.destroy()

def clear_entries():
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    genre_entry.delete(0, END)
    year_entry.delete(0, END)
    search_entry.delete(0, END)

# === Main Window ===
root = Tk()
root.title("Personal Library Manager")

# Entry Frame
frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Title").grid(row=0, column=0)
title_entry = Entry(frame, width=30)
title_entry.grid(row=0, column=1)

Label(frame, text="Author").grid(row=1, column=0)
author_entry = Entry(frame, width=30)
author_entry.grid(row=1, column=1)

Label(frame, text="Genre").grid(row=2, column=0)
genre_entry = Entry(frame, width=30)
genre_entry.grid(row=2, column=1)

Label(frame, text="Year").grid(row=3, column=0)
year_entry = Entry(frame, width=30)
year_entry.grid(row=3, column=1)

# Buttons
Button(root, text="Add Book", width=20, command=add_book).pack(pady=5)
Button(root, text="Remove Book", width=20, command=remove_book).pack(pady=5)

# Search
search_entry = Entry(root, width=40)
search_entry.pack(pady=5)
Button(root, text="Search Book", command=search_books).pack(pady=5)

# Display
Button(root, text="Display All Books", command=display_books).pack(pady=5)

# Listbox
listbox = Listbox(root, width=80)
listbox.pack(pady=10)

# Save and Exit
Button(root, text="Save & Exit", command=save_and_exit, fg="white", bg="green").pack(pady=5)

root.mainloop()
