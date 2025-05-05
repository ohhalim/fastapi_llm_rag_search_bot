import httpx
import json

class RAGService:
    def __init__(self, embedding_service):
        self.embedding_service = embedding_service
        self.ollama_url = "http://ollama:11434/api/generate"
        
    async def get_llm_response(self, prompt):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.ollama_url,
                json={  
                    "model": "tinyllama:latest",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60.0
            )
            return response.json()["response"]
    
    async def answer_question(self, question):
        # 관련 문서 검색
        relevant_docs = self.embedding_service.search_similar(question, k=3)
        
        # 컨텍스트 생성
        context = "\n\n".join([doc['content'] for doc in relevant_docs])
        
        # 프롬프트 생성
        prompt = f"""You are a Google Ads API expert. Use the following information to answer the question.

Context:
{context}

Question: {question}

Answer: Please provide a detailed answer based on the context above."""
        
        # LLM 응답 생성
        response = await self.get_llm_response(prompt)
        return response