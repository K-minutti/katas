package example

type Config struct {
	data string
}

type Server struct {
	config *Config
  }
  
// Without DI
func buildMyConfigSomehow() *Config {
	return &Config{data: "New Config"}
}

func New() *Server {
	return &Server{
	  config: buildMyConfigSomehow(),
	}
}

// With DI
func NewDI(config *Config) *Server {
	return &Server{
	  config: config,
	}
  }