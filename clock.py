import asyncio


class Clock:
    """
    @param time : (int) Time in seconds
    """

    def __init__(self, time):
        self.time = time
        self.on_play = False

    def run(self):
        while self.on_play:
            asyncio.run(asyncio.sleep(self.time))
            print("Play song..")

    def get_on_play(self):
        return self.on_play

    def set_on_play(self, on_play):
        self.on_play = on_play
