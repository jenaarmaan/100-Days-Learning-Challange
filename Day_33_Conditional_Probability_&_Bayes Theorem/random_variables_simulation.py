"""
Day 33: Random Variables & Probability Distributions - Simulation
Simulates Bernoulli, Binomial, and Normal random variables, computes their statistics
(empirical vs. theoretical), and plots their distributions.
"""

import numpy as np
import os

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

# 1. Bernoulli Distribution (Success/Failure coin toss)
def simulate_bernoulli(p=0.5, trials=10000):
    """
    Simulates a Bernoulli trial (0 or 1) using np.random.binomial with n=1.
    """
    data = np.random.binomial(1, p, trials)
    theoretical_mean = p
    theoretical_var = p * (1 - p)
    return data, theoretical_mean, theoretical_var

# 2. Binomial Distribution (Successes in n independent trials)
def simulate_binomial(n=10, p=0.5, trials=10000):
    """
    Simulates Binomial random variables (number of successes in n trials).
    """
    data = np.random.binomial(n, p, trials)
    theoretical_mean = n * p
    theoretical_var = n * p * (1 - p)
    return data, theoretical_mean, theoretical_var

# 3. Normal (Gaussian) Distribution
def simulate_normal(mean=0.0, std=1.0, size=10000):
    """
    Simulates a continuous Normal distribution.
    """
    data = np.random.normal(mean, std, size)
    theoretical_mean = mean
    theoretical_var = std ** 2
    return data, theoretical_mean, theoretical_var

# 4. Utility to compute stats
def compute_stats(data):
    """Computes empirical mean and variance of data."""
    return np.mean(data), np.var(data)

