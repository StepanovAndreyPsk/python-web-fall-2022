from pydantic import BaseModel


class Order(BaseModel):
    """Contract for order."""

    book_id: int
    customer_name: str
    additional_comments: str | None


class Review(BaseModel):
    """Contract for review."""

    book_id: int
    rank: int
    review_text: str | None
