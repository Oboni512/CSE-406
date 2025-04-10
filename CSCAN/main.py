def cscan(requests, head, disk_size=200):
    requests.sort()
    seek_sequence = []
    scount = 0
    left = []
    right = []

    for request in requests:
        if request < head:
            left.append(request)
        else:
            right.append(request)

    # First, service requests to the right of head
    for r in right:
        seek_sequence.append(r)
        scount += abs(head - r)
        head = r

    # Go to the end of the disk if not already there
    if head != disk_size - 1:
        scount += abs(head - (disk_size - 1))
        head = disk_size - 1
        seek_sequence.append(head)

    # Jump to beginning (circular move)
    scount += head  # from end to 0
    head = 0
    seek_sequence.append(head)

    # Then, service the left side
    for l in left:
        seek_sequence.append(l)
        scount += abs(head - l)
        head = l

    return scount, seek_sequence

# Example usage
requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
head = 53
total_seek, sequence = cscan(requests, head)

print("Total Seek Operations:", total_seek)
print("Seek Sequence:", sequence)
