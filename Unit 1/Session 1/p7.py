def count_less_than(race_times, threshold):
    i = 0
    for time in race_times:
        if time >= threshold:
            i += 1
    return i


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print((count_less_than(race_times, threshold)))
