from cpu import CPU
from memory import Memory


memory = Memory()

cpu = CPU(memory)


program = [

    ("MOV", 0, 10),

    ("INTERRUPT", 4),

    ("INC", 0),

    ("HALT",),

    ("INC", 0),

    ("IRET",)

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
