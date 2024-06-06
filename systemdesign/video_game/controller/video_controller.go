package controllers

import (
	"encoding/json"
	"net/http"
	"video_player_game/models"
	"video_player_game/services"
)

type VideoController struct {
	VideoService *services.VideoService
}

func NewVideoController(vs *services.VideoService) *VideoController {
	return &VideoController{VideoService: vs}
}

func (vc *VideoController) CreateVideo(w http.ResponseWriter, r *http.Request) {
	var video models.Video
	err := json.NewDecoder(r.Body).Decode(&video)
	if err != nil {
		http.Error(w, "Invalid video data", http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	err = vc.VideoService.CreateVideo(&video)
	if err != nil {
		http.Error(w, "Failed to create video", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(video)
}

// Implement other CRUD handlers
