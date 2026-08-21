from instructions import InstructionSet
from stack import Stack


class CPU:

    def __init__(self, memory):

        self.memory = memory

        self.registers = [0] * 8

        self.A = 0

        self.PC = 0

        self.SP = 7

        self.stack = Stack()

        self.zero_flag = False
        self.carry_flag = False

        self.halted = False


    def reset(self):

        self.registers = [0] * 8

        self.A = 0

        self.PC = 0

        self.SP = 7

        self.stack = Stack()

        self.zero_flag = False
        self.carry_flag = False

        self.halted = False


    def fetch(self):

        instruction = self.memory.read_program(self.PC)

        print("FETCH:", instruction)

        return instruction


    def decode_execute(self, instruction):

        if instruction is None:

            print(
                "No instruction at address:",
                self.PC
            )

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


        elif operation == "SUB":

            register = instruction[1]

            InstructionSet.SUB(
                self,
                register
            )


        elif operation == "INC":

            register = instruction[1]

            InstructionSet.INC(
                self,
                register
            )


        elif operation == "DEC":

            register = instruction[1]

            InstructionSet.DEC(
                self,
                register
            )


        elif operation == "PUSH":

            register = instruction[1]

            value = self.registers[register]

            if self.stack.push(value):

                self.SP += 1


        elif operation == "POP":

            register = instruction[1]

            value = self.stack.pop()

            if value is not None:

                self.registers[register] = value

                self.SP -= 1


        elif operation == "CALL":

            target_address = instruction[1]

            return_address = self.PC + 1

            if self.stack.push(return_address):

                self.SP += 1

                self.PC = target_address

                return


        elif operation == "RET":

            return_address = self.stack.pop()

            if return_address is not None:

                self.SP -= 1

                self.PC = return_address

                return


        elif operation == "HALT":

            InstructionSet.HALT(self)


        else:

            print(
                "Unknown instruction:",
                operation
            )

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

            print(
                f"R{i} =",
                self.registers[i]
            )

        print("A  =", self.A)

        print("PC =", self.PC)

        print("SP =", self.SP)

        print(
            "Zero Flag  =",
            self.zero_flag
        )

        print(
            "Carry Flag =",
            self.carry_flag
        )

        print(
            "Halted     =",
            self.halted
        )

        self.stack.show()

        print("---------------------")
