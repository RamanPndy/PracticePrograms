package repository

import (
	"database/sql"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestUserRepository_GetUserByID(t *testing.T) {
	mockRepo := NewMockUserRepository()
	user, err := mockRepo.GetUserByID(1)

	assert.NoError(t, err)
	assert.NotNil(t, user)
	assert.Equal(t, 1, user.ID)
	assert.Equal(t, "John Doe", user.Name)
}

func TestUserRepository_GetUserByID_NotFound(t *testing.T) {
	mockRepo := NewMockUserRepository()
	user, err := mockRepo.GetUserByID(2)

	assert.Error(t, err)
	assert.Nil(t, user)
	assert.Equal(t, sql.ErrNoRows, err)
}
