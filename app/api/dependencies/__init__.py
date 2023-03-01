"""
This module contains fastapi dependencies.

See: https://fastapi.tiangolo.com/tutorial/dependencies/
"""
from app.clients.fizzbuzz import FizzBuzzClient


async def get_fizzbuzz_client():
    return FizzBuzzClient()
