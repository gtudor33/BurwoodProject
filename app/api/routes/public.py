from fastapi import APIRouter, Request, Depends, HTTPException, Form
from app.api.dependencies import get_fizzbuzz_client
from app.clients.fizzbuzz import FizzBuzzClient
from app.external.metrics.prometheus import timing_metrics

public_router = APIRouter()
ENDPOINTS = {"fizzbuzz_number": "/fizzbuzz", "most_common": "/most_common"}


@public_router.post(ENDPOINTS["fizzbuzz_number"], tags=["Fizz Buzz Number"])
async def get_fizzbuzz_number(
    request: Request,
    number: int = Form(...),
    fizzbuzz_client: FizzBuzzClient = Depends(get_fizzbuzz_client),
):
    """
    request: Pass in the request in order to measure the metrics.
    number: It takes an int form and used as Form in order to accommodate the frontend part as well.
    fuzzbuzz_client: The client side where the outputs are formed.
    """
    with timing_metrics(request, "fizzbuzz_timing"):
        if number <= 0:
            raise HTTPException(
                status_code=400, detail="Must submit a number greater than 0!"
            )
        try:
            response = await fizzbuzz_client.get_fizzbuzz_number(request, number)
        except Exception as e:
            raise e

    return response


@public_router.get(ENDPOINTS["most_common"], tags=["Fizz Buzz Top 3"])
async def get_most_common_numbers(
    request: Request, fizzbuzz_client: FizzBuzzClient = Depends(get_fizzbuzz_client)
):
    with timing_metrics(request, "most_common_timing"):
        try:
            response = await fizzbuzz_client.get_fizzbuzz_top_3_results(request)
        except Exception as e:
            raise e

    return response
