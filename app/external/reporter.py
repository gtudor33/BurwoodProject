import logging

from typing import Mapping

logger = logging.getLogger()


class LogReporter:
    def debug(self, msg: str, *args, **kwargs):
        logger.debug(msg)

    def info(self, msg: str, *args, **kwargs):
        logger.info(msg)

    def warning(
        self,
        exc: Exception,
        context: str = None,
        cause: Exception = None,
        meta_data: Mapping = None,
    ):
        logger.warning("[%s] %s: %s", exc.__class__.__name__, exc, meta_data)

    def error(
        self,
        exc: Exception,
        context: str = None,
        cause: Exception = None,
        meta_data: Mapping = None,
    ):
        logger.error(
            "[%s] %s: %s",
            exc.__class__.__name__,
            exc,
            meta_data,
            exc_info=True,
        )

    def counter(
        self,
        meas: str,
        tags: Mapping[str, str],
        value: int = 1,
        *,
        prefix: bool = True,  # pylint: disable=W0613
    ) -> None:
        return

    def gauge(
        self,
        meas: str,
        tags: Mapping[str, str],
        value: int,
        *,
        prefix: bool = True,  # pylint: disable=W0613
    ) -> None:
        return

    def timer(
        self,
        meas: str,
        tags: Mapping[str, str],
        value: int,
        *,
        prefix: bool = True,  # pylint: disable=W0613
    ) -> None:
        return

    def http_timer(
        self,
        method: str,
        path: str,
        returned_status: int,
        status: str,
        duration_ms: int,
        user_id: str = None,
    ):  # pylint: disable=R0913
        return

    def rmq_counter(self, action: str, routing_key: str, status: str):
        return
