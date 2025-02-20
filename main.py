

# Get the number of processes
n = int(input("Enter number of processes: "))

processes = []

# Collect process details
for i in range(n):
    pid = input(f"Enter Process ID for Process {i + 1}: ")
    at = int(input(f"Enter Arrival Time for Process {pid}: "))
    bt = int(input(f"Enter Burst Time for Process {pid}: "))
    processes.append([pid, at, bt])

# Sort processes by Arrival Time first, then Burst Time for fair scheduling
processes.sort(key=lambda x: (x[1], x[2]))

# Initialize variables for scheduling
current_time = 0
completed_processes = []  # Stores completed process data

# Process execution logic
while processes:
    # Get ready processes that have already arrived
    ready_queue = [p for p in processes if p[1] <= current_time]

    # If no process is ready, increment current time
    if not ready_queue:
        current_time += 1
        continue

    # Sort ready processes by shortest burst time
    ready_queue.sort(key=lambda x: x[2])
    process = ready_queue[0]  # Select the process with shortest burst time

    # Calculate Completion Time (CT), Turnaround Time (TAT), Waiting Time (WT)
    ct = current_time + process[2]  # Completion Time
    tat = ct - process[1]  # Turnaround Time = CT - Arrival Time
    wt = tat - process[2]  # Waiting Time = TAT - Burst Time

    # Store process result
    completed_processes.append([process[0], process[1], process[2], ct, tat, wt])

    # Update current time and remove the selected process
    current_time = ct
    processes.remove(process)

# Display results in a table format
print("\nP  | AT | BT | CT | TAT | WT")
print("-" * 40)
for p in completed_processes:
    print(f"{p[0]} | {p[1]:2d} | {p[2]:2d} | {p[3]:2d} | {p[4]:2d} | {p[5]:2d}")
