data = []

# Get number of processes
process_no = int(input("Enter the number of processes: "))

# Input process details
for i in range(process_no):
    processID = input("Enter Process ID: ")
    arrival = int(input("Enter Arrival Time: "))
    burst = int(input("Enter Burst Time: "))

    data.append({
        "process": processID,
        "arrival": arrival,
        "burst": burst
    })

# Function to extract the arrival time
def get_arrival_time(process):
    return process['arrival']

# Sorting by arrival time (FCFS Scheduling)
data.sort(key=get_arrival_time)

# Initialize CPU execution time
cpu_time = 0

# Calculate Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT)
for process in data:
    if cpu_time < process['arrival']:
        cpu_time = process['arrival']

    # Calculate CT, TAT, and WT
    process['CT'] = cpu_time + process['burst']
    process['TAT'] = process['CT'] - process['arrival']
    process['WT'] = process['TAT'] - process['burst']

    # Update CPU time
    cpu_time = process['CT']

# **Display Results in Simple Table Format**
print("\n P |  A |  B |  CT |  TA |  WT ")
for p in data:
    print(f"{p['process']}  | {p['arrival']}  | {p['burst']}  | {p['CT']}  | {p['TAT']}  | {p['WT']}")


