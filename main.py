import asyncio
import clock


async def main(select_time):
    current_clock = clock.Clock(select_time)
    current_clock.set_on_play(True)
    await asyncio.gather(current_clock.run(), current_clock.stop())


if __name__ == "__main__":
    time = int(input("Select time (in seconds) : "))
    input("Launch Clock..")
    asyncio.run(main(time))
