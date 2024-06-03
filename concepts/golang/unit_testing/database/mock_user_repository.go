package repository

import "database/sql"

type MockUserRepository struct {
	users map[int]*User
}

func NewMockUserRepository() *MockUserRepository {
	return &MockUserRepository{
		users: map[int]*User{
			1: {ID: 1, Name: "John Doe"},
		},
	}
}

func (m *MockUserRepository) GetUserByID(id int) (*User, error) {
	user, exists := m.users[id]
	if !exists {
		return nil, sql.ErrNoRows
	}
	return user, nil
}
