import databases
import ujson
from fastapi_plugins import redis_plugin
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import routers
from core.config import settings
from db.session import database

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(routers.api_router, prefix=settings.API_V1_STR)


@app.on_event('startup')
async def on_startup() -> None:
    """Load tarif.json to Redis when the app starts"""
    await redis_plugin.init_app(app, config=settings)
    await redis_plugin.init()
    await database.connect()

    # for big files can try https://stackoverflow.com/a/48229517
    with open('tarif.json', 'r') as file:
        data = ujson.load(file)

    # TODO optimize it for big json
    for key, value in data.items():
        for cargo in value:
            await redis_plugin.redis.hmset_dict(
                key,
                {
                    # the cargo_type is key, the rate is value:
                    cargo["cargo_type"]: cargo["rate"]
                }
            )


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await redis_plugin.terminate()
    await database.disconnect()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", debug=True, reload=True)
