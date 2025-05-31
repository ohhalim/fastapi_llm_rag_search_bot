# fastapi에서 클래스를 가져옴 : 
# APIRouter : API 앤드포인트를 정으이 하는데 사용
# Depends : 의존성 주입 도구로, 특정 함수나 클래스의 인스턴스를 자동으로 주입할수있게 함
# HTTPException : HTTP 오류를 발생 시키기 위한 예외 클래스 이다
# HTTP 상태코드를 정의하는 모듈
# status 모듈은 HTTP 상태 코드(예: 200 OK, 404 Not Found, 500 Internal Server Error 등)를 상수 형태로 정의한 것입니다. 
# 이 모듈을 사용하면 숫자 대신 명확한 이름의 상수를 사용할 수 있어 코드의 가독성이 향상됩니다.
# HTTPException은 HTTP 상태 코드(404, 400, 500 등)를 포함한 HTTP 오류를 발생시키는 메커니즘
from fastapi import APIRouter, Depends, HTTPException, status
# sqlalchemy.orm에서 Session 클래스를 가져옴 -> 이 세션은 데이터베이스와의 상호작용을 관리
from sqlalchemy.orm import Session
# services, schemas 파일 가져옴 : services는 비즈니스 로직을 처리 , schemas 데이터 유효성검사를 의한 Pydantic모델 정의
import schemas
import services
# database.py에서 SessionLocal을 가져옴 데이터베이스 세션을 생성하는 팩토리 함수
from database import SessionLocal

# 새로운 라우터 인스턴스르 생성 : API앤드포인트에서 사용된다
router = APIRouter()
# 데이터베이스 세션을 생성 반환 
def get_db():
    # SessionLocal 을 호출하여 세로운 데이터 베이스 세션을 생성
    db = SessionLocal()
    # 예외처리 위한 블록을 시작 
    try:
        yield db
    finally:
        db.close()
# 이 데코레이터는 POST 요청을 처리하는 앤드포인트  
# 응답 모델로 schemas.UserResponse 를 사용
@router.post("/create/", response_model=schemas.UserResponse)
# 사용자 생성 요청을 처리하는 함수
def user_create(user: schemas.UserCreate, db: Session = Depends(get_db)): 
    # 서비스 모듈의 create_user 함수를 호출하여 사용자 생성, 결과 반환
    return services.create_user(db=db, user=user)

# login 경로로 들어오는 요청처리
@router.post("/login/")
# 로그인 요청 처리 함수 정의 
def login(email: str, password: str, db: Session = Depends(get_db)):
    # 서비스 모듈의 인증함수를 호출해 인증
    user = services.authenticate_user(db=db, email=email, password=password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="이메일 또는 비밀번호가 올바르지 않습니다.")
    return {"message": f"{user.username}님, 반갑습니다!"}