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


    elif operation == "HALT":

        InstructionSet.HALT(self)


    else:

        print("Unknown instruction:", operation)

        self.halted = True

        return


    if not self.halted:

        self.PC += 1            print(f"R{i} =", self.registers[i])

        print("A  =", self.A)
        print("PC =", self.PC)
        print("SP =", self.SP)

        print("Zero Flag  =", self.zero_flag)
        print("Carry Flag =", self.carry_flag)

        print("Halted     =", self.halted)

        print("---------------------")
