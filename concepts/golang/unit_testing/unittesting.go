package golang__test

import (
	"testing"
)

// Sum calculates the sum of two integers.
func Sum(a, b int) int {
	return a + b
}

// TestSum tests the Sum function.
func TestSum(t *testing.T) {
	// Test case 1: Positive numbers
	result := Sum(3, 5)
	expected := 8
	if result != expected {
		t.Errorf("Sum(3, 5) = %d; want %d", result, expected)
	}

	tests := []struct {
		a, b, expected int
	}{
		{2, 3, 5},
		{-1, 1, 0},
		{0, 0, 0},
		{10, -5, 5},
	}

	for _, tt := range tests {
		result := Sum(tt.a, tt.b)
		if result != tt.expected {
			t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
		}
	}
}
