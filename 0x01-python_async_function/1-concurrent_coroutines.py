#!/usr/bin/env python3
"""running multiple coroutine at the same time
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """call wait_random n times with specified max_delay"""
    tasks = [wait_random(max_delay) for t in range(n)]
    tasks = asyncio.as_completed(tasks)
    task_collection = [await task for task in tasks]
    return task_collection
