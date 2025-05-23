import clock

if __name__ == "__main__":
    input("Launch Clock..")
    current_clock = clock.Clock(5)
    current_clock.set_on_play(True)
    current_clock.run()
