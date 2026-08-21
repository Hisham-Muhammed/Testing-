from cpu import CPU
from memory import Memory
from process_manager import ProcessManager
from scheduler import Scheduler


print("===== FCFS SCHEDULING TEST =====")


# Create process manager
process_manager = ProcessManager()

# Create scheduler
scheduler = Scheduler()


# Program 1
program1 = [
    ("MOV", 0, 10),
    ("INC", 0),
    ("HALT",)
]


# Program 2
program2 = [
    ("MOV", 1, 20),
    ("INC", 1),
    ("INC", 1),
    ("HALT",)
]


# Program 3
program3 = [
    ("MOV", 2, 30),
    ("INC", 2),
    ("HALT",)
]


# Create processes
p1 = process_manager.create_process(
    program1,
    priority=2,
    arrival_time=0
)

p2 = process_manager.create_process(
    program2,
    priority=1,
    arrival_time=0
)

p3 = process_manager.create_process(
    program3,
    priority=3,
    arrival_time=0
)


# Add processes to scheduler
scheduler.add_process(p1)
scheduler.add_process(p2)
scheduler.add_process(p3)


# Show initial state
process_manager.show_processes()

scheduler.show_status()


# FCFS execution
while True:

    process = scheduler.fcfs()

    if process is None:
        break

    print()
    print(
        f"----- Running Process P{process.pid} -----"
    )

    memory = Memory()

    cpu = CPU(memory)

    # Load process program
    for address, instruction in enumerate(
        process.program
    ):

        memory.write_program(
            address,
            instruction
        )


    # Execute process
    while not cpu.halted:

        cpu.step()

        process.pc = cpu.PC

        scheduler.time += 1


    # Process finished
    process.remaining_time = 0

    scheduler.finish_current_process()

    print(
        f"P{process.pid} completed."
    )

    print(
        f"CPU time: {scheduler.time}"
    )

    print()


print("\n===== FCFS COMPLETE =====")

process_manager.show_processes()

scheduler.show_status()
