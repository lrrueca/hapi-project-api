from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from tortoise.exceptions import DoesNotExist
from ..handlers.delete import delete_account_type_handler


async def delete_account_type_endpoint(request: Request) -> JSONResponse:   
    """
    Handles the deletion of an account type.
    This endpoint expects a DELETE request with the account type ID in the URL path.
    It deletes the account type and returns a JSON response with the status of the operation.
    Args:
        request: The HTTP request object containing the account type ID.
    Returns:
        JSONResponse: A JSON response indicating the result of the deletion operation.
    """
    ppid = request.path_params.get("id")

    try:
        await delete_account_type_handler(ppid)

        return JSONResponse(
            status_code=HTTP_200_OK,
            content={"message": "Account type deleted successfully"},
        )

    except DoesNotExist:
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={"message": "Account type not found"},
        )
