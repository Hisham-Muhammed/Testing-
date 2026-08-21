from instructions import InstructionSet


class CPU:

    def __init__(self, memory):

        self.memory = memory

        # 8-bit registers R0-R7
        self.registers = [0] * 8

        # Accumulator
        self.A = 0

        # Program Counter
        self.PC = 0

        # Stack Pointer
        self.SP = 7

        # Flags
        self.zero_flag = False
        self.carry_flag = False

        # CPU status
        self.halted = False

    def reset(self):

        self.registers = [0] * 8

        self.A = 0
        self.PC = 0
        self.SP = 7

        self.zero_flag = False
        self.carry_flag = False

        self.halted = False

    def fetch(self):

        instruction = self.memory.read_program(self.PC)

        print("FETCH:", instruction)

        return instruction

    def decode_execute(self, instruction):

        if instruction is None:
            print("No instruction at address:", self.PC)
            self.halted = True
            return

        operation = instruction[0]

        print("DECODE:", operation)

        if operation == "MOV":

            register = instruction[1]
            value = instruction[2]

            InstructionSet.MOV(
                self,
                register,
                value
            )

        elif operation == "ADD":

            register = instruction[1]

            InstructionSet.ADD(
                self,
                register
            )

        elif operation == "HALT":

            InstructionSet.HALT(self)

        else:

            print("Unknown instruction:", operation)
            self.halted = True
            return

        if not self.halted:
            self.PC += 1

    def step(self):

        if self.halted:
            return

        instruction = self.fetch()

        self.decode_execute(instruction)

    def show_state(self):

        print("\n----- CPU STATE -----")

        for i in range(8):

            print(f"R{i} =", self.registers[i])

        print("A  =", self.A)
        print("PC =", self.PC)
        print("SP =", self.SP)

        print("Zero Flag  =", self.zero_flag)
        print("Carry Flag =", self.carry_flag)

        print("Halted     =", self.halted)

        print("---------------------")
