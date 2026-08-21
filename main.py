from cpu import CPU
from memory import Memory


# Create memory
memory = Memory()

# Create CPU
cpu = CPU(memory)


# Program to test CALL and RET
program = [

    ("MOV", 0, 10),

    ("CALL", 3),

    ("HALT",),

    ("INC", 0),

    ("RET",)

]


# Load program into program memory
for address, instruction in enumerate(program):

    memory.write_program(
        address,
        instruction
    )


print("===== MicroOS-Sim =====")
print()


# Fetch-Decode-Execute cycle
while not cpu.halted:

    cpu.step()

    cpu.show_state()

    print()
