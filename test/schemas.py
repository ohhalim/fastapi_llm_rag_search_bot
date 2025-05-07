from pydantic import BaseModel, EmailStr, constr, validator

class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3)
    password: str
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v

class UserResponse(BaseModel):
    email: EmailStr
    username: str

    class Config:
        orm_mode = True