from pydantic import BaseModel, Field

"""
Task 모델 정의
데이터베이스의 스키마와는 다르다
"""

class Task(BaseModel):
  id: int
  title: str | None = Field(None, example="세탁소에 맡긴 것을 찾으러 가기")
  done: bool = Field(False, description="완료 플래그")
