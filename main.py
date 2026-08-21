from cpu import CPU
from memory import Memory


# Create memory
memory = Memory()

# Create CPU
cpu = CPU(memory)


# Program to test GPIO
program = [

    ("SET_PIN", 2),

    ("READ_PIN", 2),

    ("CLEAR_PIN", 2),

    ("READ_PIN", 2),

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
