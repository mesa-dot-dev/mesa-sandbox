from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    in_stock: bool = True


# In-memory storage for demo purposes
items_db: dict[int, Item] = {}
current_id = 0


@router.get("/")
async def list_items():
    """Get all items."""
    return {"items": {id: item.model_dump() for id, item in items_db.items()}}


@router.get("/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@router.post("/", status_code=201)
async def create_item(item: Item):
    """Create a new item."""
    global current_id
    current_id += 1
    items_db[current_id] = item
    return {"id": current_id, **item.model_dump()}


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"id": item_id, **item.model_dump()}


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None
