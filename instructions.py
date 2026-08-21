class InstructionSet:

    @staticmethod
    def MOV(cpu, register, value):
        cpu.registers[register] = value

        if value == 0:
            cpu.zero_flag = True
        else:
            cpu.zero_flag = False

    @staticmethod
    def ADD(cpu, register):
        result = cpu.A + cpu.registers[register]

        if result > 255:
            cpu.carry_flag = True
            result = result % 256
        else:
            cpu.carry_flag = False

        cpu.A = result

        if cpu.A == 0:
            cpu.zero_flag = True
        else:
            cpu.zero_flag = False

    @staticmethod
    def HALT(cpu):
        cpu.halted = True
