from fastapi import FastAPI
import routes.app_router
import routes.cve_router
import routes.api_router



app = FastAPI(debug=True)

app.include_router(routes.app_router.router)
app.include_router(routes.cve_router.router)
app.include_router(routes.api_router.router)


@app.get("/")
async def root():
    return {"threat_radar_api_v": "0.1"}


