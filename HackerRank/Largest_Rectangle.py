def largestRectangle(h):
    stack = []
    result = 0
    for idx, height in enumerate(h):
        if stack == []:
            stack.append([idx, height])
        else:
            width = idx
            while stack != [] and stack[-1][1] > height:
                value = stack.pop()
                width = value[0]
                size = value[1] * (idx - value[0])
                if result < size:
                    result = size
            stack.append([width, height])
    for value in stack:
        size = value[1] * (len(h) - value[0])
        if result < size:
            result = size
    return result
