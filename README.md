### Virtual environment

```bash
conda create -n sa_env
conda activate sa_env
```

### Documentation

```bash
python3 -m mkdocs serve
```

### FastAPI Server

```bash
cd <main_project_folder>
uvicorn app.api:app \
--host 0.0.0.0 \
--port 8000 \
--reload \
--reload-dir sentiment_analysis \
--reload-dir app
```

### React server

```bash
cd frontend/spa
npm start
```
