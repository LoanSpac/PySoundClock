from ainput import ainput
import asyncio
import sound


class Clock:
    def __init__(self, time):
        """
        :param time:
        """
        self.time = time
        self.on_play = False
        self.sound = sound.Sound()

    async def run(self):
        while self.on_play:
            self.sound.play()
            await asyncio.sleep(self.time)

    async def stop(self):
        await ainput("Enter to stop..")
        self.on_play = False

    def get_on_play(self):
        return self.on_play

    def set_on_play(self, on_play):
        self.on_play = on_play
