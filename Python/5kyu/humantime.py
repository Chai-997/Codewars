# Write a function, which takes a non-negative integer (seconds)
# as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):
    h = '{:02d}'.format(seconds // 3600)
    m = '{:02d}'.format((seconds % 3600) // 60)
    s = '{:02d}'.format(seconds % 60)
    return f"{h}:{m}:{s}"

print(make_readable(3600))