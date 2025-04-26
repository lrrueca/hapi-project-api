from starlette.routing import Route
from .endpoints.get_all import get_all_account_types_endpoint
from .endpoints.get_one import get_account_type_by_id_endpoint


account_type_routes = [
    Route(path="/account_types", endpoint=get_all_account_types_endpoint, methods=["GET"]),
    Route(path="/account_types/{id}", endpoint=get_account_type_by_id_endpoint, methods=["GET"], name="get_account_type_by_id"),
]
