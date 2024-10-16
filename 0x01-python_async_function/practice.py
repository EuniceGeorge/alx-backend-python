#!/usr/bin/env python3

import asyncio

async def fetch_data(delay):
    print("fetching data...")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"data": "some data"}

async def main():
    print("start of main function")
    task = fetch_data(2)
    result = await task
    print(f"Received result: {result}")
    print("end of main")


asyncio.run(main())
