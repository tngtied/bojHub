def solution(progresses, speeds):
    def duration(done_work, speed):
        left_work = 100 - done_work
        if (left_work % speed != 0):
            return left_work //speed + 1
        else:
            return left_work // speed
    ptr = 0
    count = 0
    answer = []
    while (ptr < len(progresses)):
        core_dur = duration(progresses[ptr], speeds[ptr])
        print("ptr %d duration %d" % (ptr, duration(progresses[ptr], speeds[ptr])))
        ptr += 1
        count += 1
        while (ptr < len(progresses) and core_dur >= duration(progresses[ptr], speeds[ptr])):
            print("ptr %d duration %d" % (ptr, duration(progresses[ptr], speeds[ptr])))
            count += 1
            ptr += 1
        answer.append(count)
        count = 0

    return answer