def plot_distributions(bernoulli_data, binomial_data, normal_data, 
                       bern_params, bin_params, norm_params):
    """Plots histograms and density distributions for Bernoulli, Binomial, and Normal RVs."""
    if not HAS_MATPLOTLIB:
        print("\n[Notice] matplotlib is not installed. Skipping plot generation.")
        print("To enable visualization, run: pip install matplotlib")
        return

    # Create a 3-panel figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))
    
    # 1. Bernoulli Plot (Discrete PMF)
    p_bern = bern_params['p']
    ax = axes[0]
    unique, counts = np.unique(bernoulli_data, return_counts=True)
    frequencies = counts / len(bernoulli_data)
    ax.bar(unique, frequencies, color=["#f87171", "#60a5fa"], edgecolor="black", width=0.4, alpha=0.85)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Failure (0)', 'Success (1)'])
    ax.set_title(f"Bernoulli Distribution (p={p_bern})", fontsize=12, fontweight='bold')
    ax.set_ylabel("Empirical Probability", fontsize=10)
    ax.grid(True, axis='y', linestyle='--', alpha=0.3)
    
    # Add labels on top of bars
    for x, y in zip(unique, frequencies):
        ax.text(x, y + 0.02, f"{y:.4f}", ha='center', fontweight='bold')
    ax.set_ylim(0, 1.1)

    # 2. Binomial Plot (Discrete PMF)
    n_bin = bin_params['n']
    p_bin = bin_params['p']
    ax = axes[1]
    # Use bins centered on integers
    bins = np.arange(-0.5, n_bin + 1.5, 1)
    ax.hist(binomial_data, bins=bins, density=True, color="#34d399", edgecolor="black", alpha=0.75, rwidth=0.8)
    ax.set_title(f"Binomial Distribution (n={n_bin}, p={p_bin})", fontsize=12, fontweight='bold')
    ax.set_xlabel("Number of Successes", fontsize=10)
    ax.set_ylabel("Probability Density", fontsize=10)
    ax.set_xticks(range(0, n_bin + 1))
    ax.grid(True, linestyle='--', alpha=0.3)

    # 3. Normal Plot (Continuous PDF)
    mu = norm_params['mean']
    sigma = norm_params['std']
    ax = axes[2]
    # Empirical histogram
    count, bins, ignored = ax.hist(normal_data, bins=50, density=True, color="#a78bfa", edgecolor="black", alpha=0.6)
    # Theoretical bell curve
    x_theoretical = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    y_theoretical = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x_theoretical - mu) ** 2) / (2 * sigma ** 2))
    ax.plot(x_theoretical, y_theoretical, color="#6d28d9", linewidth=2.5, label="Theoretical PDF")
    ax.set_title(rf"Normal Distribution ($\mu$={mu}, $\sigma$={sigma})", fontsize=12, fontweight='bold')
    ax.set_xlabel("Values", fontsize=10)
    ax.set_ylabel("Probability Density", fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend()

    plt.suptitle("Probability Distributions of Random Variables", fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    filename = "distributions_visualization.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\n[Success] Distributions plot saved as '{filename}'")
    plt.close()

if __name__ == "__main__":
    print("--- Day 33: Random Variables & Probability Distributions ---")
    
    # Set seed for reproducibility
    np.random.seed(42)
    trials_count = 50000
    
    # 1. Simulate Bernoulli RV
    bern_p = 0.35
    bern_data, bern_t_mean, bern_t_var = simulate_bernoulli(p=bern_p, trials=trials_count)
    bern_e_mean, bern_e_var = compute_stats(bern_data)
    
    # 2. Simulate Binomial RV
    bin_n = 10
    bin_p = 0.5
    bin_data, bin_t_mean, bin_t_var = simulate_binomial(n=bin_n, p=bin_p, trials=trials_count)
    bin_e_mean, bin_e_var = compute_stats(bin_data)
    
    # 3. Simulate Normal RV
    norm_mean = 5.0
    norm_std = 2.0
    norm_data, norm_t_mean, norm_t_var = simulate_normal(mean=norm_mean, std=norm_std, size=trials_count)
    norm_e_mean, norm_e_var = compute_stats(norm_data)
    
    # Print statistics comparison
    print(f"\nExperiment size: {trials_count} trials")
    print("-" * 75)
    print(f"{'Distribution':<15} | {'Theoretical Mean':<18} | {'Empirical Mean':<18} | {'Error (Mean)':<12}")
    print(f"{'':<15} | {'Theoretical Var':<18} | {'Empirical Var':<18} | {'Error (Var)':<12}")
    print("-" * 75)
    
    # Bernoulli output
    print(f"{'Bernoulli (p=0.35)':<15} | {bern_t_mean:<18.4f} | {bern_e_mean:<18.4f} | {abs(bern_t_mean - bern_e_mean):<12.6f}")
    print(f"{'':<15} | {bern_t_var:<18.4f} | {bern_e_var:<18.4f} | {abs(bern_t_var - bern_e_var):<12.6f}")
    print("-" * 75)
    
    # Binomial output
    print(f"{'Binomial(10, 0.5)':<15} | {bin_t_mean:<18.4f} | {bin_e_mean:<18.4f} | {abs(bin_t_mean - bin_e_mean):<12.6f}")
    print(f"{'':<15} | {bin_t_var:<18.4f} | {bin_e_var:<18.4f} | {abs(bin_t_var - bin_e_var):<12.6f}")
    print("-" * 75)
    
    # Normal output
    print(f"{'Normal(5.0, 2.0)':<15} | {norm_t_mean:<18.4f} | {norm_e_mean:<18.4f} | {abs(norm_t_mean - norm_e_mean):<12.6f}")
    print(f"{'':<15} | {norm_t_var:<18.4f} | {norm_e_var:<18.4f} | {abs(norm_t_var - norm_e_var):<12.6f}")
    print("-" * 75)

    # Plot & Save
    plot_distributions(
        bernoulli_data=bern_data, 
        binomial_data=bin_data, 
        normal_data=norm_data,
        bern_params={'p': bern_p},
        bin_params={'n': bin_n, 'p': bin_p},
        norm_params={'mean': norm_mean, 'std': norm_std}
    )
