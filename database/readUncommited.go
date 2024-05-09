package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	// Replace the connection string with your MySQL database connection details
	db, err := sql.Open("mysql", "user:password@tcp(localhost:3306)/dbname")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Begin a transaction
	tx, err := db.Begin()
	if err != nil {
		log.Fatal(err)
	}

	// Set the isolation level to Read Uncommitted
	_, err = tx.Exec("SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")
	if err != nil {
		tx.Rollback()
		log.Fatal(err)
	}

	// Perform database operations within the transaction
	// For example, you can execute queries using tx.Query() or tx.Exec()

	// Commit the transaction
	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Transaction committed successfully with Read Uncommitted isolation level.")
}
