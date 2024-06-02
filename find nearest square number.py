def nearest_sq(n):
    result = int(n ** 0.5)
    if n ** 0.5 < result + 1:
        return int((n + 1) ** 0.5) ** 2
    else:
        return int(n ** 0.5) ** 2