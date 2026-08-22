from process_manager import ProcessManager
from integrated_scheduler import IntegratedScheduler


def create_processes():

    manager = ProcessManager()

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

    p1 = manager.create_process(
        program1,
        priority=2,
        arrival_time=0
    )

    p2 = manager.create_process(
        program2,
        priority=1,
        arrival_time=0
    )

    p3 = manager.create_process(
        program3,
        priority=3,
        arrival_time=0
    )

    return [p1, p2, p3]


print("===== INTEGRATED SCHEDULER TEST =====")

print("\n1. FCFS")
processes = create_processes()
scheduler = IntegratedScheduler(processes)
scheduler.run_fcfs()


print("\n2. ROUND ROBIN")
processes = create_processes()
scheduler = IntegratedScheduler(processes)
scheduler.run_round_robin(quantum=2)


print("\n3. PRIORITY")
processes = create_processes()
scheduler = IntegratedScheduler(processes)
scheduler.run_priority()


print("\n===== INTEGRATED TEST COMPLETE =====")
