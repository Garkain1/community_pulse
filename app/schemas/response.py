from pydantic import BaseModel, Field


class ResponseCreate(BaseModel):
    question_id: int = Field(..., description="ID вопроса")
    is_agree: bool = Field(..., description="Согласие или несогласие с вопросом")


class ResponseModel(BaseModel):
    id: int
    question_id: int
    is_agree: bool

    class Config:
        from_attributes = True
