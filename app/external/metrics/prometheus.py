from typing import Union
from collections import namedtuple
from time import monotonic

import typing
import prometheus_client

SpamLabels = namedtuple("SpamLabels", ["method", "path", "spam_name"])
CounterLabels = namedtuple("CounterLabels", ["endpoint"])
HTTPLabels = namedtuple("HTTPLabels", ["method", "path", "http_status"])

BUCKETS = (
    # these are log spaced with 1 sig-fig rounding so there are 3 per decade
    # 2 div/decade = 1,       3.16,       10
    # 3 div/decade = 1,   2.15,   4.64,   10
    # 4 div/decade = 1, 1.78, 3.16, 5.62, 10
    0.0002,  # 200 μs
    0.0005,
    0.001,  # 1 ms
    0.002,
    0.005,
    0.01,
    0.02,
    0.05,
    0.1,
    0.2,
    0.5,
    1,
    2,
    5,
    10,
    20,  # default envoy timeout is 15 seconds, bin up to that time
    float("inf"),
)


def get_path(routes, scope):
    path = "path-not-found"
    for route in routes:
        _, matches = route.matches(scope)
        if len(matches) > 0:
            path = route.path
    return path


async def prometheus_middleware(request, call_next):
    start_time = monotonic()
    response = await call_next(request)
    elapsed_sec = monotonic() - start_time
    path = get_path(request.app.routes, request.scope)

    labels = HTTPLabels(
        method=request.method,
        path=path,
        http_status=response.status_code,
    )
    http_histogram.labels(*labels).observe(elapsed_sec)

    return response


def setup_metrics_factory(registry, name, documentation, labelnames):
    """Setup prometheus metrics"""
    prom_histogram = prometheus_client.Histogram(
        name=name,
        documentation=documentation,
        labelnames=labelnames,
        registry=registry,
        buckets=BUCKETS,
    )

    return prom_histogram


def setup_http_metrics(registry):
    prom_histogram = setup_metrics_factory(
        registry,
        name="http_request_duration_seconds",
        documentation="Request duration (seconds)",
        labelnames=HTTPLabels._fields,
    )

    return prom_histogram


def setup_spam_metrics(registry):
    prom_histogram = setup_metrics_factory(
        registry,
        name="internal_function_duration_seconds",
        documentation="internal function duration (seconds)",
        labelnames=SpamLabels._fields,
    )
    return prom_histogram


def ctx_histogram_timer(labels: Union[HTTPLabels, SpamLabels]):
    """
    Context manager for methods timer
    Usage:
        Context manager
        ```
        labels = SpamLabels(method="GET", path="/abc", spam_name="abc")
        with ctx_histogram_timer(labels):
            abc()
            ...
        ```
        Decorator:
        ```
            labels = SpamLabels(method="GET", path="/abc", spam_name="abc")
            @ctx_histogram_timer(labels)
            def meh():
                abc()
        ```
    See more:
    # pylint: disable=line-too-long
     - https://github.com/prometheus/client_python#histogram
    """
    return spam_histogram.labels(*labels).time()


def timing_metrics(request, spam_name):
    """Handy proxy to ctx_histogram_timer to be used with a request
    Usage:
        ```
        with timing_metrics(request, "my_method_to_be_instrumented"):
            abc()
            ...
        ```
    """

    method = request.method
    path = get_path(request.app.routes, request.scope)

    labels = SpamLabels(method=method, path=path, spam_name=spam_name)
    return ctx_histogram_timer(labels)


http_histogram = setup_http_metrics(registry=prometheus_client.REGISTRY)
spam_histogram = setup_spam_metrics(registry=prometheus_client.REGISTRY)


def metrics():
    return (
        prometheus_client.generate_latest(prometheus_client.REGISTRY),
        prometheus_client.CONTENT_TYPE_LATEST,
    )
