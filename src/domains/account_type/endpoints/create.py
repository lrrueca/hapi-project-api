from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY
from pydantic_core import ValidationError

from ..handlers.create import create_account_type_handler
from ....application.response import error_response


async def create_account_type_endpoint(request: Request) -> JSONResponse:
    """
    Handles the creation of a new account type.
    This endpoint expects a POST request with account type data in the request body.
    It creates a new account type and returns a JSON response with the status of the operation.
    Args:
        request: The HTTP request object containing the account type data.
    Returns:
        JSONResponse: A JSON response indicating the result of the creation operation.
    """
    payload = await request.json()
    try:
        data: dict = payload["data"]
        id: int = await create_account_type_handler(data)
        url = request.url_for("get_account_type_by_id", id=str(id))

        return JSONResponse(
            content={"message": "ok"},
            status_code=HTTP_201_CREATED,
            headers={"location": str(url)},
        )

    except KeyError as e:
        return JSONResponse(
            content=error_response({"loc": e.args}),
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        )

    except ValidationError as e:
        return JSONResponse(
            content=error_response(
                e.errors(include_url=False, include_context=False, include_input=False)
            ),
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        )
