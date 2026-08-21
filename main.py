from cpu import CPU
from memory import Memory


# Create memory
memory = Memory()

# Create CPU
cpu = CPU(memory)


# Program to test PUSH and POP
program = [

    ("MOV", 0, 10),

    ("PUSH", 0),

    ("MOV", 1, 20),

    ("POP", 1),

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


# Fetch-Decode-Execute cycle
while not cpu.halted:

    cpu.step()

    cpu.show_state()

    print()
