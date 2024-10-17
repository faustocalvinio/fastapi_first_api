## Learning FastAPI

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