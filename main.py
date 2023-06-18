import uvicorn
from src.views.api import app


if __name__ == '__main__':
    uvicorn.run(
        app, host="localhost", port=6000
    )
