from instructions import InstructionSet


class CPU:

    def __init__(self):

        self.registers = [0] * 8

        self.A = 0

        self.PC = 0

        self.SP = 7

        self.zero_flag = False
        self.carry_flag = False

        self.halted = False

    def reset(self):

        self.registers = [0] * 8

        self.A = 0
        self.PC = 0
        self.SP = 7

        self.zero_flag = False
        self.carry_flag = False

        self.halted = False

    def execute(self, instruction):

        operation = instruction[0]

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
            return

        self.PC += 1

    def show_state(self):

        print("----- CPU STATE -----")

        for i in range(8):

            print(f"R{i} =", self.registers[i])

        print("A  =", self.A)
        print("PC =", self.PC)
        print("SP =", self.SP)

        print("Zero Flag  =", self.zero_flag)
        print("Carry Flag =", self.carry_flag)

        print("Halted     =", self.halted)

        print("---------------------")
