cpdef int intersection(tuple s1, tuple s2):
    return set(s1) & set(s2) != set()
