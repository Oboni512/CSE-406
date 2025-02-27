from collections import deque


class Process:
    def __init__(self, no, arrival, burst):
        self.no = no
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = 0
        self.turnAround = 0
        self.waiting = 0
        self.response = -1  # Response time, -1 means not set yet


def round_robin(processes, quantum):
    time = 0
    completed = 0
    n = len(processes)

    queue = deque()
    in_queue = [False] * n
    first_response = [False] * n

    queue.append(0)
    in_queue[0] = True

    while completed < n:
        i = queue.popleft()

        # Set response time for first execution
        if not first_response[i]:
            processes[i].response = time - processes[i].arrival
            first_response[i] = True

        if processes[i].remaining > quantum:
            time += quantum
            processes[i].remaining -= quantum
        else:
            time += processes[i].remaining
            processes[i].remaining = 0
            processes[i].completion = time
            processes[i].turnAround = processes[i].completion - processes[i].arrival
            processes[i].waiting = processes[i].turnAround - processes[i].burst
            completed += 1

        # Add new processes that have arrived by the current time
        for j in range(n):
            if processes[j].arrival <= time and processes[j].remaining > 0 and not in_queue[j]:
                queue.append(j)
                in_queue[j] = True

        # Re-add the current process if it's not yet completed
        if processes[i].remaining > 0:
            queue.append(i)


def print_processes(processes):
    print("No\tAT\tBT\tCT\tTAT\tWT\tRT")
    for p in processes:
        print(f"P{p.no}\t{p.arrival}\t{p.burst}\t{p.completion}\t{p.turnAround}\t{p.waiting}\t{p.response}")


# Define processes
processes = [Process(1, 0, 5),
             Process(2, 1, 4),
             Process(3, 2, 2),
             Process(4, 4, 1)]
quantum = 2

round_robin(processes, quantum)
print_processes(processes)
