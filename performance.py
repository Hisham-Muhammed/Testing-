class PerformanceAnalyzer:

    def __init__(self, processes, total_time, context_switches):
        self.processes = processes
        self.total_time = total_time
        self.context_switches = context_switches

    def calculate_waiting_time(self, process):
        return (
            process.turnaround_time
            - process.burst_time
        )

    def calculate_cpu_utilization(self):
        if self.total_time == 0:
            return 0

        total_burst_time = sum(
            process.burst_time
            for process in self.processes
        )

        return (
            total_burst_time
            / self.total_time
        ) * 100

    def show_results(self):

        print("\n===== PERFORMANCE ANALYSIS =====")

        total_waiting = 0
        total_turnaround = 0
        total_response = 0

        for process in self.processes:

            waiting_time = (
                self.calculate_waiting_time(process)
            )

            turnaround_time = (
                process.turnaround_time
            )

            response_time = (
                process.response_time
            )

            total_waiting += waiting_time
            total_turnaround += turnaround_time
            total_response += response_time

            print(
                f"\nP{process.pid}"
            )

            print(
                f"Waiting Time    : {waiting_time}"
            )

            print(
                f"Turnaround Time : {turnaround_time}"
            )

            print(
                f"Response Time   : {response_time}"
            )

        count = len(self.processes)

        if count > 0:

            print(
                "\nAverage Waiting Time    : "
                f"{total_waiting / count:.2f}"
            )

            print(
                "Average Turnaround Time : "
                f"{total_turnaround / count:.2f}"
            )

            print(
                "Average Response Time   : "
                f"{total_response / count:.2f}"
            )

        print(
            f"Context Switches        : "
            f"{self.context_switches}"
        )

        print(
            "CPU Utilization         : "
            f"{self.calculate_cpu_utilization():.2f}%"
        )

        print(
            "================================"
  )
