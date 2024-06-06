package services

import (
	"video_player_game/models"
	"video_player_game/repositories"
)

type VideoService struct {
	VideoRepo *repositories.VideoRepository
}

func NewVideoService(vr *repositories.VideoRepository) *VideoService {
	return &VideoService{VideoRepo: vr}
}

func (vs *VideoService) CreateVideo(video *models.Video) error {
	return vs.VideoRepo.CreateVideo(video)
}

// Implement other CRUD methods in a similar manner
