package main

import (
	"archive/zip"
	"bytes"
	"errors"
	"io"
	"strings"

	"gopkg.in/yaml.v2"
)

func (s *Service) SaveBaseTfArtifacts(zipData []byte, componentNameTypes map[string]string) ([]byte, error) {
	var modulepackData Modulepack

	// Create a reader for the zip data
	zipReader, err := zip.NewReader(bytes.NewReader(zipData), int64(len(zipData)))
	if err != nil {
		return nil, err
	}

	// Search for "eacmodulepack.yaml" in the zip data
	var yamlData []byte
	for _, file := range zipReader.File {
		if file.Name == "eacmodulepack.yaml" {
			rc, err := file.Open()
			if err != nil {
				return nil, err
			}
			yamlData, err = io.ReadAll(rc)
			rc.Close()
			if err != nil {
				return nil, err
			}
			break
		}
	}

	// Check if we found the yaml file
	if yamlData == nil {
		return nil, errors.New("eacmodulepack.yaml not found in zipData")
	}

	// Unmarshal the yaml data into the modulepackData struct
	err = yaml.Unmarshal(yamlData, &modulepackData)
	if err != nil {
		return nil, err
	}

	// Create a buffer for the new zip file
	newZipBuffer := new(bytes.Buffer)

	// Create a writer for the new zip file
	newZipWriter := zip.NewWriter(newZipBuffer)

	// Iterate over the entries in the zip file
	for _, file := range zipReader.File {
		// Iterate over the entries in componentNameTypes
		for key, value := range componentNameTypes {
			component, ok := modulepackData.Components[value]
			if !ok {
				return nil, errors.New("component not found")
			}
			dir := component.Dir
			if strings.HasPrefix(file.Name, dir) {
				// Open the file
				rc, err := file.Open()
				if err != nil {
					return nil, err
				}
				defer rc.Close()

				// Create a new file in the new zip file
				newFile, err := newZipWriter.Create(key + "/" + strings.TrimPrefix(file.Name, dir))
				if err != nil {
					return nil, err
				}

				// Copy the data from the old file to the new one
				_, err = io.Copy(newFile, rc)
				if err != nil {
					return nil, err
				}
			}
		}
	}

	if err = newZipWriter.Close(); err != nil {
		return nil, err
	}

	return newZipBuffer.Bytes(), nil
}

