from cpu import CPU
from memory import Memory
from process_manager import ProcessManager
from performance import PerformanceAnalyzer


print("===== PERFORMANCE ANALYSIS TEST =====")


process_manager = ProcessManager()


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

time = 0
context_switches = 0


for process in processes:

    process.set_state("RUNNING")

    memory = Memory()

    cpu = CPU(memory)

    for address, instruction in enumerate(
        process.program
    ):

        memory.write_program(
            address,
            instruction
        )

    start_time = time

    process.response_time = (
        start_time - process.arrival_time
    )

    process.burst_time = 0

    while not cpu.halted:

        cpu.step()

        time += 1

        process.burst_time += 1

    process.pc = cpu.PC

    process.completed = True

    process.set_state("TERMINATED")

    process.turnaround_time = (
        time - process.arrival_time
    )

    process.waiting_time = (
        process.turnaround_time
        - process.burst_time
    )

    context_switches += 1


analyzer = PerformanceAnalyzer(
    processes,
    time,
    context_switches
)

analyzer.show_results()
