# 데이터베이스와 상호작용하는 세션생성
from sqlalchemy.orm import Session
# 비밀번호 해싱을 위한 클래스:cryptcontext -> 비밀번호를 안전하게 저장하는데 사용된다
from passlib.context import CryptContext
# 현재 디렉토리의 모델 파일에서 User클래스를 가져온다 
from .models import User
# 현제 디렉토리 schemas.py에서 UserCreate 클래스를 가져온다 : 이클래스는 데이터베이스의 user 테이블을 나타냅니다
from .schemas import UserCreate
# repositories.py에서 UserRepository클래스를 가져온다 데이텁에ㅣ스 작업을 처리
from .repositories import UserRepository

# CrypotContext 인스턴스를 생성 bcrypt 를 통하여 비밀번호를 해싱  deprtcated = auto 는 이전 번전의 알고리즘을 자동을 ㅗ처리
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 새로운사용자를 생성하는함수 
# db는 sqlalchemy 객체이고 
# sqlalchemy에서 session 객체는 데이터 베이스와 상오작용한다 
# 이 session 객체를 사용해서 데이터베이스에 쿼리를 보내고  데이터를 추가, 수정 삭제를 하는 작업을 수앻한다
# 데이터베이스와 연결을 유지하며 작업을 수행하는동한 상태를 관리한다

# UserCreate는 schemas 에서 정의한 데이터의 형태
def create_user(db: Session, user: UserCreate):
    user_repo = UserRepository(db)
    hashed_password = pwd_context.hash(user.password)
    # repo에 create_user 매서드를 호출해서 새로운 사용자를 데이터베이스에 추가 
    # 사용자 인스턴스를 반환 
    return user_repo.create_user(email=user.email, username=user.username, hashed_password=hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_email(email)
    if user and pwd_context.verify(password, user.hashed_password):
        return user
    return None