# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # 데이터 모델
# class Item(BaseModel):
#     id: int
#     name: str
#     price: float

# # 임시 데이터 저장소
# items = []

# # API 엔드포인트
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.post("/items/", response_model=Item)
# def create_item(item: Item):
#     items.append(item)
#     return item

# @app.get("/items/", response_model=List[Item])
# def read_items():
#     return items

# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int):
#     for item in items:
#         if item.id == item_id:
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from embeddings import EmbeddingService
from rag import RAGService
import numpy as np

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 서비스 초기화
embedding_service = EmbeddingService()
rag_service = RAGService(embedding_service)

# 샘플 Google Ads API 문서 데이터
sample_docs = [
    {
        "content": "test",
        "metadata": "test"
    }
]

# 시작시 문서 임베딩 생성
@app.on_event("startup")
async def startup_event():
    # 문서 저장
    embedding_service.documents = sample_docs
    
    # 임베딩 생성
    texts = [doc["content"] for doc in sample_docs]
    embeddings = embedding_service.create_embeddings(texts)
    
    # FAISS 인덱스 생성
    embedding_service.create_faiss_index(np.array(embeddings))

class Query(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

@app.post("/api/chat", response_model=Response)
async def chat(query: Query):
    try:
        answer = await rag_service.answer_question(query.question)
        return Response(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}