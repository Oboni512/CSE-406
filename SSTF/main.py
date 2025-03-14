def calculateDifference(queue, head):
    return [abs(track - head) for track in queue]


# Function to find the track with the minimum distance from the current head
def findMin(diff, accessed):
    minimum = float('inf')
    index = -1

    for i in range(len(diff)):
        if not accessed[i] and diff[i] < minimum:
            minimum = diff[i]
            index = i
    return index


# Shortest Seek Time First (SSTF) Disk Scheduling Algorithm
def shortestSeekTimeFirst(requests, head):
    if len(requests) == 0:
        print("No requests to process.")
        return

    l = len(requests)
    accessed = [False] * l
    seek_count = 0
    seek_sequence = []

    # Process each request
    for _ in range(l):
        seek_sequence.append(head)
        diff = calculateDifference(requests, head)
        index = findMin(diff, accessed)

        accessed[index] = True
        seek_count += diff[index]
        head = requests[index]

    seek_sequence.append(head)

    # Output results
    print(f"Total number of seek operations = {seek_count}")
    print("Seek Sequence is:", ' -> '.join(map(str, seek_sequence)))


# Driver code
if __name__ == "__main__":
    proc = [176, 79, 34, 60, 92, 11, 41, 114]
    initial_head = 50
    shortestSeekTimeFirst(proc, initial_head)
