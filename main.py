from cpu import CPU
from memory import Memory


# Create memory
memory = Memory()


# Create CPU
cpu = CPU(memory)


# Program
program = [

    ("MOV", 0, 10),

    ("MOV", 1, 20),

    ("ADD", 0),

    ("HALT",)

]


# Load program into program memory

for address, instruction in enumerate(program):

    memory.write_program(
        address,
        instruction
    )


print("===== MicroOS-Sim =====")
print()


# CPU execution loop

while not cpu.halted:

    cpu.step()

    cpu.show_state()

    print()
