from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from ..handlers.get_all import get_all_account_types_handler


async def get_all_account_types_endpoint(request: Request) -> JSONResponse: 
    """
    Get all account types endpoint.
    Args:
        request (Request): The request object.
    Returns:
        JSONResponse: The response object.
    """
    try:
        content = await get_all_account_types_handler()
        return JSONResponse(content=content, status_code=HTTP_200_OK)

    except Exception:
        return JSONResponse(
            content={"error": "An error occurred while retrieving account types."},
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        )
