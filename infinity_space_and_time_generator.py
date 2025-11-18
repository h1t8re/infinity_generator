def infinity_space_generator(units, coordinate, dimension):
  for unit in units:
    if len(coordinate)+1 < dimension:
      for x in infinity_space_generator(units, coordinate+str(unit), dimension):
        yield x
    elif len(coordinate)+1 == dimension:
      yield coordinate+str(unit)

def infinity_space_and_time_generator():
  i = 0
  while True:
    i = i + 1
    for x in infinity_space_generator([ y for y in range(0, i)], "", i):
      yield x
