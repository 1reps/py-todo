from pydantic import BaseModel, ConfigDict, Field

"""
Task 모델 정의
데이터베이스의 스키마와는 다르다
"""


class TaskBase(BaseModel):
    title: str = Field(..., example="세탁소에 맡긴 것을 찾으러 가기")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="완료 플래그")

    model_config = ConfigDict(from_attributes=True)
