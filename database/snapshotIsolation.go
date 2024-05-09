package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

func main() {
	// Replace the connection string with your PostgreSQL database connection details
	db, err := sql.Open("postgres", "user=youruser password=yourpassword dbname=yourdb sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Begin a transaction with snapshot isolation
	tx, err := db.BeginTx(nil, &sql.TxOptions{Isolation: sql.LevelSnapshot})
	if err != nil {
		log.Fatal(err)
	}

	// Perform database operations within the transaction
	// For example, you can execute queries using tx.Query() or tx.Exec()

	// Commit the transaction
	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Transaction committed successfully with Snapshot Isolation.")
}
