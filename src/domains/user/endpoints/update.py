from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from tortoise.exceptions import DoesNotExist
from ..handlers.update import update_user_handler


async def update_user_endpoint(request: Request) -> JSONResponse:
    """
    Update user endpoint.
    Args:
        request (Request): The request object.
    Returns:
        JSONResponse: The response object.
    """
    ppid = request.path_params.get("id")
    payload = await request.json()

    try:
        await update_user_handler(ppid, payload["data"])
        return JSONResponse(
            content={
                "message": "User updated successfully",
            },
            status_code=HTTP_200_OK,
        )

    except DoesNotExist:
        return JSONResponse(
            content={
                "message": "User not found",
            },
            status_code=HTTP_404_NOT_FOUND,
        )
