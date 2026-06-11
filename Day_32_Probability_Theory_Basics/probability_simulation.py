"""
Day 32: Probability Theory Basics - Simulation
Simulating probability concepts using Python to demonstrate empirical vs. theoretical
probabilities, conditional/joint probability, and the Law of Large Numbers.
"""

import random
import os

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

# 1. Simulate Coin Flips (Biased or Unbiased)
def simulate_coin_flips(trials=10000, p_heads=0.5):
    """
    Simulates coin flips and returns empirical probability of heads.
    Also returns a history of running estimates to visualize convergence.
    """
    heads = 0
    history = []
    
    for i in range(1, trials + 1):
        # random.random() returns a float in [0.0, 1.0)
        if random.random() < p_heads:
            heads += 1
        history.append(heads / i)
        
    return heads / trials, history

# 2. Simulate Dice Rolls
def simulate_dice_rolls(trials=10000, target_faces=None):
    """
    Simulates dice rolls. target_faces can be a set of values (e.g., {2, 4, 6} for even).
    """
    if target_faces is None:
        target_faces = {2, 4, 6} # Default to even numbers
        
    favorable_outcomes = 0
    history = []
    
    for i in range(1, trials + 1):
        roll = random.randint(1, 6)
        if roll in target_faces:
            favorable_outcomes += 1
        history.append(favorable_outcomes / i)
        
    return favorable_outcomes / trials, history

# 3. Simulate Conditional and Joint Probabilities (Rain & Traffic)
def simulate_weather_traffic(trials=10000, p_rain=0.3, p_traffic_given_rain=0.8, p_traffic_given_no_rain=0.3):
    """
    Simulates weather and traffic conditions.
    Estimates:
    - P(Rain)
    - P(Traffic | Rain) (Conditional)
    - P(Traffic and Rain) (Joint)
    - P(Traffic) (Total Probability)
    """
    rain_count = 0
    traffic_count = 0
    rain_and_traffic_count = 0
    
    for _ in range(trials):
        is_rain = random.random() < p_rain
        # Traffic depends on whether it rains
        p_traffic = p_traffic_given_rain if is_rain else p_traffic_given_no_rain
        has_traffic = random.random() < p_traffic
        
        if is_rain:
            rain_count += 1
            if has_traffic:
                rain_and_traffic_count += 1
        if has_traffic:
            traffic_count += 1
            
    empirical_p_rain = rain_count / trials
    empirical_p_traffic = traffic_count / trials
    empirical_p_joint = rain_and_traffic_count / trials
    
    # Conditional probability P(Traffic | Rain) = P(Traffic and Rain) / P(Rain)
    empirical_p_cond = (rain_and_traffic_count / rain_count) if rain_count > 0 else 0.0
    
    return {
        "P(Rain)": empirical_p_rain,
        "P(Traffic)": empirical_p_traffic,
        "P(Traffic and Rain)": empirical_p_joint,
        "P(Traffic | Rain)": empirical_p_cond
    }

def run_convergence_demo():
    """Demonstrates how increasing trials converges to theoretical probability."""
    print("=== Law of Large Numbers Convergence Demo ===")
    p_true = 0.7 # Biased coin (70% heads)
    trial_steps = [10, 100, 1000, 10000, 100000]
    
    print(f"Theoretical P(Heads) = {p_true}\n")
    print(f"{'Trials':<12} | {'Empirical P(Heads)':<20} | {'Absolute Error':<15}")
    print("-" * 55)
    
    for t in trial_steps:
        p_empirical, _ = simulate_coin_flips(trials=t, p_heads=p_true)
        error = abs(p_empirical - p_true)
        print(f"{t:<12} | {p_empirical:<20.6f} | {error:<15.6f}")
    print()

def plot_convergence(history_unbiased, history_biased):
    """Plots the convergence of coin flips using matplotlib."""
    if not HAS_MATPLOTLIB:
        print("\n[Notice] matplotlib is not installed. Skipping convergence plot creation.")
        print("To enable plotting, run: pip install matplotlib")
        return
        
    plt.figure(figsize=(10, 6))
    
    # Plot unbiased coin convergence
    plt.plot(history_unbiased, label="Empirical P(Heads) - Fair Coin", color="#3b82f6", alpha=0.8)
    plt.axhline(y=0.5, color="#1d4ed8", linestyle="--", label="Theoretical P(Heads) = 0.5")
    
    # Plot biased coin convergence
    plt.plot(history_biased, label="Empirical P(Heads) - Biased Coin (0.7)", color="#f59e0b", alpha=0.8)
    plt.axhline(y=0.7, color="#b45309", linestyle="--", label="Theoretical P(Heads) = 0.7")
    
    plt.xscale('log') # Logarithmic scale for better visualization of convergence stages
    plt.title("Law of Large Numbers: Convergence to Theoretical Probability", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Number of Trials (Log Scale)", fontsize=12)
    plt.ylabel("Empirical Probability", fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(frameon=True, facecolor="white", edgecolor="none")
    plt.tight_layout()
    
    filename = "probability_convergence.png"
    plt.savefig(filename, dpi=300)
    print(f"\n[Success] Convergence plot saved as '{filename}'")
    plt.close()

if __name__ == "__main__":
    print("--- Day 32: Probability Theory Basics ---")
    
    # Set seed for reproducible results
    random.seed(42)
    
    # 1. Basic Fair Coin Simulation
    print("\n--- 1. Coin Toss Experiments ---")
    p_fair, history_fair = simulate_coin_flips(trials=10000, p_heads=0.5)
    p_biased, history_biased = simulate_coin_flips(trials=10000, p_heads=0.7)
    
    print(f"Fair Coin (10k trials)   - Empirical P(Heads): {p_fair:.4f} (Expected: ~0.5)")
    print(f"Biased Coin (10k trials) - Empirical P(Heads): {p_biased:.4f} (Expected: ~0.7)")
    
    # 2. Dice Roll Simulation (Even Numbers)
    print("\n--- 2. Dice Roll Experiments ---")
    p_even, _ = simulate_dice_rolls(trials=10000, target_faces={2, 4, 6})
    p_three, _ = simulate_dice_rolls(trials=10000, target_faces={3})
    
    print(f"Even Numbers (10k trials) - Empirical P(Even): {p_even:.4f} (Expected: 0.5000)")
    print(f"Rolling a 3 (10k trials)  - Empirical P(3):    {p_three:.4f} (Expected: 0.1667)")
    
    # 3. Weather & Traffic (Conditional & Joint)
    print("\n--- 3. Weather & Traffic Simulation ---")
    # Setup: P(Rain) = 0.3, P(Traffic | Rain) = 0.8, P(Traffic | No Rain) = 0.3
    stats = simulate_weather_traffic(trials=50000)
    print("Simulated Parameters: P(Rain) = 0.3, P(Traffic|Rain) = 0.8, P(Traffic|No Rain) = 0.3")
    print(f"Empirical P(Rain):         {stats['P(Rain)']:.4f} (Expected: 0.3000)")
    print(f"Empirical P(Traffic|Rain): {stats['P(Traffic | Rain)']:.4f} (Expected: 0.8000)")
    print(f"Empirical P(Traffic):      {stats['P(Traffic)']:.4f} (Expected: 0.3*0.8 + 0.7*0.3 = 0.4500)")
    print(f"Empirical P(Traffic & Rain) [Joint]: {stats['P(Traffic and Rain)']:.4f} (Expected: 0.3*0.8 = 0.2400)")
    
    # 4. Convergence Demo
    print()
    run_convergence_demo()
    
    # 5. Generate plot
    plot_convergence(history_fair, history_biased)
