from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from tortoise.exceptions import DoesNotExist
from ..handlers.update import update_account_type_handler


async def update_account_type_endpoint(request: Request) -> JSONResponse:
    """
    Update account type endpoint.
    Args:
        request (Request): The request object.
    Returns:
        JSONResponse: The response object.
    """
    ppid = request.path_params.get("id")
    payload = await request.json()

    try:
        await update_account_type_handler(ppid, payload["data"])
        return JSONResponse(
            content={
                "message": "Account type updated successfully",
            },
            status_code=HTTP_200_OK,
        )

    except DoesNotExist:
        return JSONResponse(
            content={
                "message": "Account type not found",
            },
            status_code=HTTP_404_NOT_FOUND,
        )
