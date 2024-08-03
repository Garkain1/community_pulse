from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., description="Название категории")


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: int = Field(..., description="ID категории")


class QuestionResponse(BaseModel):
    id: int
    text: str
    category: CategoryResponse

    class Config:
        from_attributes = True
