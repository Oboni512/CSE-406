def priority_preemptive(processes):
    time = 0
    completed = 0
    n = len(processes)

    gantt_chart = []
    proc_info = {p[0]: {"priority": p[1], "arrival": p[2], "burst": p[3], "remaining": p[3],
                        "ct": 0, "tat": 0, "wt": 0, "rt": -1} for p in processes}

    while completed < n:
        # Find process with highest priority (max value) that has arrived
        min_priority_proc = None
        for pid, info in proc_info.items():
            if info["arrival"] <= time and info["remaining"] > 0:
                if min_priority_proc is None or info["priority"] > proc_info[min_priority_proc]["priority"]:
                    min_priority_proc = pid

        if min_priority_proc is None:
            gantt_chart.append("Idle")
            time += 1
            continue

        # Record first response time (RT) when the process starts execution for the first time
        if proc_info[min_priority_proc]["rt"] == -1:
            proc_info[min_priority_proc]["rt"] = time - proc_info[min_priority_proc]["arrival"]

        # Execute selected process for 1 unit of time
        gantt_chart.append(min_priority_proc)
        proc_info[min_priority_proc]["remaining"] -= 1
        time += 1

        # If process is completed, calculate completion time
        if proc_info[min_priority_proc]["remaining"] == 0:
            proc_info[min_priority_proc]["ct"] = time
            proc_info[min_priority_proc]["tat"] = proc_info[min_priority_proc]["ct"] - proc_info[min_priority_proc][
                "arrival"]
            proc_info[min_priority_proc]["wt"] = proc_info[min_priority_proc]["tat"] - proc_info[min_priority_proc][
                "burst"]
            completed += 1

    return {"gantt_chart": gantt_chart, "completed": proc_info}


def print_table(completed):
    print("\nProcess\tPriority\tArrival\tBurst\tCT\tTAT\tWT\tRT")
    for pid, values in sorted(completed.items()):
        print(
            f"{pid}\t{values['priority']}\t\t{values['arrival']}\t{values['burst']}\t{values['ct']}\t{values['tat']}\t{values['wt']}\t{values['rt']}")


if __name__ == "__main__":
    # Example: [(PID, Priority, Arrival Time, Burst Time)]
    process_list = [(1, 10, 0, 5), (2, 20, 1, 4), (3, 30, 2, 2), (4, 40, 4, 1)]

    result = priority_preemptive(process_list)

    print("\nGantt Chart:", result["gantt_chart"])
    print_table(result["completed"])
