current_time = '1:28 PM'

def stopwatch(m, s):
    time_result = f'{m}:{s}'
    print(time_result)
    return "Time recorded"

print(f'The current time is {current_time}')
print(f'Result from stopwatch: {stopwatch(1, 12)}')
print(f'Result from stopwatch: {stopwatch(0, 48)}')