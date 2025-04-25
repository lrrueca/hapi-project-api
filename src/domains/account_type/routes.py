from starlette.routing import Route
from .endpoints.get_all import get_all_account_types_endpoint


account_type_routes = [
    Route(path="/account_types", endpoint=get_all_account_types_endpoint, methods=["GET"]),
]
