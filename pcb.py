class PCB:

    def __init__(
        self,
        pid,
        program,
        priority=1,
        arrival_time=0
    ):

        self.pid = pid

        self.program = program

        self.priority = priority

        self.arrival_time = arrival_time

        self.pc = 0

        self.state = "NEW"

        self.burst_time = len(program)

        self.remaining_time = self.burst_time

        self.waiting_time = 0

        self.turnaround_time = 0

        self.response_time = -1

        self.completed = False


    def set_state(self, state):

        self.state = state


    def show(self):

        print(
            f"PID: {self.pid}"
        )

        print(
            f"State: {self.state}"
        )

        print(
            f"Priority: {self.priority}"
        )

        print(
            f"PC: {self.pc}"
        )

        print(
            f"Arrival Time: {self.arrival_time}"
        )

        print(
            f"Burst Time: {self.burst_time}"
        )

        print(
            f"Remaining Time: {self.remaining_time}"
        )

        print(
            f"Waiting Time: {self.waiting_time}"
        )

        print(
            f"Turnaround Time: {self.turnaround_time}"
        )

        print(
            f"Response Time: {self.response_time}"
        )

        print("---------------------")
