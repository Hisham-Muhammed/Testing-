from cpu import CPU
from memory import Memory


class Simulator:

    def __init__(self):

        self.program = []

        self.cpu = None

        self.memory = None

        self.running = False


    def load_program(self, program):

        self.program = program

        self.reset()

        print("Program loaded successfully.")

        print(
            f"Instructions: {len(self.program)}"
        )


    def reset(self):

        self.memory = Memory()

        self.cpu = CPU(self.memory)

        self.running = False

        for address, instruction in enumerate(
            self.program
        ):

            self.memory.write_program(
                address,
                instruction
            )

        print("Simulator reset.")


    def step(self):

        if self.cpu is None:

            print("No program loaded.")

            return

        if self.cpu.halted:

            print("CPU is already halted.")

            return

        self.cpu.step()


    def run(self):

        if self.cpu is None:

            print("No program loaded.")

            return

        self.running = True

        print("\n===== PROGRAM RUNNING =====")

        while not self.cpu.halted:

            self.cpu.step()

        self.running = False

        print("\n===== PROGRAM FINISHED =====")


    def show_state(self):

        if self.cpu is None:

            print("No program loaded.")

            return

        print("\n===== SIMULATOR STATE =====")

        print(
            f"PC     : {self.cpu.PC}"
        )

        print(
            f"SP     : {self.cpu.SP}"
        )

        print(
            f"Halted : {self.cpu.halted}"
        )

        print(
            f"R0     : {self.cpu.registers[0]}"
        )

        print(
            f"R1     : {self.cpu.registers[1]}"
        )

        print(
            f"R2     : {self.cpu.registers[2]}"
        )

        print(
            f"R3     : {self.cpu.registers[3]}"
        )

        print(
            f"R4     : {self.cpu.registers[4]}"
        )

        print(
            f"R5     : {self.cpu.registers[5]}"
        )

        print(
            f"R6     : {self.cpu.registers[6]}"
        )

        print(
            f"R7     : {self.cpu.registers[7]}"
        )

        print(
            f"Stack  : {self.cpu.stack}"
        )

        print(
            "==========================="
        )


def main():

    simulator = Simulator()


    program = [

        ("MOV", 0, 10),

        ("INC", 0),

        ("MOV", 1, 20),

        ("PUSH", 0),

        ("POP", 1),

        ("HALT",)

    ]


    while True:

        print("\n===== MicroOS-Sim =====")

        print("1. Load Program")

        print("2. Run")

        print("3. Single Step")

        print("4. Show CPU State")

        print("5. Reset")

        print("6. Exit")


        choice = input(
            "Enter choice: "
        )


        if choice == "1":

            simulator.load_program(
                program
            )


        elif choice == "2":

            simulator.run()


        elif choice == "3":

            simulator.step()


        elif choice == "4":

            simulator.show_state()


        elif choice == "5":

            simulator.reset()


        elif choice == "6":

            print("Exiting MicroOS-Sim.")

            break


        else:

            print(
                "Invalid choice."
            )


if __name__ == "__main__":

    main()
