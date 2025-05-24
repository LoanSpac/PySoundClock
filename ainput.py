import asyncio
from concurrent.futures import ThreadPoolExecutor


async def ainput(prompt: str = "") -> str:
    """
    source : https://gist.github.com/delivrance/675a4295ce7dc70f0ce0b164fcdbd798

    :param prompt:
    :return:
    """
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)
