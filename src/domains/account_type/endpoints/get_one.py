from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from tortoise.exceptions import DoesNotExist
from pydantic import ValidationError
from ..handlers.get_one import get_account_type_by_id_handler


async def get_account_type_by_id_endpoint(request: Request) -> JSONResponse:    
    """
    Get account type by ID endpoint.
    Args:
        request (Request): The request object.
    Returns:
        JSONResponse: The response object.
    """
    ppid = request.path_params.get("id")
    try:
        content = await get_account_type_by_id_handler(ppid)
        return JSONResponse(content=content, status_code=HTTP_200_OK)

    except (DoesNotExist, ValidationError):
        return JSONResponse(content={"error": "Account type not found"}, status_code=HTTP_404_NOT_FOUND)
    