.PHONY: build up down logs test clean

# Build da imagem
build:
	docker-compose build

# Iniciar os containers
up:
	docker-compose up -d

# Parar os containers
down:
	docker-compose down

# Ver logs
logs:
	docker-compose logs -f

# Executar testes
test:
	docker-compose exec web python -m pytest tests/ -v

# Limpar containers e volumes
clean:
	docker-compose down -v
	docker system prune -f

# Executar linting (se tiver flake8)
lint:
	docker-compose exec web flake8 .

# Acessar shell do container
shell:
	docker-compose exec web bash