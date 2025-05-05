FROM node:18-alpine

WORKDIR /app

# 의존성 파일 복사 및 설치
COPY package.json package-lock.json* ./
RUN npm install

# 소스 파일 복사
COPY . .

# 개발 서버 실행
CMD ["npm", "start"]