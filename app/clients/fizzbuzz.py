import logging
from collections import Counter

import httpx

numbers = []


class FizzBuzzClient:
    def __init__(self):
        self.logger = logging

    async def get_fizzbuzz_number(self, request, number: int) -> dict:
        self.logger.info(f"[fizzbuzz client REQUEST] {request.method} {request.url} ")
        result = ""

        try:
            numbers.append(number)
            if number % 15 == 0:
                result += "FizzBuzz"
            elif number % 3 == 0:
                result += "Fizz"
            elif number % 5 == 0:
                result += "Buzz"
            else:
                result += str(number)
        except httpx.TimeoutException as exc:
            raise exc

        return {"result": result}

    async def get_fizzbuzz_top_3_results(self, request) -> dict:
        self.logger.info(
            f"[fizzbuzz client most common REQUEST] {request.method} {request.url} "
        )
        counter = Counter(numbers)
        top_counts = counter.most_common(3)
        return {"result": top_counts}
