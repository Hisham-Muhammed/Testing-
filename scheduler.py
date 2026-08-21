from ready_queue import ReadyQueue


class Scheduler:

    def __init__(self):

        self.ready_queue = ReadyQueue()

        self.current_process = None

        self.context_switches = 0

        self.time = 0


    def add_process(self, process):

        process.set_state("READY")

        self.ready_queue.enqueue(process)


    def fcfs(self):

        if self.current_process is not None:
            return self.current_process

        process = self.ready_queue.dequeue()

        if process is None:
            return None

        self.context_switches += 1

        self.current_process = process

        process.set_state("RUNNING")

        if process.response_time == -1:

            process.response_time = (
                self.time - process.arrival_time
            )

        print(
            f"FCFS: Running P{process.pid}"
        )

        return process


    def finish_current_process(self):

        if self.current_process is None:
            return

        process = self.current_process

        process.set_state("TERMINATED")

        process.completed = True

        process.turnaround_time = (
            self.time - process.arrival_time
        )

        self.current_process = None


    def show_status(self):

        print("\n===== SCHEDULER =====")

        if self.current_process is None:

            print("Current Process: None")

        else:

            print(
                f"Current Process: "
                f"P{self.current_process.pid}"
            )

        print(
            f"Time: {self.time}"
        )

        print(
            f"Context Switches: "
            f"{self.context_switches}"
        )

        self.ready_queue.show()

        print("=====================")
