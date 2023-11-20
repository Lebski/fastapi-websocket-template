# FastAPI sample project

## Description

Example project for FastAPI with HTTP and Websocket endpoints.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

or

```bash
python main.py
```

## Docker

```bash
docker build -t fastapi-example .
docker run -p 8000:8000 fastapi-example
```
