package main

import (
	"bytes"
	"fmt"
)

// Without DI
type Logger struct{}

func (logger *Logger) Log(message string) {
	fmt.Println(message)
}

type HttpClient struct {
	logger *Logger
}

func (client *HttpClient) Get(url string) string {
	client.logger.Log("Getting... " + url)
	return "Response from... " + url
}

func NewHttpClient() *HttpClient {
	logger := &Logger{}
	return &HttpClient{logger}
}

type ConcatService struct {
	logger *Logger 
	client *HttpClient
}

func (service *ConcatService) GetAll(urls ...string) string {
	service.logger.Log("Running GetAll")
	var result bytes.Buffer
	for _, url := range urls {
		result.WriteString(service.client.Get(url))
	}

	return result.String()
}

func NewConcatService() *ConcatService {
	logger := &Logger{}
	client := NewHttpClient()
	return &ConcatService{logger, client}
}

func main_ex() {
	service := NewConcatService()
	result := service.GetAll(
		"http://example.com",
		"https://minutti.xyz",
	)
	fmt.Println(result)
}

// With DI
func NewHttpClientDI(logger *Logger) *HttpClient {
	return &HttpClient{logger}
}

func NewConcatServiceDI(logger *Logger, client *HttpClient) *ConcatService {
	return &ConcatService{logger, client}
}

func main_di_ex() {
	logger := &Logger{}
	client := NewHttpClientDI(logger)
	service := NewConcatServiceDI(logger, client)

	result := service.GetAll(
		"http://example.com",
		"https://minutti.xyz",
	)
	fmt.Println(result)		
}