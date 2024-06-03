package repository

import (
	"database/sql"
)

type User struct {
	ID   int
	Name string
}

type UserRepository interface {
	GetUserByID(id int) (*User, error)
}

type userRepositoryImpl struct {
	DB *sql.DB
}

func NewUserRepository(db *sql.DB) UserRepository {
	return &userRepositoryImpl{DB: db}
}

func (r *userRepositoryImpl) GetUserByID(id int) (*User, error) {
	row := r.DB.QueryRow("SELECT id, name FROM users WHERE id = ?", id)
	user := &User{}
	err := row.Scan(&user.ID, &user.Name)
	if err != nil {
		return nil, err
	}
	return user, nil
}
