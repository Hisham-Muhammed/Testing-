from pcb import PCB
from ready_queue import ReadyQueue


class ProcessManager:

    def __init__(self):

        self.processes = []

        self.ready_queue = ReadyQueue()

        self.next_pid = 1


    def create_process(
        self,
        program,
        priority=1,
        arrival_time=0
    ):

        process = PCB(
            self.next_pid,
            program,
            priority,
            arrival_time
        )

        process.set_state("READY")

        self.processes.append(process)

        self.ready_queue.enqueue(process)

        self.next_pid += 1

        print(
            f"Process P{process.pid} created"
        )

        return process


    def get_process(self, pid):

        for process in self.processes:

            if process.pid == pid:

                return process

        return None


    def show_processes(self):

        print("\n===== PROCESS TABLE =====")

        for process in self.processes:

            print(
                f"P{process.pid} | "
                f"State: {process.state} | "
                f"Priority: {process.priority} | "
                f"PC: {process.pc}"
            )

        print("=========================")


    def show_ready_queue(self):

        self.ready_queue.show()
