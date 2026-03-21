"""
Day 8: State Space Representation - Part 2
Exploring State Space Explosion
"""

def count_states(grid_size):
    """Complexity of a grid state space is N^2."""
    return grid_size ** 2

def count_max_transitions(grid_size):
    """
    In a 4-neighbor grid, each state has at most 4 transitions.
    Transitions = 4 * N^2 - 4 * N (edges) - 4 (corners) ... roughly 4 * N^2.
    """
    # More precise calculation:
    # Interior states (N-2)^2 have 4 transitions.
    # Edge states 4*(N-2) have 3 transitions.
    # Corner states 4 have 2 transitions.
    if grid_size < 2: return 0
    interior = (grid_size - 2) ** 2
    edges = 4 * (grid_size - 2)
    corners = 4
    return (interior * 4) + (edges * 3) + (corners * 2)

def demonstrate_explosion():
    print(f"{'Grid Size (NxN)':<20} | {'Total States':<15} | {'Max Transitions':<20}")
    print("-" * 60)
    for n in [2, 4, 10, 50, 100, 1000]:
        states = count_states(n)
        transitions = count_max_transitions(n)
        print(f"{f'{n}x{n}':<20} | {f'{states:,}':<15} | {f'{transitions:,}':<20}")

if __name__ == "__main__":
    print("Demonstrating State Space Explosion in Grid Navigation:")
    demonstrate_explosion()
    print("\nConsider a 3D grid (NxNxN):")
    for n in [10, 100, 1000]:
        print(f"{n}x{n}x{n} Grid: {n**3:,} states")
        
    print("\nConsider Chess:")
    print("Estimated states in Chess: 10^120")
    print("This is why we can't just explore the entire state space for complex problems!")
