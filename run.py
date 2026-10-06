import os
import sys
import uvicorn

if __name__ == "__main__":
    print("=" * 65)
    print("   EventPulse - Event Management System (FastAPI + SQLite)")
    print("=" * 65)
    print(" -> Web Application:    http://127.0.0.1:8000")
    print(" -> Swagger API Docs:   http://127.0.0.1:8000/docs")
    print(" -> ReDoc Alternative:  http://127.0.0.1:8000/redoc")
    print("=" * 65)
    print(" Starting server with auto-reload enabled...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
