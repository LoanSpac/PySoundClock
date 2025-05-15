import asyncio


class Clock:
    def __init__(self):
        time = 10  # Seconds
        play = True

        while play:
            asyncio.run(asyncio.sleep(time))
            input("Play song..")
