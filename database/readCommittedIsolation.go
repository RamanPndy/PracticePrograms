package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "your_username"
	password = "your_password"
	dbname   = "your_database"
)

func main() {
	// Connect to the database
	connStr := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Set the isolation level for the transaction
	txOptions := &sql.TxOptions{
		Isolation: sql.LevelReadCommitted, // Change this to the desired isolation level
	}

	// Start a transaction with the specified isolation level
	tx, err := db.BeginTx(nil, txOptions)
	if err != nil {
		log.Fatal(err)
	}
	defer tx.Rollback() // Rollback the transaction if it's not committed

	// Perform database operations within the transaction
	// For example, you can execute SQL statements like tx.Exec("INSERT INTO ...")

	// Commit the transaction to make the changes permanent
	err = tx.Commit()
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	// Open a connection to the database
	db, err := sql.Open("mysql", "user:password@tcp(host:port)/dbname")
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	// Begin a transaction with a specific isolation level
	tx, err := db.Begin()
	if err != nil {
		panic(err.Error())
	}

	// Set the isolation level for the transaction
	_, err = tx.Exec("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
	if err != nil {
		panic(err.Error())
	}

	// Perform SQL operations within the transaction
	// For example, querying or updating data
	// tx.Query("SELECT * FROM table_name")

	// Commit the transaction
	err = tx.Commit()
	if err != nil {
		panic(err.Error())
	}

	fmt.Println("Transaction committed successfully")
}
