file = open("input.txt", 'r')
data = file.read()
lines = data.splitlines()

start = int(lines[0])
ids = [int(id) for id in lines[1].split(',') if id != 'x']

# Part 1
print("Part 1")
departures = [(id, ((start // id) + 1) * id) for id in ids]
departures = sorted(departures, key=lambda x: x[1])
print("Value:", departures[0][0] * (departures[0][1] - start))


buses = [(int(id), offset) for offset, id in enumerate(lines[1].split(',')) if id != 'x']
buses = sorted(buses, key=lambda x: -x[0]) # Larges id first


def check_time(buses, time):
  for bus in buses:
    if (time + bus[1]) % bus[0] != 0:
      return False
  return True


# Part 2
print("Part 2")
step = buses[0][0]
time = step - buses[0][1]
for n in range(1, len(buses)):
  while True:
    if check_time(buses[:(n+1)], time):
      break
    else:
      time += step
  step *= buses[n][0]
print("First time:", time)