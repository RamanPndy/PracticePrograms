func readLines(filename string) ([]string, error) {
	var lines []string
	file, err := ioutil.ReadFile(filename)
	if err != nil {
		return lines, err
	}
	buf := bytes.NewBuffer(file)
	for {
		line, err := buf.ReadString('\n')
		if len(line) == 0 {
			if err != nil {
				if err == io.EOF {
					break
				}
				return lines, err
			}
		}
		lines = append(lines, line)
		if err != nil && err != io.EOF {
			return lines, err
		}
	}
	return lines, nil
}

// the easiest way to read a file (at least for me) is using the scanner from the bufio package in the standard library. 
package main

import (
    "bufio"
    "fmt"
    "io"
    "log"
    "os"
)

func main() {
    // first open the file
    file, err := os.Open("./fifa-winners.jsonl")
    if err != nil {
        log.Fatalf("could not open the file: %v", err)
    }
    defer file.Close()
    log.Println("******************* READ WITH SCANNER *******************")
    readWithScanner(file)
    log.Println("******************* READ WITH READLINE() *******************")

    // we just reset the offset. because we read this file once
    // imagine the cursor is in the end of the file so we have to get back to the first line and read it again 
    file.Seek(0, 0)
    readWithReadLine(file)

    log.Println("we read a file twice!")
}

// Read with simple scanner

func readWithScanner(file *os.File) {
    // first open the file
    file, err := os.Open("./fifa-winners.jsonl")
    if err != nil {
        log.Fatalf("could not open the file: %v", err)
    }
    // finally, we can have our scanner
    buf := []byte{}
    scanner := bufio.NewScanner(file)
    scanner.Buffer(buf, 2048*1024)
    lineNumber := 1
    for scanner.Scan() {
        fmt.Println(scanner.Text())
        lineNumber++
    }
    // the rest of our spaghetti
    if err := scanner.Err(); err != nil {
        log.Fatalf("something bad happened in the line %v: %v", lineNumber, err)
    }
}

// Read with Readline function

func read(r *bufio.Reader) ([]byte, error) {
    var (
        isPrefix = true
        err      error
        line, ln []byte
    )

    for isPrefix && err == nil {
        line, isPrefix, err = r.ReadLine()
        ln = append(ln, line...)
    }

    return ln, err
}

func readWithReadLine(file *os.File) {
    reader := bufio.NewReader(file)
    for {
        line, err := read(reader)
        if err != nil {
            if err == io.EOF {
                break
            }
            log.Fatalf("a real error happened here: %v\n", err)
        }
        fmt.Println(string(line))
    }
}

func writeToFile() {
	// Create a file
	file, err := os.Create("example.txt")
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	// Ensure the file is closed properly
	defer file.Close()

	// Write to the file
	_, err = file.WriteString("Hello, World!\n")
	if err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}

	fmt.Println("File written successfully")
}

func writeToFileWithScanner() {
	// Create or open the file for writing
	file, err := os.Create("output.txt")
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close() // Ensure the file is closed properly

	// Create a scanner to read from standard input
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Enter text to write to the file (type 'exit' to finish):")

	for scanner.Scan() {
		// Read the input
		input := scanner.Text()

		// Exit the loop if the user types 'exit'
		if input == "exit" {
			break
		}

		// Write the input to the file
		_, err := file.WriteString(input + "\n")
		if err != nil {
			fmt.Println("Error writing to file:", err)
			return
		}
	}

	// Check for scanner errors
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
	}

	fmt.Println("Finished writing to the file")
}