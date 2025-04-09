"""
Calculates the number of ways 2 students can be seated next to each other
in a classroom, given the desks already occupied.

Args:
  arr: A list of integers. The first element is the number of desks (K),
        and the rest are the desks already occupied (in sorted order).

Returns:
  The number of seating arrangements where 2 students can sit together.
"""

def seating_students(arr):

  num_desks = arr[0]
  occupied_desks = set(arr[1:])
  count = 0

  for i in range(1, num_desks, 2):  

    if i not in occupied_desks:
      if i + 1 <= num_desks and i + 1 not in occupied_desks:
        count += 1
      if i + 2 <= num_desks and i + 2 not in occupied_desks:
        count += 1

    if i + 1 <= num_desks and i + 1 not in occupied_desks:
      if i + 3 <= num_desks and i + 3 not in occupied_desks:
        count += 1

  return count

