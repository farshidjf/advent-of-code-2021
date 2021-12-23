A, B, C, D = 1, 10, 100, 1000
hallway = [0] * 11
entrance = [2, 4, 6, 8]
Amphipads = [A, B, C, D]
target_room = {A: 0, B: 1, C: 2, D: 3}
INF = 10000000000

def solve(rooms: list[list[int]], hallway: list[int], capacity: int = 2) -> int:
      if all(sum(room) == capacity * Amphipads[i] for i, room in enumerate(rooms)): 
            return 0
      
      def accessible_hallway(room_number: int) -> list[int]:
            _entrance = entrance[room_number]
            i1 = _entrance - next((i for i, x in enumerate(hallway[_entrance::-1]) if x), _entrance + 1)
            i2 = _entrance + next((i for i, x in enumerate(hallway[_entrance:]) if x), 11 - _entrance)
            return [i for i in range(i1 + 1, i2) if i not in entrance]
      
      def has_access_to(h: int, room_number: int) -> bool:
            if h < (e := entrance[room_number]):
                  return not any(hallway[h+1: e])
            return not any(hallway[e: h])
      
      for h, amph in enumerate(hallway):
            if amph:
                  if has_access_to(h, target_room[amph]):
                        room = rooms[target_room[amph]]
                        if all(a == amph for a in room):
                              hallway[h] = 0
                              room.append(amph)
                              move_cost = (capacity - len(room) + 1 + abs(h - entrance[target_room[amph]])) * amph
                              return move_cost + solve(rooms, hallway, capacity)
      cost = []
      for i, room in enumerate(rooms):
            if room and sum(room) != len(room) * Amphipads[i]:
                  for h in accessible_hallway(i):
                        _rooms = [r[:-1].copy() if i == ii else r.copy() for ii, r in enumerate(rooms)]
                        _hallway = hallway.copy()
                        _hallway[h] = room[-1]
                        move_cost = (capacity - len(room) + 1 + abs(h - entrance[i])) * room[-1]
                        cost.append(solve(_rooms, _hallway, capacity) + move_cost)
      if cost: return min(cost)
      return INF

inputs = (('Puzzle 1', [[B, D], [A, D], [A, C], [C, B]]),
          ('Puzzle 2', [[B, D, D, D], [A, B, C, D], [A, A, B, C], [C, C, A, B]]))
for label, rooms in inputs[:]:
      print(f'{label}: {solve(rooms, hallway, len(rooms[0]))}')