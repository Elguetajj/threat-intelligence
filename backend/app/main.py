from fastapi import FastAPI
import routes.app_router as app_router


app = FastAPI()

app.include_router(app_router.router)

@app.get("/")
async def root():
    return {"threat_radar_api_v": "0.1"}


