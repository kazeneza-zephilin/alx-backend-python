#!/usr/bin/env python3
"""async comprehension"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float]:
    """wait 1 sec asynchronous then yield random number"""
    for i in range(10):
        res = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield res
