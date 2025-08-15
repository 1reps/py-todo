from fastapi import APIRouter

router = APIRouter(
  prefix="/api/v1",
  tags=["done"],
)


@router.get("/tasks/{task_id}/done")
async def mark_task_as_done():
  pass


@router.delete("/tasks/{task_id}/done")
async def unmark_task_as_done():
  pass
