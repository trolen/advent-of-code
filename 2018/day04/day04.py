#! /usr/bin/env python3

from datetime import datetime

def read_data(filename):
    with open(filename, 'rt') as file:
        return sorted([line.strip() for line in file.readlines()])


def tabulate_sleep_times(data):
    results = {}
    guardOnDuty = None
    minuteAsleep = None
    for line in data:
        (dtStr, actionStr) = line.split(']')
        dtStr = dtStr[1:]
        actionStr = actionStr.strip()
        terms = actionStr.split(' ')
        if 'shift' in terms:        # begins shift
            guardOnDuty = int(terms[1][1:])
        elif 'asleep' in terms:     # falls asleep
            dtObj = datetime.strptime(dtStr, '%Y-%m-%d %H:%M')
            minuteAsleep = dtObj.minute
            if guardOnDuty not in results:
                minutes = [0] * 60
                results[guardOnDuty] = minutes
        elif 'wakes' in terms:      # wakes up
            dtObj = datetime.strptime(dtStr, '%Y-%m-%d %H:%M')
            minuteAwake = dtObj.minute
            for i in range(minuteAsleep, minuteAwake):
                results[guardOnDuty][i] += 1
    return results


def guard_asleep_most(sleep_times):
    guardAsleepMost = None
    guardSleepTime = 0
    for guard in sleep_times:
        total = sum(sleep_times[guard])
        if total > guardSleepTime:
            guardSleepTime = total
            guardAsleepMost = guard
    return guardAsleepMost


def minute_most_asleep(guard, sleep_times):
    minuteMostAsleep = 0
    minutesAsleep = 0
    minuteTotals = sleep_times[guard]
    for i in range(0, 60):
        if minuteTotals[i] > minutesAsleep:
            minutesAsleep = minuteTotals[i]
            minuteMostAsleep = i
    return minuteMostAsleep


def guard_most_asleep_on_minute(sleep_times):
    guardMostAsleep = None
    minuteMostAsleep = None
    minutesAsleep = 0
    for guard in sleep_times:
        minutes = sleep_times[guard]
        for i in range(0, 60):
            if minutes[i] > minutesAsleep:
                minutesAsleep = minutes[i]
                minuteMostAsleep = i
                guardMostAsleep = guard
    return (guardMostAsleep, minuteMostAsleep)


if __name__ == '__main__':
    data = read_data('input.txt')
    sleep_times = tabulate_sleep_times(data)
    guard = guard_asleep_most(sleep_times)
    minute = minute_most_asleep(guard, sleep_times)
    print('Product ({0} x {1}): {2}'.format(guard, minute, guard * minute))
    (guard, minute) = guard_most_asleep_on_minute(sleep_times)
    print('Product ({0} x {1}): {2}'.format(guard, minute, guard * minute))