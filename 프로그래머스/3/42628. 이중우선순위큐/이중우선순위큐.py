import heapq
def solution(operations):
    minq = []
    maxq = []
    maxdict = {}
    mindict = {}
    for o in operations:
        print("minq: %s, maxq %s\n----------" % (str(minq), str(maxq)))
        oper, num = o.split()

        if (oper == "I"):
            heapq.heappush(minq, int(num))
            heapq.heappush(maxq, -int(num))
        else:
            if int(num) == 1 and len(maxq):
                el = heapq.heappop(maxq)
                if (-el not in mindict):
                    mindict[-el] = 1
                else:
                    mindict[-el] += 1
                print("> mindict[%d] %d" % (-el, mindict[-el]))
            elif (int(num) == -1 and len(minq)):
                el = heapq.heappop(minq)
                if (el not in maxdict):
                    maxdict[el] = 1
                else:
                    maxdict[el] += 1
                print("> el %d maxdict[el] %d" % (el, maxdict[el] ))
        if (len(maxq)):
            print(">> -maxq[0] %d" % -maxq[0])
            if  (-maxq[0] in maxdict):
                print(">>> maxdict[-maxq[0]] %d" % (maxdict[-maxq[0]]))
        if (len(minq)):
            print(">> minq[0] %d" % minq[0])
            if  (minq[0] in mindict):
                print(">>> mindict[minq[0]] %d" % (mindict[minq[0]]))
        while (len(maxq) and -maxq[0] in maxdict and maxdict[-maxq[0]] > 0):
            maxdict[-maxq[0]] -= 1
            heapq.heappop(maxq)
        while (len(minq) and minq[0] in mindict and mindict[minq[0]] > 0):
            mindict[minq[0]] -= 1
            heapq.heappop(minq)
    if (len(maxq) and len(minq)):
        return [-maxq[0], minq[0]]
    else:
        return [0, 0]