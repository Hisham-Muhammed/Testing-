from cpu import CPU
from memory import Memory


# Create memory
memory = Memory()

# Create CPU
cpu = CPU(memory)


# Program to test Timer
program = [

    ("TIMER_RESET",),

    ("TIMER_START",),

    ("TIMER_READ",),

    ("MOV", 0, 10),

    ("INC", 0),

    ("TIMER_READ",),

    ("TIMER_STOP",),

    ("TIMER_READ",),

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
