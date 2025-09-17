from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from template_test_api.log import configure_logging
from template_test_api.web.api.router import api_router
from template_test_api.web.lifespan import lifespan_setup


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="template_test_api",
        version=metadata.version("template_test_api"),
        lifespan=lifespan_setup,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Main router for the API.
    app.include_router(api_router, prefix="/api")

    return app
    app.include_router(router=api_router, prefix="/api")

    return app
