#!/usr/bin/env python3

import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

n = 5
max_delay = 6

print(asyncio.run(wait_n(n, max_delay)))

