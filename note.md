database.py


``` python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # 예시로 SQLite 사용

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

sqlalchemy
sqlalchemy는 파이썬에서 데이터베이스와 상오작용할수있게 도와주는 라이브러리
데이터 저장 조회할떄 사용

```python 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
```
create_engine 
데이버 베이스와 연결을 만드는 역할 

sessionmaker
데이터베이스와의 상호작용을 위한 세션을 만드는 도구 
세션은 데이터베이스에 쿼리를 보내고 결과를 받아오는역할

declarative_base 
데이터베이스 모델을 정의할떄 기본 클래스를 생성
이클래스를 상속받아 데이터베이스의 테이블구조 정의

model.py 


``` python
from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base()
```

declarative_base 데이터 베이스 모델을 정의할떄 사용ㅎ라 기본 클래스를 생성

class User(Base)
user클래스 정이후 base클래스를 상속받아 데이터베이스의 user테이블을 나타낸다

__tablename__ = "users"



repository.py 
데이터베이스와의 상호작용을 추상화 
crud 작업 관리
비즈니스 로직과의 분리 
테스트 용이성

```
from sqlalchemy.orm import Session
sqlalchemy의 orm 에서 session 클래스를 가져온다
이 클래스는 데이터 베이스의 상호작용을 관리하는 세션을 생성 하는데 사용
```
```
from .models omport User
현재 디렉토리의 models.py 파일에서 User 클래스를 가져온다 
이 클래스는 데이터베이스의 users테이블을 나타낸다
```

```
class UserRepository:
클래스 정의 사용자와의 관련된 데이터베이스 작업을 처리
```








``` python

FastAPI에서의 DTO
제시된 코드에서는 schemas.py 파일의 Pydantic 모델들이 DTO 역할을 합니다:
python# schemas.py (DTO 예시)
class UserCreate(BaseModel):  # 입력 DTO
    email: EmailStr
    username: constr(min_length=3)
    password: str
    password2: str
    
    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v

class UserResponse(BaseModel):  # 출력 DTO
    email: EmailStr
    username: str

    class Config:
        orm_mode = True
DTO의 종류

입력 DTO (Request DTO):

클라이언트에서 보내는 데이터를 검증하고 변환
예: UserCreate - 사용자 등록 시 입력값 검증


출력 DTO (Response DTO):

클라이언트에게 반환할 데이터 형식 정의
민감한 데이터 필터링 (비밀번호 등)
예: UserResponse - 비밀번호 필드 제외된 사용자 정보


내부 DTO:

서비스 계층 간 데이터 전달
특정 작업에 필요한 데이터 구조 정의



DTO의 장점

보안 강화:

민감한 정보를 필터링하여 노출 방지
입력 데이터 검증으로 악의적 입력 차단


유지보수성 향상:

API 계약과 내부 구현의 분리
내부 모델 변경이 API에 영향을 주지 않음


문서화 개선:

API 요청/응답 형식 자동 문서화 (OpenAPI/Swagger)
명확한 데이터 구조 표현
```


```python

# 데이터 베이스 파일
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# DB 설정
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/fastapi_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 모델 파일
# 모델 정의
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)


# 라우터 
# 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

