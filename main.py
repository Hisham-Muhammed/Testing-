from cpu import CPU
from memory import Memory


# Create memory
memory = Memory()

# Create CPU
cpu = CPU(memory)


# Program to execute
program = [
    ("MOV", 0, 10),
    ("MOV", 1, 5),
    ("INC", 0),
    ("DEC", 1),
    ("ADD", 0),
    ("SUB", 1),
    ("HALT",)
]


# Load program into program memory
for address, instruction in enumerate(program):
    memory.write_program(address, instruction)


print("===== MicroOS-Sim =====")
print()


# Fetch-Decode-Execute cycle
while not cpu.halted:

    cpu.step()

    cpu.show_state()

    print()
