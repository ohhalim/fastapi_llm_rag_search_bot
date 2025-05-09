# basemodel:pydantic 모델의 기본클래스 : 이클래스르 상속받아 데이터 유효성 검사를 위한 모델정의
# EmailStr 이메일 형식의 문자열을 검증하는데 사용
# constr 문자열에 대한 제약조건을 정의 할수있는 타입
# validator:PYdantic모델의 필드에 대한 유효성 검사를 정의하는 데 사용되는 데코레이터
from pydantic import BaseModel, EmailStr, constr, validator
# pydantic 모델 정의 
# 이 모델은 회원가입할떄 필요한 데이터를 검증 
class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3)
    password: str
    password2: str
    # password2 필드에대한 사용자 정의 유효성 검사 하는 데코레이터 
    @validator('password2')
    # 비밀번호 학인필드의 유효성 검사 
    def passwords_match(cls, v, values):
        # values 딕셔너리에 다르면 참이된다
        if 'password' in values and v != values['password']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v
# pydantic 모델정의 사용자 정보 생성후 클라이언트에게 반환될 데이터
class UserResponse(BaseModel):
    email: EmailStr
    username: str
    # Pydantic 모델의 설정을 정의하는 내부클래스 시작 
    class Config:
        # ORM과 호환되도록 한다
        orm_mode = True