from sqlalchemy.orm import Session
from models import User

# 데이터베이스 작업을 처리하는 레포지토리
class UserRepository:
    # db 매개변수는 session 객체를 받는다 init 초기화 매서드
    def __init__(self, db: Session):
        # 전달받은 db세션을 클래스의 변수로 저장 
        self.db = db
    # email. username hashpassword 를 매개변수로 받는다
    def create_user(self, email: str, username: str, hashed_password: str):
        db_user = User(email=email, username=username, hashed_password=hashed_password)
        # 사용자 인스턴스를 데이터베이스 세션에 추가한다
        self.db.add(db_user)
        # 데이터베이스 변경사항을 저장 
        self.db.commit()
        # 데이터 베이스에서 새로 생성된 사용자 인스턴스 정보 교체
        self.db.refresh(db_user)
        return db_user
    # 사용자 조회 메서드
    def get_user_by_email(self, email: str):
        # user 테이블을 쿼리하여 이메일과 첫번쨰 사용자를 찾는다 존제하지 않으면 none
        return self.db.query(User).filter(User.email == email).first()
        # 여기서 사용되는 delate는 sql문법에 있는 메서드야?
    def delete_user(self, user: User):
        self.db.delete(user)
        # delete 메서드를 호출하면, 해당 인스턴스가 데이터베이스 세션에서 삭제 대기 상태가 됩니다. 
        # 실제로 데이터베이스에서 삭제되려면 self.db.commit() 메서드를 호출하여 변경 사항을 저장해야한다
        self.db.commit()