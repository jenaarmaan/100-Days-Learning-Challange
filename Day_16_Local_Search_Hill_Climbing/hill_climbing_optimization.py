import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    """
    Objective Function: f(x) = -x^2 + 4x
    Wait, let's use a slightly more interesting function for visualization.
    Wait, user provided: -x^2 + 4x. Let's stick with it first.
    The maximum of -x^2 + 4x is when f'(x) = -2x + 4 = 0 => x = 2.
    """
    return -x**2 + 4*x

def hill_climbing(start_x, step_size=0.1, max_iter=100):
    """
    Hill Climbing Algorithm
    """
    x = start_x
    history = [x]
    
    for _ in range(max_iter):
        # We check both directions
        neighbors = [x + step_size, x - step_size]
        
        # Consider the best neighbor
        best_neighbor = max(neighbors, key=f)
        
        # If the best neighbor is not better than the current state, we are at a peak.
        if f(best_neighbor) <= f(x):
            print(f"Reached local maximum at x = {x:.4f}, f(x) = {f(x):.4f}")
            break
            
        x = best_neighbor
        history.append(x)
        
    return x, history

def visualize_hill_climbing(history):
    # Setup the plot
    x_range = np.linspace(-10, 10, 400)
    y_range = f(x_range)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label='Objective Function: f(x) = -x^2 + 4x', color='#2ecc71', linewidth=2)
    
    # Plot the starting point
    plt.scatter(history[0], f(history[0]), color='#e74c3c', s=100, label='Start State', zorder=5)
    
    # Plot the path
    history_y = [f(x) for x in history]
    plt.plot(history, history_y, '--', color='#f1c40f', alpha=0.6, label='Search Path', zorder=4)
    plt.scatter(history, history_y, color='#f39c12', s=30, alpha=0.8, zorder=4)
    
    # Final point
    plt.scatter(history[-1], f(history[-1]), color='#3498db', s=120, label='Best State Found', zorder=6)
    
    plt.title("Hill Climbing Visualization - Day 16", fontsize=16, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Save visualization for user reference
    plt.savefig('hill_climbing_result.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # 1. Initialize random starting position
    x_start = np.random.uniform(-10, 10)
    print(f"--- Starting Hill Climbing from x = {x_start:.4f} ---")
    
    # 2. Run the algorithm
    best_x, search_history = hill_climbing(x_start)
    
    # 3. Print Results
    print("\n[Results]")
    print(f"Final x: {best_x:.4f}")
    print(f"Maximum f(x): {f(best_x):.4f}")
    print(f"Total steps taken: {len(search_history)-1}")
    
    # 4. Generate Visualization
    print("\n[Visualization] Generating plot...")
    try:
        visualize_hill_climbing(search_history)
        print("Success: visualization saved as hill_climbing_result.png")
    except Exception as e:
        print(f"Error during visualization: {e}")
