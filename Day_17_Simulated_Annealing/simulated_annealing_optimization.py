import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Objective Function: f(x) = -x^2 + 4x + sin(5x)
    This creates multiple local maxima due to the sine term.
    """
    return -x**2 + 4*x + np.sin(5*x)

def run_simulated_annealing(start_x, T_init=10.0, cooling_rate=0.99, max_iters=1000):
    """
    Simulated Annealing Algorithm
    """
    x = start_x
    T = T_init
    history = [(x, f(x), T)]
    
    for i in range(max_iters):
        # 1. Propose a new state (neighboring move)
        # We use a normal distribution for random jumps
        new_x = x + np.random.normal(0, 0.5) 
        
        # 2. Calculate energy difference (delta)
        delta = f(new_x) - f(x)
        
        # 3. Acceptance Criteria
        # Accept if it's better (delta > 0)
        # Accept if it's worse with probability P = e^(delta / T)
        if delta > 0:
            x = new_x
        else:
            acceptance_prob = np.exp(delta / T)
            if np.random.rand() < acceptance_prob:
                x = new_x
                
        # 4. Temperature Cooling
        T *= cooling_rate
        history.append((x, f(x), T))
        
        # Stop early if T is extremely low
        if T < 1e-10:
            break
            
    return x, history

def visualize_optimization(history):
    # Prepare background function
    x_range = np.linspace(-4, 8, 1000)
    y_range = f(x_range)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [2, 1]})
    plt.subplots_adjust(hspace=0.3)
    
    # Plot 1: The Function and Search Path
    ax1.plot(x_range, y_range, label='Target Function (Bumpy)', color='#3498db', linewidth=2, alpha=0.7)
    
    # Extract data from history
    path_x = [step[0] for step in history]
    path_y = [step[1] for step in history]
    temps = [step[2] for step in history]
    
    # Color the path based on temperature (Hot = Red, Cold = Blue)
    sc = ax1.scatter(path_x, path_y, c=temps, cmap='inferno', s=15, alpha=0.5, label='Search Path (Color = Temp)', zorder=3)
    cbar = plt.colorbar(sc, ax=ax1)
    cbar.set_label('Temperature (T)')
    
    # Starting & Ending points
    ax1.scatter(path_x[0], path_y[0], color='green', s=100, label='Start Point', edgecolors='white', zorder=5)
    ax1.scatter(path_x[-1], path_y[-1], color='red', s=150, marker='*', label='Final Maxima Found', edgecolors='black', zorder=6)
    
    ax1.set_title("Simulated Annealing - Escaping Local Maxima", fontsize=16, fontweight='bold')
    ax1.set_xlabel("x", fontsize=12)
    ax1.set_ylabel("f(x)", fontsize=12)
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Plot 2: Temperature Cooling Schedule
    ax2.plot(range(len(temps)), temps, color='#e67e22', linewidth=2)
    ax2.fill_between(range(len(temps)), temps, color='#e67e22', alpha=0.1)
    ax2.set_title("Cooling Schedule (Temperature vs Iteration)", fontsize=12)
    ax2.set_xlabel("Iteration", fontsize=10)
    ax2.set_ylabel("T", fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.5)

    # Save visualization
    plt.savefig('simulated_annealing_result.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # 1. Random Initial Position
    x_initial = np.random.uniform(-4, 0) # Start on the left part
    print(f"--- Starting Simulated Annealing from x = {x_initial:.4f} ---")
    
    # 2. Run Algorithm
    # Initial T is high so it can jump easily
    best_x, search_history = run_simulated_annealing(x_initial, T_init=10.0, cooling_rate=0.993)
    
    # 3. Print Results
    print("\n[Results]")
    print(f"Final x: {best_x:.4f}")
    print(f"Maximum f(x): {f(best_x):.4f}")
    print(f"Total iterations: {len(search_history)}")
    
    # 4. Visualization
    print("\n[Visualization] Generating plot...")
    try:
        visualize_optimization(search_history)
        print("Success: visualization saved as simulated_annealing_result.png")
    except Exception as e:
        print(f"Error during visualization: {e}")
