from fastapi import FastAPI, APIRouter
from backend.app.api.routes import companies_router, leads_router, campaigns_router, emails_router, scrape_router

api_router = APIRouter()

api_router.include_router(companies_router, prefix="/companies", tags=["companies"])
api_router.include_router(leads_router, prefix="/leads", tags=["leads"])
api_router.include_router(campaigns_router, prefix="/campaigns", tags=["campaigns"])
api_router.include_router(emails_router, prefix="/emails", tags=["emails"])
api_router.include_router(scrape_router, prefix="/scrape", tags=["scrape"])

def create_api():
    app = FastAPI(title="CRM API", description="API for CRM system", version="1.0.0")
    app.include_router(api_router, prefix="/api/v1")

    # CORS configuration
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    # Exception handlers
    from fastapi.exceptions import RequestValidationError
    from starlette.exceptions import HTTPException
    from starlette.responses import JSONResponse

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors(), "body": exc.body},
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    return app