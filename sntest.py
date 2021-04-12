import asyncio 
from datetime import datetime

async def gen_time(delay=1):
    while True:
        await asyncio.sleep(delay)
        yield {'time':datetime.now().strftime("%X: %x")}

def dump(d):
    print(d)
    return d
