from uvicorn import run
from src import app


if __name__ == "__main__":
    run(app, env_file="./.env.dev")
