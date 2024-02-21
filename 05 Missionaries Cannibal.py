from collections import deque

# Function to check if a state is valid
def is_valid_state(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries < cannibals and missionaries > 0:
        return False
    return True

# Function to check if a state is the goal state
def is_goal_state(state):
    return state == (0, 0, 0)

# Function to get all possible next states from the current state
def get_next_states(state):
    states = []
    missionaries, cannibals, boat = state

    if boat == 1:
        for m in range(3):
            for c in range(3):
                if m + c > 0 and m + c <= 2:
                    new_state = (missionaries - m, cannibals - c, 0)
                    if is_valid_state(new_state):
                        states.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if m + c > 0 and m + c <= 2:
                    new_state = (missionaries + m, cannibals + c, 1)
                    if is_valid_state(new_state):
                        states.append(new_state)

    return states

# Function to solve the Missionaries and Cannibals problem using breadth-first search
def solve_missionaries_cannibals(start_missionaries, start_cannibals):
    start_state = (start_missionaries, start_cannibals, 1)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue

        visited.add(current_state)
        if is_goal_state(current_state):
            return path

        next_states = get_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Take input for the number of missionaries and cannibals on the starting side
start_missionaries = int(input("Enter the number of missionaries on the starting side: "))
start_cannibals = int(input("Enter the number of cannibals on the starting side: "))

# Solve the Missionaries and Cannibals problem
solution = solve_missionaries_cannibals(start_missionaries, start_cannibals)

# Print the solution
if solution:
    print("Solution Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
