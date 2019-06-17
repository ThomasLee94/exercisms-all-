def distance(strand_a: str, strand_b: str) -> int:

    if len(strand_a) != len(strand_b):
        raise ValueError("Differing strand lengths")

    count = 0

    for i in range(0, len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count += 1
    return count

    
