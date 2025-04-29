from starlette.routing import Route
from .endpoints.get_all import get_all_account_types_endpoint
from .endpoints.get_one import get_account_type_by_id_endpoint
from .endpoints.create import create_account_type_endpoint
from .endpoints.update import update_account_type_endpoint
from .endpoints.delete import delete_account_type_endpoint


account_type_routes = [
    Route(path="/", endpoint=get_all_account_types_endpoint, methods=["GET"]),
    Route(path="/{id}", endpoint=get_account_type_by_id_endpoint, methods=["GET"], name="get_account_type_by_id"),
    Route(path="/", endpoint=create_account_type_endpoint, methods=["POST"]),
    Route(path="/{id}", endpoint=update_account_type_endpoint, methods=["PUT", "PATCH"]),
    Route(path="/{id}", endpoint=delete_account_type_endpoint, methods=["DELETE"]),
]
