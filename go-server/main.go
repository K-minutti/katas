package main

import (
	"archive/zip"
	"io"
	"log"
	"bytes"
	"strings"
	"net/http"
	"os"
	"gopkg.in/yaml.v3"

	"github.com/labstack/echo/v4"
)

type Message struct {
	Key string `yaml:"key"`
}

func main() {
	// Create a new Echo instance
	e := echo.New()

	// Routes
	e.GET("/healthcheck", healthCheckHandler)
	e.POST("/files", uploadFilesHandler)
	e.POST("/files/mem", uploadFilesInMemoryHandler)

	// Start the server
	e.Start(":8080")
}

// Handler for the /healthcheck endpoint
func healthCheckHandler(c echo.Context) error {
	return c.String(http.StatusOK, "Server is healthy")
}

// Handler for the /files endpoint
func uploadFilesHandler(c echo.Context) error {
	// Read the request body as binary data
	body, err := io.ReadAll(c.Request().Body)
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to read the request body")
	}

	// Create a temporary file to store the zipfile
	tempFile, err := os.CreateTemp("", "temp.zip")
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to create temporary file")
	}
	defer os.Remove(tempFile.Name())

	// Write the binary data to the temporary file
	_, err = tempFile.Write(body)
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to write the zipfile to temporary file")
	}

	// Open the zipfile
	zipFile, err := zip.OpenReader(tempFile.Name())
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to open the zipfile")
	}
	defer zipFile.Close()

	// Log the filenames
	for _, file := range zipFile.File {
		log.Println(file.Name)
		if strings.HasSuffix(file.Name, "/") {
			log.Println("---------- not a file")
		}
	}

	return c.String(http.StatusOK, "Filenames logged")
}

func uploadFilesInMemoryHandler(c echo.Context) error {
	// Read the request body as binary data
	body, err := io.ReadAll(c.Request().Body)
	log.Println("Running in memory zip handler")
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to read the request body")
	}

	// Open the zip archive from memory
	zipReader, err := zip.NewReader(bytes.NewReader(body), int64(len(body)))
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to open the zip archive from memory")
	}

	// Create a new buffer to store the modified zip file
	buf := new(bytes.Buffer)

	// Create a new zip writer using the buffer
	zipWriter := zip.NewWriter(buf)

	messages := make(map[string]Message)

	// Iterate through each file in the original zip archive
	for _, file := range zipReader.File {
		// Open the file from the original archive
		fileReader, err := file.Open()
		if err != nil {
			return c.String(http.StatusInternalServerError, "Failed to open a file from the original zip archive")
		}
		defer fileReader.Close()

		if strings.HasSuffix(file.Name, "message.yml") {
			// Read the contents of the file
			fileContents, err := io.ReadAll(fileReader)
			if err != nil {
				return c.String(http.StatusInternalServerError, "Failed to read the contents of the file")
			}

			// Deserialize the file contents into the Message struct
			var message Message
			err = yaml.Unmarshal(fileContents, &message)
			if err != nil {
				return c.String(http.StatusInternalServerError, "Failed to deserialize the file contents")
			}
			messages[file.Name] = message
			log.Println(message)	
		}

		// Create a new file in the modified zip archive
		newFileWriter, err := zipWriter.Create(file.Name)
		if err != nil {
			return c.String(http.StatusInternalServerError, "Failed to create a new file in the modified zip archive")
		}

		// Copy the contents of the original file to the new file in the modified zip archive
		_, err = io.Copy(newFileWriter, fileReader)
		if err != nil {
			return c.String(http.StatusInternalServerError, "Failed to copy file contents to the modified zip archive")
		}
	}

	log.Println(messages)

	// Create a new file in the modified zip archive
	newFileWriter, err := zipWriter.Create("newfile.txt")
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to create a new file in the modified zip archive")
	}

	// Write content to the new file
	_, err = newFileWriter.Write([]byte("This is a new file added to the zip archive"))
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to write content to the new file in the modified zip archive")
	}

	// Close the zip writer
	err = zipWriter.Close()
	if err != nil {
		return c.String(http.StatusInternalServerError, "Failed to close the zip writer")
	}

	// Set the response headers
	c.Response().Header().Set(echo.HeaderContentType, "application/zip")
	c.Response().Header().Set(echo.HeaderContentDisposition, `attachment; filename="modified.zip"`)

	// Return the modified zip file as the response
	return c.Blob(http.StatusOK, "application/zip", buf.Bytes())
}
