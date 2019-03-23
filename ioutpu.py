def read_tagged(file):
    result = []
    with open(file,encoding='utf8') as file:
        buffer = []
        for line in file:
            if len(line) < 2:
                result.append(buffer)
                buffer = []
            else:
                buffer.append((line[0],line[1]))
    return result
