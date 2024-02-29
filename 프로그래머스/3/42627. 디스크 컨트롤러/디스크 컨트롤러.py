import heapq
def solution(jobs):
    jobs.sort(key = lambda x : x[0])
    answer = 0
    hq = []
    job_index = 0
    cur_time = 0
    jobs_done = 0
    i = 0
    while (jobs_done < len(jobs)):
        print("cur_time %d jobs_done %d" % (cur_time, jobs_done))
        while (job_index < len(jobs) and jobs[job_index][0] <= cur_time):
            heapq.heappush(hq, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        if (len(hq)):
            el =  heapq.heappop(hq)
            answer += el[0] + cur_time - el[1]
            cur_time += el[0]
            jobs_done += 1
        else:
            cur_time = jobs[job_index][0]
    return answer // len(jobs)