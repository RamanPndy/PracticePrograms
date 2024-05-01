package golang

import (
	"net/http"
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

type HTTPClient interface {
	Get(url string) (*http.Response, error)
}

type MyHTTPClient struct{}

func (c *MyHTTPClient) Get(url string) (*http.Response, error) {
	// Implementation of Get method
	return nil, nil
}

func GetData(client HTTPClient, url string) (string, error) {
	_, err := client.Get(url)
	if err != nil {
		return "", err
	}
	// Process response
	return "Data", nil
}

type MockHTTPClient struct{}

func (c *MockHTTPClient) Get(url string) (*http.Response, error) {
	// Mock implementation for testing
	return &http.Response{}, nil
}

func TestGetData(t *testing.T) {
	client := &MockHTTPClient{}
	data, err := GetData(client, "http://example.com")
	if err != nil {
		t.Errorf("GetData returned an error: %v", err)
	}
	if data != "Data" {
		t.Errorf("GetData returned unexpected data: %s", data)
	}
}
