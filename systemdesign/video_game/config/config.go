package config

type Config struct {
	DBDriver   string
	DBName     string
	DBUser     string
	DBPassword string
}

var AppConfig Config

func LoadConfig() {
	AppConfig = Config{
		DBDriver:   "sqlite3",
		DBName:     "video_player.db",
		DBUser:     "",
		DBPassword: "",
	}
}
