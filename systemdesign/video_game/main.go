package main

import (
	"log"
	"net/http"
	"video_player_game/config"
	"video_player_game/controllers"
	"video_player_game/database"
	"video_player_game/repositories"
	"video_player_game/services"
)

func main() {
	config.LoadConfig()
	database.InitDatabase()

	videoRepo := repositories.NewVideoRepository(database.DB)
	videoService := services.NewVideoService(videoRepo)
	videoController := controllers.NewVideoController(videoService)

	http.HandleFunc("/videos", videoController.CreateVideo)
	// Add other routes for CRUD operations

	log.Println("Starting server on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
