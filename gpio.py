class GPIO:

    def __init__(self, number_of_pins=8):

        self.number_of_pins = number_of_pins

        self.pins = [0] * number_of_pins


    def set_pin(self, pin):

        if 0 <= pin < self.number_of_pins:

            self.pins[pin] = 1

            print(
                f"GPIO Pin {pin}: ON"
            )

        else:

            print(
                f"Invalid GPIO Pin: {pin}"
            )


    def clear_pin(self, pin):

        if 0 <= pin < self.number_of_pins:

            self.pins[pin] = 0

            print(
                f"GPIO Pin {pin}: OFF"
            )

        else:

            print(
                f"Invalid GPIO Pin: {pin}"
            )


    def read_pin(self, pin):

        if 0 <= pin < self.number_of_pins:

            return self.pins[pin]

        print(
            f"Invalid GPIO Pin: {pin}"
        )

        return None


    def show(self):

        print(
            "GPIO Pins:",
            self.pins
        )
