from fastapi import APIRouter

from app import contracts

router = APIRouter()


@router.get("/")
def read_root():
    """Description."""
    return {"service": "online book store"}


@router.get("/books/:{book_id}")
async def get_book_info(book_id: int):
    """Get book info."""
    return {"book_id": book_id}


@router.post("/orders")
async def create_order(order: contracts.Order):
    """Place a new order."""
    order_dict = order.dict()

    return order_dict


@router.post("/review")
async def add_review(review: contracts.Review):
    """Create a book review."""
    review_dict = review.dict()
    return review_dict


@router.get("/review")
async def get_review(book_id: int, author_name: str):
    """Get review."""
    return {"author_name": author_name, "book_id": book_id}
