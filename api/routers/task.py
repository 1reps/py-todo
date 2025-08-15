from fastapi import APIRouter

import api.schemas.task as task_schema

"""
*pass*

파이썬 문법에 pass는 '아무것도 하지 않는 문장'을 의미한다
일반적으로 함수는 return 문으로 값을 반환하지만 return을 쓸 필요는 없다.

파이썬은 들여쓰기에 엄격하므로, 아무것도 처리하지 않는 함수를 그대로 두면
함수의 내용을 찾을 수 없어 들여쓰기 오류가 발생한다. 
"""

router = APIRouter(
  prefix="/api/v1",
  tags=["tasks"],
)


@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
  return [task_schema.Task(id=1, title="첫 번째 ToDo 작업")]


@router.post("/tasks")
async def create_task():
  pass


@router.put("/tasks/{task_id}")
async def update_task():
  pass


@router.delete("/tasks/{task_id}")
async def delete_task():
  pass
