class InstructionSet:

    @staticmethod
    def MOV(cpu, register, value):

        value = value % 256

        cpu.registers[register] = value

        cpu.zero_flag = (value == 0)


    @staticmethod
    def ADD(cpu, register):

        result = cpu.A + cpu.registers[register]

        if result > 255:
            cpu.carry_flag = True
            result = result % 256
        else:
            cpu.carry_flag = False

        cpu.A = result

        cpu.zero_flag = (cpu.A == 0)


    @staticmethod
    def SUB(cpu, register):

        result = cpu.A - cpu.registers[register]

        if result < 0:
            cpu.carry_flag = True
            result = result % 256
        else:
            cpu.carry_flag = False

        cpu.A = result

        cpu.zero_flag = (cpu.A == 0)


    @staticmethod
    def INC(cpu, register):

        cpu.registers[register] += 1

        if cpu.registers[register] > 255:
            cpu.registers[register] = 0

        cpu.zero_flag = (
            cpu.registers[register] == 0
        )


    @staticmethod
    def DEC(cpu, register):

        cpu.registers[register] -= 1

        if cpu.registers[register] < 0:
            cpu.registers[register] = 255

        cpu.zero_flag = (
            cpu.registers[register] == 0
        )


    @staticmethod
    def HALT(cpu):

        cpu.halted = True
