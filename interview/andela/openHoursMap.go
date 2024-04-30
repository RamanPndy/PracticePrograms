package main

import (
	"fmt"
)

func main() {
	openhoursmap := []map[string]string{
		{
			"day":   "Monday",
			"open":  "8 am",
			"close": "5 pm",
		},
		{
			"day":   "Tuesday",
			"open":  "8 am",
			"close": "5 pm",
		},
		{
			"day":   "Wednesday",
			"open":  "8 am",
			"close": "6 pm",
		},
		{
			"day":   "Thursday",
			"open":  "8 am",
			"close": "5 pm",
		},
		{
			"day":   "Friday",
			"open":  "8 am",
			"close": "5 pm",
		},
		{
			"day":   "Saturday",
			"open":  "8 am",
			"close": "4 pm",
		},
	}

	grouphoursmap := make([]map[string]string, 0)
	currentGroup := make(map[string]string)

	for _, hours := range openhoursmap {
		if hours["open"] == currentGroup["open"] && hours["close"] == currentGroup["close"] {
			// Extend the current group
			currentGroup["day"] += "-" + hours["day"]
		} else {
			// Start a new group
			if len(currentGroup) > 0 {
				grouphoursmap = append(grouphoursmap, currentGroup)
			}
			currentGroup = map[string]string{
				"day":   hours["day"],
				"open":  hours["open"],
				"close": hours["close"],
			}
		}
	}

	// Add the last group
	if len(currentGroup) > 0 {
		grouphoursmap = append(grouphoursmap, currentGroup)
	}

	// Print the grouped hours
	for _, group := range grouphoursmap {
		fmt.Printf("Day: %s, Open: %s, Close: %s\n", group["day"], group["open"], group["close"])
	}
}
