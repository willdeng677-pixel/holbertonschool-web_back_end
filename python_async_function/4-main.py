#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

print(asyncio.run(task_wait_n(5, 5)))
print(asyncio.run(task_wait_n(10, 7)))
print(asyncio.run(task_wait_n(10, 0)))
