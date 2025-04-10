def scan_disk_scheduling(request_sequence, initial_head):
    request_sequence.sort()
    left = [r for r in request_sequence if r < initial_head][::-1]
    right = [r for r in request_sequence if r >= initial_head]

    sequence = right + left
    total_seek_time = 0
    current_head = initial_head

    for req in sequence:
        total_seek_time += abs(req - current_head)
        current_head = req

    return total_seek_time, sequence

def take_input():
    head = int(input("Enter initial head position: "))
    req_sequences = [int(input(f'Enter request {i+1}: ')) for i in range(int(input("Enter number of requests: ")))]
    return req_sequences, head

def print_sequence(sequences):
    print(" ---> ".join(map(str, sequences)))

if __name__ == "__main__":
    req_sequences, head = take_input()
    total_seek_time, sequence = scan_disk_scheduling(req_sequences, head)

    print(f"Total Seek Time: {total_seek_time}")
    print("Seek Sequence: ", end="")
    print_sequence(sequence)

