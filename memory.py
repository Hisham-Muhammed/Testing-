class Memory:
    def __init__(self):
        # 256 locations for program memory
        self.program_memory = [None] * 256

        # 256 locations for data memory
        self.data_memory = [0] * 256

    def write_program(self, address, instruction):
        self.program_memory[address] = instruction

    def read_program(self, address):
        return self.program_memory[address]

    def write_data(self, address, value):
        self.data_memory[address] = value

    def read_data(self, address):
        return self.data_memory[address]

    def show_program_memory(self):
        print("----- PROGRAM MEMORY -----")

        for address, instruction in enumerate(self.program_memory):
            if instruction is not None:
                print(address, ":", instruction)

    def show_data_memory(self):
        print("----- DATA MEMORY -----")

        for address, value in enumerate(self.data_memory):
            if value != 0:
                print(address, ":", value)
