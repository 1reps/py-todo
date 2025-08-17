from sqlalchemy import create_engine, text

from api.models.task import Base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    with engine.connect() as conn:
        # 외래키 제약조건 비활성화
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
        conn.commit()

        # 테이블 삭제
        Base.metadata.drop_all(bind=engine)

        # 외래키 제약조건 활성화
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
        conn.commit()

    # 테이블 재생성
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
