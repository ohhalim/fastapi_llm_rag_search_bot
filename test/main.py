# fast api 애플리케이션 생성
from fastapi import FastAPI
import routers
# 현재 층의 database.py 파일에서 engine과 Base를 가져 온다
# engine은 데이터 베이스 연결을 나타네고 Base 데이터베이스 모델 정의할떄 사용할 기본클래스
from database import engine, Base

# FastAPI 클래스를 사용해서 애플리케이션 인스턴스를 생성 
# 이 인스턴스는 애플리케이션의 모든 설정과 라우팅을 관리
app = FastAPI()

# 데이터베이스 테이블 생성
# Base 클래스에 정의된 모든 데이터 베읏 모델에 대해 테이블 생성
# bind=engine은 이 작업이 사용할 데이터 베이스 엔진을 지정
# 애플리케이션이 시작될떄 데이터베이스에 필요한 테이블이 없으면 생성
Base.metadata.create_all(bind=engine)
# app.include_router router 를 Fast API애플리케이션에 포함시킨다
# prefix 모든 앤드포인트에 접두사 "/users"를 추가 예를 들어 router 에 정의된 create앤드포인트는 /users/create/로 접근할수있게 된다
# tags=["users"] Swagger UI에서 이 라우터에대한 태그를 설정하여 API문서에서 그룹화 할수있도록 한다
app.include_router(routers.router, prefix="/users", tags=["users"])

# 이 파일은 Fast API 애플리케이션의 진입점으로 애플리케이션을 초기화하고 데이터베이스 생성, router를 포함하는 역할을 한다 
