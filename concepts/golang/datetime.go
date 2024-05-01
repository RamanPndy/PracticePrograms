package golang

import "time"

func main() {
	// Current time
	currentTime := time.Now()

	// Custom time object
	customTime := time.Date(2022, time.May, 1, 12, 0, 0, 0, time.UTC)

	// Go provides formatting and parsing functions to convert time objects to strings and vice versa.
	// The time.Format() method formats a time object according to a layout string, while time.Parse()
	// parses a string into a time object based on a layout.

	// Formatting time to string
	formattedTime := currentTime.Format("2006-01-02 15:04:05")

	// Parsing string to time
	parsedTime, err := time.Parse("2006-01-02", "2022-05-01")
	if err != nil {
		// Handle parsing error
	}

	// Adding duration to time
	futureTime := currentTime.Add(time.Hour * 24) // Adding 24 hours

	// Subtracting duration from time
	pastTime := currentTime.Add(-time.Hour * 48) // Subtracting 48 hours

	// Loading time zone
	loc, err := time.LoadLocation("America/New_York")
	if err != nil {
		// Handle error
	}

	// Converting time to a specific time zone
	newYorkTime := currentTime.In(loc)

	// You can compare time objects using comparison operators like <, <=, >, >=, ==, !=.

	// Comparing time objects
	if currentTime.Before(futureTime) {
		// currentTime is before futureTime
	}

	if pastTime.After(currentTime) {
		// pastTime is after currentTime
	}

}
