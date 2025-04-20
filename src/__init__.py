from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount

from .application.lifespan import lifespan
from .domains.user.routes import user_routes


async def homepage(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/api", endpoint=homepage),
    Mount("/api", routes=user_routes),  # Mounting user routes
]

app = Starlette(debug=True, lifespan=lifespan, routes=routes)
