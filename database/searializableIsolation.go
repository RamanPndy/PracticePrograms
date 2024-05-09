package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq" // PostgreSQL driver
)

func main() {
	// Open a connection to the PostgreSQL database
	db, err := sql.Open("postgres", "user=youruser dbname=yourdb sslmode=disable")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	// Begin a transaction with the desired isolation level
	tx, err := db.Begin()
	if err != nil {
		panic(err)
	}
	defer tx.Rollback() // Rollback transaction if not committed

	// Set isolation level to SERIALIZABLE
	_, err = tx.Exec("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")
	if err != nil {
		panic(err)
	}

	// Perform database operations within the transaction
	// ...

	// Commit the transaction if everything is successful
	err = tx.Commit()
	if err != nil {
		panic(err)
	}

	fmt.Println("Transaction committed successfully")
}
