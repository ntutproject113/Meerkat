from fastapi.middleware.cors import CORSMiddleware
def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # 允許的前端
        allow_credentials=True,  # 支援 Cookie / Authorization
        allow_methods=["*"],     # 允許所有 HTTP 方法
        allow_headers=["*"],     # 允許所有 header
    )
