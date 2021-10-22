import asyncio
import urllib.request as req
import time

async def ask():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    # data = urllib.urlencode({'name' : 'joe', 'age'  : '10'})
    reqURL = req.Request(url)
    response = req.urlopen(reqURL)
    print(response.read()) 




async def main():
    # =======================
    # To run as async promise => 
    # 1. create async def
    # 2. create_task to wrap the promise you want to run
    # =======================

    asyncio.create_task(ask())
    print(f"started at {time.strftime('%X')}")
    anw = 36 * 16
    print(anw)
    print(f"finished at {time.strftime('%X')}")

# .run => run as asynchrous
# asyncio.create_task(ask()) => create async task
asyncio.run(main())


# async def main():
# await function_that_returns_a_future_object()


#========= Promise.all================================
# # this is also valid:
# await asyncio.gather(
# function_that_returns_a_future_object(),
# some_python_coroutine()
# )

# asyncio.shield => shield from cancellation



# ===========================
# Sleeping  Time.sleep  => within that async function

# import asyncio
# import datetime

# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)

# asyncio.run(display_date())


# asyncio.wait_for => wait for centainty time for promise
# if no promise within the time, action cancell

# async def eternity():
#     # Sleep for one hour
#     await asyncio.sleep(3600)
#     print('yay!')

# async def main():
#     # Wait for at most 1 second
#     try:
#         await asyncio.wait_for(eternity(), timeout=1.0)
#     except asyncio.TimeoutError:
#         print('timeout!')

# asyncio.run(main())