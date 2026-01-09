# Mesa Sandbox API

A basic FastAPI project with one controller.

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Root
- `GET /` - Welcome message
- `GET /health` - Health check

### Items Controller
- `GET /items/` - List all items
- `GET /items/{item_id}` - Get a specific item
- `POST /items/` - Create a new item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item
