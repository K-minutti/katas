package main

import (
	"database/sql"
)

type Person struct {
	Id int `json:"id"`
	Name string `json:"name"`
	Age int `json:"age"`
}

type Config struct {
	Enabled bool
	DatabasePath string
	Port 		string
}

func NewConfig() *Config {
	return &Config{
		Enabled: true,
		DatabasePath: "./example.db",
		Port: "8000",
	}
}

func ConnectDatabase(config *Config) (*sql.DB, error) {
	return sql.Open("sqlite3", config.DatabasePath)
}

type PersonRepository struct {
	database *sql.DB
}

func (repository *PersonRepository) FindAll() []*Person {
	rows, _ := repository.database.Query(`SELECT id, name, age FROM people;`)
	defer rows.Close()

	people := []*Person{}

	for rows.Next() {
		var (
			id int
			name string
			age int
		)

	rows.Scan(&id, &name, &age)

	people = append(people, &Person {
		Id: id, 
		Name: name, 
		Age: age,
		})
	}
	return people
}

func NewPersonRepository(database *sql.DB) *PersonRepository {
	return &PersonRepository{database: database}
}

type PersonService struct {
	config *Config
	repository *PersonRepository
}

func (service *PersonService) FindAll() []*Person {
	if service.config.Enabled {
		return service.repository.FindAll()
	}
	return []*Person{}
}

func NewPersonService(config *Config, respository *PersonRepository) *PersonService {
	return &PersonService{config: config, repository: respository}
}