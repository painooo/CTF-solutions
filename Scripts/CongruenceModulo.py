def CongruenceModulo(n, r):
    # Define an n as the modulus
    # Define r as how many multiples it'll go
    # Returns a list of different buckets [([neg], [pos]), (neg, pos)]
    bucketIndexes = range(0, n)
    buckets = []
    for bI in bucketIndexes:
        pos = []
        neg = []
        for mult in range(1, r+1):
            pos.append((n * mult)+bI)
            neg.append((n * mult * -1) + bI)
        bucket = (neg, pos)
        buckets.append(bucket)
    return buckets

