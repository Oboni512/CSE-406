# -*- coding: utf-8 -*-
"""Mid_21201088.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e4-l3xL79eNvvHI3H_D7jdAW9kr8-nJY
"""

def elevator_disk_scheduling(requests, head):
    # Sort the request sequence
    requests.sort()

    # Find the position to split the requests (left and right of the current head)
    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]

    # Calculate total seek operations
    total_seek = 0
    seek_sequence = []

    # Move the head towards the right first
    for r in right:
        seek_sequence.append(r)
        total_seek += abs(head - r)
        head = r

    # Now move the head towards the left
    for r in reversed(left):
        seek_sequence.append(r)
        total_seek += abs(head - r)
        head = r

    return total_seek, seek_sequence


# Given input
requests = [137, 240, 179, 75, 118, 29, 15, 51]
head = 55

# Apply Elevator (SCAN) Disk Scheduling
total_seek, seek_sequence = elevator_disk_scheduling(requests, head)

print(f"Total Seek Operations: {total_seek}")
print(f"Seek Sequence: {seek_sequence}")

from collections import deque

def round_robin(process_list, time_quanta):
    time = 0
    gantt = []
    completed = {}
    queue = deque()
    backup = {}
    response_time = {}

    #store initial data

    for process in process_list:
        pid = process[2]
        burst_time = process[1]
        arrival_time = process[0]
        backup[pid] = [arrival_time, burst_time]

        #Initialize Remaining Process List

    remaining_process = process_list[:]
#main loop
    while remaining_process or queue:
      # Move Arrived Processes to Queue
        for process in remaining_process[:]:
            if process[0] <= time:
                queue.append(process)
                remaining_process.remove(process)

        if not queue:
            gantt.append(("Idle", time, time + 1))
            time += 1
            continue

        process = queue.popleft()
        pid = process[2]
        arrival_time = process[0]

        if pid not in response_time:
            response_time[pid] = time - arrival_time  # First time it's scheduled

        execution_time = min(time_quanta, process[1])
        process[1] -= execution_time
        gantt.append((pid, time, time + execution_time))
        time += execution_time

        for p in remaining_process[:]:
            if p[0] <= time:
                queue.append(p)
                remaining_process.remove(p)

        if process[1] == 0:
            burst_time = backup[pid][1]
            ct = time
            tat = ct - arrival_time
            wt = tat - burst_time
            rt = response_time[pid]
            completed[pid] = [pid, arrival_time, burst_time, ct, tat, wt, rt]
        else:
            queue.append(process)

    return {
        'gantt': gantt,
        'completed': completed
    }


def print_table(completed):
    print("\nProcess\tAT\tBT\tCT\tTAT\tWT\tRT")
    total_tat = total_wt = total_rt = 0
    for pid in sorted(completed):
        data = completed[pid]
        print(f'{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[4]}\t{data[5]}\t{data[6]}')
        total_tat += data[4]
        total_wt += data[5]
        total_rt += data[6]

    n = len(completed)
    print(f"\nAverage TAT: {total_tat / n:.2f}")
    print(f"Average WT : {total_wt / n:.2f}")
    print(f"Average RT : {total_rt / n:.2f}")


def print_gantt_chart(gantt):
    print("\nGantt Chart:")
    for pid, start, end in gantt:
        print(f"| {pid} ({start}-{end}) ", end="")
    print("|")


if __name__ == "__main__":
    # process = [arrival, burst, pid]
    process_list = [
        [0, 7, 'P1'],
        [1, 4, 'P2'],
        [2, 15, 'P3'],
        [3, 11, 'P4'],
        [4, 20, 'P5'],
        [4, 9, 'P6'],
    ]

    time_quanta = 5

    res = round_robin(process_list, time_quanta)

    print_gantt_chart(res['gantt'])
    print_table(res['completed'])