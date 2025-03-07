def manage_stage_changes(changes):
    cancelled_stack = []
    schedule = []
    for i in range(0, len(changes)):
        if changes[i] == "Cancel":
            cancelled_stack.append(changes[i - 1])
            schedule.pop()
        elif changes[i] == "Reschedule":
            schedule.append(cancelled_stack.pop().split(" ")[-1])
        else:
            schedule.append(changes[i].split(" ")[-1])

    return schedule


print(
    manage_stage_changes(
        ["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]
    )
)
print(
    manage_stage_changes(
        ["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]
    )
)
print(
    manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])
)
