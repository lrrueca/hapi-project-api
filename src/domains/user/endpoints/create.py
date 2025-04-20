from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY
from pydantic_core import ValidationError

from ..handlers.create import create_user_handler
from ....application.response import error_response


async def create_user_endpoint(request: Request) -> JSONResponse:
    """
    Handles the creation of a new user.
    This endpoint expects a POST request with user data in the request body.
    It creates a new user and returns a JSON response with the status of the operation.
    Args:
        request: The HTTP request object containing the user data.
    Returns:
        JSONResponse: A JSON response indicating the result of the creation operation.
    """
    payload = await request.json()
    try:
        data = payload["data"]
        uid = await create_user_handler(data)
        url = request.url_for("get_user_by_id", id=str(uid))

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
