#!/usr/bin/env python3
import asyncio

"""running multiple coroutine at the same time
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """call wait_random n times with specified max_delay"""
    num_collection = []
    for e in range(n):
        tasks = [wait_random(max_delay) for t in range(n)]
        tasks = asyncio.as_completed(tasks)
        task_collection = [await task for task in tasks]
        return task_collection
