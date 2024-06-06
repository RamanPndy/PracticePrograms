package database

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
)

var DB *sql.DB

func InitDatabase() {
	db, err := sql.Open("sqlite3", "video_player.db")
	if err != nil {
		panic(err)
	}
	DB = db
}
