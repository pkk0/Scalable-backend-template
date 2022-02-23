from socket import gethostname
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books
from app.settings import settings

params = {
    'title': settings.TITLE,
    'version': settings.VERSION
}
if not settings.API_DOCS_ENABLED:
    params['docs_url'] = None
    params['redocs_url'] = None

app = FastAPI(**params)

#
# Add origins to make sure frontend can work with our API.
#
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(url) for url in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#
#  Add hostname header to every request.
#  Useful for debugging, can be safely removed.
#
@app.middleware('http')
async def add_hostname_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers['hostname'] = gethostname()

    return response


#
# Add more routers here
#
app.include_router(books.router)