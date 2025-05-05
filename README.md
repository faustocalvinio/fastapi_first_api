## Learning FastAPI

This project demonstrates a simple FastAPI application.

### Features

- RESTful API endpoints
- Dockerized setup for easy deployment
- Database seeding script
- Hot-reloading for development

### Getting Started

1. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2. **Seed the database**
    (see below)

3. **Run the application**
    (see below)

### Project Structure

- `app/main.py` - FastAPI application entry point
- `app/seed.py` - Script to seed the database
- `requirements.txt` - Python dependencies
- `docker-compose.yml` - Docker configuration

### API Documentation

Once running, access the interactive docs at:  
`http://localhost:8000/docs`

SEED
```bash
python ./app/seed.py
```


RUN APP
```bash
docker compose up -d
uvicorn app.main:app --reload
```

DEPENDENCIES
```bash
pip freeze > requirements.txt
```