### ToDo 앱을 구현하기 위한 기능 정리

- ToDo 리스트 표시하기
- ToDo에 작업 추가하기
- ToDo 작업 설명문을 변경하기
- ToDo 작업 자체를 삭제하기
- ToDo 작업 `완료` 플래그 닫기
- ToDo 작업에서 `완료` 플래그 제거하기

_endpoint_

- `GET` /tasks
- `POST` /tasks
- `PUT` /tasks/{task_id}
- `DELETE` /tasks/{task_id}
- `PUT` /tasks/{task_id}/done
- `DELETE` /tasks/{task_id}/done

_FastAPI 공식 문서_

- https://fastapi.tiangolo.com/
- https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#file-structure

_swagger_

- http://localhost:8000/docs#/
- http://127.0.0.1:8000/docs#/
