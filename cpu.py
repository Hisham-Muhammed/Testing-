class CPU:
    def __init__(self):
        # 8-bit registers R0 to R7
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

    def reset(self):
        self.registers = [0] * 8
        self.A = 0
        self.PC = 0
        self.SP = 7
        self.zero_flag = False
        self.carry_flag = False

    def show_state(self):
        print("----- CPU STATE -----")

        for i in range(8):
            print(f"R{i} =", self.registers[i])

        print("A  =", self.A)
        print("PC =", self.PC)
        print("SP =", self.SP)

        print("Zero Flag  =", self.zero_flag)
        print("Carry Flag =", self.carry_flag)

        print("---------------------")
