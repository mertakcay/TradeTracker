from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()
# app.include_router(gym_classes_router)
# app.include_router(clients_router)
# app.include_router(gym_passes_router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema  # type: ignore

    openapi_schema = get_openapi(
        title="hexagonal-architecture-python",
        version="1.0.0",
        description="Hexagonal architecture in Python build on top of FastAPI",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema  # type: ignore


app.openapi = custom_openapi  # type: ignore

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)