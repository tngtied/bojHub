def solution(elements):
    numset = set()
    numset.add(sum(elements))
    for i in range(len(elements)):
        j = i
        while True:
            # print(f"{i} : {j}")
            j += 1
            if j >= len(elements):
                j -= len(elements)
            if j > i:
                numset.add(sum(elements[i : j]))
            else:
                numset.add(sum(elements[0 : j]) + sum(elements[i:]))
            if j == i:
                break
                
    return len(numset)