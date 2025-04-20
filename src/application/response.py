from typing import Callable


error_response: Callable[[str], dict] = lambda e: {"message": "Invalid data", "errors": e}
