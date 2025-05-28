def minimumWaitingTime(queries):
    queries.sort()
    min_wait_time, output = 0, 0
    for num in range(1, len(queries)):
        output += queries[num-1]
        min_wait_time += output


    return min_wait_time
