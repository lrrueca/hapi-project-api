from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from tortoise.exceptions import DoesNotExist
from ..handlers.delete import delete_user_handler


async def delete_user_endpoint(request: Request) -> JSONResponse:
    """
    Handles the deletion of a user.
    This endpoint expects a DELETE request with the user ID in the URL path.
    It deletes the user and returns a JSON response with the status of the operation.
    Args:
        request: The HTTP request object containing the user ID.
    Returns:
        JSONResponse: A JSON response indicating the result of the deletion operation.
    """
    ppid = request.path_params.get("id")

    try:
        await delete_user_handler(ppid)

        return JSONResponse(
            status_code=HTTP_200_OK,
            content={"message": "User deleted successfully"},
        )

    except DoesNotExist:
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={"message": "User not found"},
        )
