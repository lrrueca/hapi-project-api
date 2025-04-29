from starlette.routing import Route
from .endpoints.get_all import get_all_users_endpoint
from .endpoints.get_one import get_user_by_id_endpoint
from .endpoints.create import create_user_endpoint
from .endpoints.update import update_user_endpoint
from .endpoints.delete import delete_user_endpoint


user_routes = [
    Route(path="/", endpoint=get_all_users_endpoint, methods=["GET"]),
    Route(path="/{id}", endpoint=get_user_by_id_endpoint, methods=["GET"], name="get_user_by_id"),
    Route(path="/", endpoint=create_user_endpoint, methods=["POST"]),
    Route(path="/{id}", endpoint=update_user_endpoint, methods=["PUT", "PATCH"]),
    Route(path="/{id}", endpoint=delete_user_endpoint, methods=["DELETE"]),
]
