package tests

import (
	"database/sql"
	"log"
	"os"
	"testing"
	"video_player_game/config"
	"video_player_game/database"
)

func TestMain(m *testing.M) {
	setup()
	code := m.Run()
	tearDown()
	os.Exit(code)
}

func setup() {
	config.AppConfig.DBDriver = "sqlite3"
	config.AppConfig.DBName = "test.db"

	db, err := sql.Open(config.AppConfig.DBDriver, config.AppConfig.DBName)
	if err != nil {
		log.Fatalf("Error opening test database: %v\n", err)
	}
	database.DB = db

	// Create necessary tables for testing
	_, err = db.Exec("CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
	if err != nil {
		log.Fatalf("Error creating test table: %v\n", err)
	}
}

func tearDown() {
	database.DB.Close()
	os.Remove("test.db")
}
