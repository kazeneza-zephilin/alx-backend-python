#!/usr/bin/env python3
"""defining the basic of asychronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waiting for number of max_delay"""
    rn = random.uniform(0, max_delay + 1)
    await asyncio.sleep(max_delay)
    return rn
