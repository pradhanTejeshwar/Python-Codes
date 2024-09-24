def find_max(values):
    maximum = values[0]
    for i in values:
        if maximum < i:
            maximum=i
    
    return maximum