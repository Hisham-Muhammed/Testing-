from cpu import CPU
from memory import Memory
from process_manager import ProcessManager


print("===== ROUND ROBIN SCHEDULING TEST =====")


# Create process manager
process_manager = ProcessManager()


# -------------------------
# Programs
# -------------------------

program1 = [
    ("MOV", 0, 10),
    ("INC", 0),
    ("INC", 0),
    ("INC", 0),
    ("HALT",)
]


program2 = [
    ("MOV", 1, 20),
    ("INC", 1),
    ("INC", 1),
    ("INC", 1),
    ("HALT",)
]


program3 = [
    ("MOV", 2, 30),
    ("INC", 2),
    ("INC", 2),
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


processes = [p1, p2, p3]


# -------------------------
# Time Quantum
# -------------------------

time_quantum = 2

time = 0

context_switches = 0


# -------------------------
# CPU execution
# -------------------------

for process in processes:

    process.set_state("READY")


while True:

    all_completed = True

    for process in processes:

        if process.completed:

            continue

        all_completed = False

        print()
        print(
            f"===== Running P{process.pid} ====="
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


        # Restore program counter
        cpu.PC = process.pc


        # Run for time quantum
        instructions_executed = 0

        while (
            not cpu.halted
            and instructions_executed < time_quantum
        ):

            cpu.step()

            instructions_executed += 1

            time += 1


        # Save CPU state
        process.pc = cpu.PC


        # Check completion
        if cpu.halted:

            process.completed = True

            process.remaining_time = 0

            process.set_state("TERMINATED")

            process.turnaround_time = (
                time - process.arrival_time
            )

            print(
                f"P{process.pid} COMPLETED"
            )

        else:

            process.set_state("READY")

            process.remaining_time -= (
                instructions_executed
            )

            print(
                f"P{process.pid} TIME SLICE OVER"
            )

            print(
                f"Returning to Ready Queue: "
                f"P{process.pid}"
            )


        context_switches += 1


    if all_completed:

        break


print()
print("===== ROUND ROBIN COMPLETE =====")

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
        f"State: {process.state} | "
        f"PC: {process.pc} | "
        f"Turnaround: "
        f"{process.turnaround_time}"
          )
