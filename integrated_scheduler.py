from cpu import CPU
from memory import Memory


class IntegratedScheduler:

    def __init__(self, processes):

        self.processes = processes

        self.time = 0

        self.context_switches = 0

        self.current_process = None


    def run_process(self, process, quantum=None):

        memory = Memory()

        cpu = CPU(memory)

        # Load program into memory
        for address, instruction in enumerate(
            process.program
        ):

            memory.write_program(
                address,
                instruction
            )

        # Restore program counter
        cpu.PC = process.pc

        process.set_state("RUNNING")

        # First time CPU response
        if process.response_time == -1:

            process.response_time = (
                self.time
                - process.arrival_time
            )

        executed = 0

        while not cpu.halted:

            cpu.step()

            executed += 1

            self.time += 1

            process.burst_time += 1

            process.pc = cpu.PC

            # Round Robin time quantum
            if (
                quantum is not None
                and executed >= quantum
            ):

                break


        # Process completed
        if cpu.halted:

            process.completed = True

            process.remaining_time = 0

            process.set_state("TERMINATED")

            process.turnaround_time = (
                self.time
                - process.arrival_time
            )

            return True


        # Time slice finished
        process.set_state("READY")

        return False


    # =========================
    # FCFS
    # =========================

    def run_fcfs(self):

        print("\n===== FCFS SCHEDULING =====")

        for process in self.processes:

            if process.completed:

                continue

            print(
                f"\nRunning P{process.pid}"
            )

            self.current_process = process

            self.context_switches += 1

            self.run_process(process)

        self.current_process = None

        self.show_results()


    # =========================
    # PRIORITY
    # =========================

    def run_priority(self):

        print(
            "\n===== PRIORITY SCHEDULING ====="
        )

        remaining = [
            process
            for process in self.processes
            if not process.completed
        ]

        while remaining:

            # Smaller number = higher priority
            process = min(
                remaining,
                key=lambda p: p.priority
            )

            print(
                f"\nRunning P{process.pid} "
                f"(Priority {process.priority})"
            )

            self.current_process = process

            self.context_switches += 1

            self.run_process(process)

            remaining.remove(process)

        self.current_process = None

        self.show_results()


    # =========================
    # ROUND ROBIN
    # =========================

    def run_round_robin(self, quantum=2):

        print(
            "\n===== ROUND ROBIN SCHEDULING ====="
        )

        while True:

            active = [
                process
                for process in self.processes
                if not process.completed
            ]

            if not active:

                break

            for process in active:

                if process.completed:

                    continue

                print(
                    f"\nRunning P{process.pid}"
                )

                self.current_process = process

                self.context_switches += 1

                self.run_process(
                    process,
                    quantum
                )

        self.current_process = None

        self.show_results()


    # =========================
    # RESULTS
    # =========================

    def show_results(self):

        print(
            "\n===== SCHEDULING RESULTS ====="
        )

        print(
            f"Total CPU Time: {self.time}"
        )

        print(
            f"Context Switches: "
            f"{self.context_switches}"
        )

        print("\nProcess Results:")

        for process in self.processes:

            waiting_time = (
                process.turnaround_time
                - process.burst_time
            )

            print(
                f"P{process.pid} | "
                f"State: {process.state} | "
                f"Priority: {process.priority} | "
                f"Waiting: {waiting_time} | "
                f"Turnaround: "
                f"{process.turnaround_time} | "
                f"Response: "
                f"{process.response_time}"
          )
