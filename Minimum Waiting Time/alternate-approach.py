def minimumWaitingTime(queries):
    queries.sort()

    min_wait_time = 0
    for num in range(len(queries)):
        rem_queries = len(queries) - (num + 1)
        min_wait_time += queries[num] * rem_queries

    return min_wait_time
