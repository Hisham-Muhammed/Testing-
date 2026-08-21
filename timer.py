class Timer:

    def __init__(self):

        self.counter = 0

        self.running = False


    def start(self):

        self.running = True

        print("Timer: STARTED")


    def stop(self):

        self.running = False

        print("Timer: STOPPED")


    def reset(self):

        self.counter = 0

        print("Timer: RESET")


    def tick(self):

        if self.running:

            self.counter += 1


    def get_value(self):

        return self.counter


    def show(self):

        status = "RUNNING" if self.running else "STOPPED"

        print(
            f"Timer: {self.counter} | {status}"
        )
