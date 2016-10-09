def contains(needed, seq):
    """ Check if list contains needed """
    if not isinstance(needed, (list, tuple)) or not isinstance(seq, (list, tuple)):
        raise Exception("Arguments should be lists of tuples")

    index = [i for i in range(len(seq)) if seq[i:i + len(needed)] == needed]
    return bool(index)

print contains([4], [1,2,3,4,5])
print contains(None, None)
