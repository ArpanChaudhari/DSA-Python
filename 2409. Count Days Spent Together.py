def countDaysTogether(
    arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
) -> int:
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Convert MM-DD into a day number
    def get_days(date):
        month, day = map(int, date.split("-"))

        total = sum(day_in_month[: month - 1])

        return total + day

    arriveAlice = get_days(arriveAlice)
    leaveAlice = get_days(leaveAlice)
    arriveBob = get_days(arriveBob)
    leaveBob = get_days(leaveBob)

    # Find overlap boundaries
    start = max(arriveAlice, arriveBob)
    end = min(leaveAlice, leaveBob)

    # No Overlap
    if start > end:
        return 0

    # Count both the starting and ending days
    return end - start + 1


arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))  