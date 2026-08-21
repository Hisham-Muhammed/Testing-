from cpu import CPU
from memory import Memory
from process_manager import ProcessManager


print("===== PRIORITY SCHEDULING TEST =====")


# Create process manager
process_manager = ProcessManager()


# -------------------------
# Programs
# -------------------------

program1 = [
    ("MOV", 0, 10),
    ("INC", 0),
    ("HALT",)
]


program2 = [
    ("MOV", 1, 20),
    ("INC", 1),
    ("INC", 1),
    ("HALT",)
]


program3 = [
    ("MOV", 2, 30),
    ("INC", 2),
    ("HALT",)
]


# -------------------------
# Create processes
# -------------------------

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


processes = [p1, p2, p3]


# -------------------------
# Priority Scheduling
# -------------------------

time = 0

context_switches = 0

completed = []


while len(completed) < len(processes):

    # Find READY processes
    ready_processes = [
        process
        for process in processes
        if (
            not process.completed
            and process.state == "READY"
        )
    ]

    if not ready_processes:
        break


    # Smaller priority number
    # means higher priority
    process = min(
        ready_processes,
        key=lambda p: p.priority
    )


    print()
    print(
        f"===== Running P{process.pid} "
        f"(Priority {process.priority}) ====="
    )


    process.set_state("RUNNING")


    memory = Memory()

    cpu = CPU(memory)


    # Load program
    for address, instruction in enumerate(
        process.program
    ):

        memory.write_program(
            address,
            instruction
        )


    # Restore PC
    cpu.PC = process.pc


    # Execute until completion
    while not cpu.halted:

        cpu.step()

        process.pc = cpu.PC

        time += 1


    # Process completed
    process.completed = True

    process.remaining_time = 0

    process.set_state("TERMINATED")

    process.turnaround_time = (
        time - process.arrival_time
    )

    completed.append(process)

    context_switches += 1


    print(
        f"P{process.pid} completed."
    )

    print(
        f"CPU Time: {time}"
    )


# -------------------------
# Results
# -------------------------

print()
print("===== PRIORITY SCHEDULING COMPLETE =====")

print(
    f"Total Time: {time}"
)

print(
    f"Context Switches: {context_switches}"
)


print()
print("===== PROCESS RESULTS =====")


for process in processes:

    print(
        f"P{process.pid} | "
        f"Priority: {process.priority} | "
        f"State: {process.state} | "
        f"Turnaround: "
        f"{process.turnaround_time}"
      )
