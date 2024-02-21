import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth + self.calculate_manhattan_distance()

    def calculate_manhattan_distance(self):
        distance = 0
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j], 3)
                    distance += abs(i - goal_row) + abs(j - goal_col)
        return distance

    def generate_children(self):
        children = []
        zero_row, zero_col = self.find_zero_position()
        moves = [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]
        for dr, dc, move_name in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = copy.deepcopy(self.state)
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                children.append(PuzzleNode(new_state, self, move_name, self.depth + 1))
        return children

    def find_zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_path(self):
        path = []
        current_node = self
        while current_node.parent is not None:
            path.append(current_node.move)
            current_node = current_node.parent
        path.reverse()
        return path

    def __lt__(self, other):
        return self.cost < other.cost

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    open_list = [initial_node]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            return current_node.get_path()
        closed_list.add(tuple(map(tuple, current_node.state)))
        children = current_node.generate_children()
        for child in children:
            if tuple(map(tuple, child.state)) not in closed_list:
                heapq.heappush(open_list, child)

    return None

print("Enter the initial state of the puzzle (0 represents the empty space):")
initial_state = []
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

solution = solve_puzzle(initial_state)

print("\nInitial State:")
for row in initial_state:
    print(row)

if solution:
    print("\nSolution Steps:")
    current_state = copy.deepcopy(initial_state)
    print("Step 0:")
    for row in current_state:
        print(row)
    for i, move in enumerate(solution, start=1):
        zero_row, zero_col = PuzzleNode(current_state).find_zero_position()
        if move == 'left':
            current_state[zero_row][zero_col], current_state[zero_row][zero_col - 1] = current_state[zero_row][zero_col - 1], current_state[zero_row][zero_col]
        elif move == 'right':
            current_state[zero_row][zero_col], current_state[zero_row][zero_col + 1] = current_state[zero_row][zero_col + 1], current_state[zero_row][zero_col]
        elif move == 'up':
            current_state[zero_row][zero_col], current_state[zero_row - 1][zero_col] = current_state[zero_row - 1][zero_col], current_state[zero_row][zero_col]
        elif move == 'down':
            current_state[zero_row][zero_col], current_state[zero_row + 1][zero_col] = current_state[zero_row + 1][zero_col], current_state[zero_row][zero_col]
        print(f"\nStep {i}:")
        for row in current_state:
            print(row)
else:
    print("\nNo solution found.")
