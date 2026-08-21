class InterruptController:

    def __init__(self):

        self.pending = False

        self.interrupt_vector = 0


    def request_interrupt(self):

        self.pending = True

        print("Interrupt: REQUESTED")


    def clear_interrupt(self):

        self.pending = False

        print("Interrupt: CLEARED")


    def is_pending(self):

        return self.pending


    def set_vector(self, address):

        self.interrupt_vector = address


    def get_vector(self):

        return self.interrupt_vector


    def show(self):

        print(
            "Interrupt Pending:",
            self.pending
        )

        print(
            "Interrupt Vector:",
            self.interrupt_vector
        )
