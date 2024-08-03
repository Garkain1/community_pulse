from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: int = Field(..., description="ID категории")


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int

    class Config:
        from_attributes = True
