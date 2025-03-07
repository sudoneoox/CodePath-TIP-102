def merge_schedules(schedule_1, schedule_2):
    stack = []
    i, j = 0, 0
    while i < len(schedule_1) and j < len(schedule_2):
        stack.append(schedule_1[i])
        stack.append(schedule_2[j])
        i += 1
        j += 1

    while i < len(schedule_1):
        stack.append(schedule_1[i])
        i += 1

    while j < len(schedule_2):
        stack.append(schedule_2[j])
        j += 1

    return "".join(stack)


print(merge_schedules("abc", "pqr"))
print(merge_schedules("ab", "pqrs"))
print(merge_schedules("abcd", "pq"))
