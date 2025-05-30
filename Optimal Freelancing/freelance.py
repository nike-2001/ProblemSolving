def optimalFreelancing(jobs):
    max_days = 7
    max_profit = 0
    jobs.sort(key = lambda k: k["payment"], reverse = True)
    days = [False] * (max_days + 1)

    for job in jobs:
        deadline = min(job["deadline"], max_days)
        for i in range(deadline, 0, -1):
            if days[i] == False:
                days[i] = True
                max_profit += job["payment"]
                break

    return max_profit
