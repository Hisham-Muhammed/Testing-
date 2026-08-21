from cpu import CPU
from memory import Memory


memory = Memory()

cpu = CPU(memory)


program = [

    ("MOV", 0, 10),

    ("CALL", 4),

    ("HALT",),

    ("NOP",),

    ("INC", 0),

    ("RET",)

]


for address, instruction in enumerate(program):

    memory.write_program(
        address,
        instruction
    )


print("===== MicroOS-Sim =====")
print()


while not cpu.halted:

    cpu.step()

    cpu.show_state()

    print()
