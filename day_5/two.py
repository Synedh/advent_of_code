# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

# What is the ID of your seat?

# Your puzzle answer was 671.

seats = sorted(int(''.join('1' if i in 'BR' else '0' for i in seat[:-1]), 2) for seat in open('input').readlines())
print((set(range(seats[0], seats[-1] + 1)) - set(seats)).pop())
