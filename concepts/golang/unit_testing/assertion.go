package golang__test

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func add(a, b int) int {
	return a + b
}

func TestAdd(t *testing.T) {
	assert := assert.New(t)

	result := add(2, 3)
	assert.Equal(5, result, "they should be equal")

	result = add(-1, 1)
	assert.Equal(0, result, "they should be equal")
}
