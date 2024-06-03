package golang__test

import (
	"net/http"
	"testing"
)

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
