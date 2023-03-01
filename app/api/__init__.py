import logging
from fastapi import FastAPI


from app.api.routes import root as root_router, public_router
from app.settings import Settings
from app.external.metrics.prometheus import prometheus_middleware
from app.external.reporter import LogReporter


def create_app(settings: Settings):
    app = FastAPI()
    app.reporter = LogReporter()
    app.middleware("http")(prometheus_middleware)
    app.include_router(root_router)
    app.include_router(public_router)

    @app.on_event("startup")
    async def _startup():
        """
        Use this to initialize all of the singleton dependencies and shared
        objects.  i.e. reporters, etc
        """
        init_logger(settings.log_level)

    @app.on_event("shutdown")
    async def _shutdown():
        """
        Clean up before closing the application
        """

        pass

    return app


def init_logger(log_level):
    logging.basicConfig(
        format="%(asctime)s|%(name)s|%(levelname)-5.5s|%(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    logger = logging.getLogger()
    logger.setLevel(log_level)
