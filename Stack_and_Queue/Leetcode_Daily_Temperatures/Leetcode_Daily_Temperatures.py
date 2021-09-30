##### My code #####
##### Runtime 1340ms, Memory 35MB #####

def dailyTemperatures(temperatures):
    rlt = [0]*len(temperatures)
    dic = {}
    Stack = []

    for idx, val in enumerate(temperatures):
        dic[idx] = val

    for idx, temp in dic.items():
        while Stack and dic.get(Stack[-1]) < temp:
            rlt[Stack[-1]] = idx - Stack[-1]
            Stack.pop()
        Stack.append(idx)

    return rlt