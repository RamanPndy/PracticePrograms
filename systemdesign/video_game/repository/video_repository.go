package repositories

import (
	"database/sql"
	"log"
	"video_player_game/models"
)

type VideoRepository struct {
	DB *sql.DB
}

func NewVideoRepository(db *sql.DB) *VideoRepository {
	return &VideoRepository{DB: db}
}

func (vr *VideoRepository) CreateVideo(video *models.Video) error {
	_, err := vr.DB.Exec("INSERT INTO videos (title, author) VALUES (?, ?)", video.Title, video.Author)
	if err != nil {
		log.Println("Error creating video:", err)
		return err
	}
	return nil
}

// Implement other CRUD methods like GetVideoByID, UpdateVideo, DeleteVideo
