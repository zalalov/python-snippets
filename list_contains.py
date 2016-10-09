def contains(needed, seq):
    """ Check if list contains needed """
    index = [i for i in range(len(seq)) if seq[i:i + len(needed)] == needed]
    return bool(index)

print contains([4], [1,2,3,4,5])

