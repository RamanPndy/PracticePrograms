package main

import (
	"fmt"
)

type Book struct {
	Title     string
	Author    string
	Quantity  int
	Borrowers map[string]int // map user ID to borrowed quantity
}

type Library struct {
	Books []Book
}

type User struct {
	ID       string
	Name     string
	Borrowed map[string]int // map book title to borrowed quantity
}

func main() {
	lib := Library{
		Books: []Book{
			{Title: "Book1", Author: "Author1", Quantity: 5, Borrowers: make(map[string]int)},
			{Title: "Book2", Author: "Author2", Quantity: 3, Borrowers: make(map[string]int)},
			{Title: "Book3", Author: "Author3", Quantity: 7, Borrowers: make(map[string]int)},
		},
	}

	users := []User{
		{ID: "1", Name: "User1", Borrowed: make(map[string]int)},
		{ID: "2", Name: "User2", Borrowed: make(map[string]int)},
	}

	// Display available books
	fmt.Println("Available Books:")
	for _, book := range lib.Books {
		fmt.Printf("Title: %s, Author: %s, Quantity: %d\n", book.Title, book.Author, book.Quantity)
	}

	// Borrow a book
	borrowBook(&lib, &users[0], "Book1", 2)

	// Return a book
	returnBook(&lib, &users[0], "Book1", 1)

	// Search for a book
	searchBook(&lib, "Book2")

	// Display borrowed books
	displayBorrowedBooks(&users[0])
}

func borrowBook(lib *Library, user *User, title string, quantity int) {
	for i, book := range lib.Books {
		if book.Title == title && book.Quantity >= quantity {
			lib.Books[i].Quantity -= quantity
			user.Borrowed[title] += quantity
			lib.Books[i].Borrowers[user.ID] += quantity
			fmt.Printf("%s borrowed %d copies of %s\n", user.Name, quantity, title)
			return
		}
	}
	fmt.Printf("Sorry, %s copies of %s are not available\n", title, quantity)
}

func returnBook(lib *Library, user *User, title string, quantity int) {
	if borrowed, ok := user.Borrowed[title]; ok && borrowed >= quantity {
		for i, book := range lib.Books {
			if book.Title == title {
				lib.Books[i].Quantity += quantity
				user.Borrowed[title] -= quantity
				lib.Books[i].Borrowers[user.ID] -= quantity
				fmt.Printf("%s returned %d copies of %s\n", user.Name, quantity, title)
				return
			}
		}
	}
	fmt.Printf("You have not borrowed %s copies of %s\n", title, quantity)
}

func searchBook(lib *Library, title string) {
	for _, book := range lib.Books {
		if book.Title == title {
			fmt.Printf("Book %s is available\n", title)
			return
		}
	}
	fmt.Printf("Book %s is not available\n", title)
}

func displayBorrowedBooks(user *User) {
	fmt.Printf("%s's Borrowed Books:\n", user.Name)
	for title, quantity := range user.Borrowed {
		fmt.Printf("Title: %s, Quantity: %d\n", title, quantity)
	}
}
