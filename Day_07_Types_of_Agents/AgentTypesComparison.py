import numpy as np
import matplotlib.pyplot as plt

# --- Day 7: Types of Agents (Reflex vs. Learning) ---

"""
Scenario: A smart thermostat trying to find the optimal temperature threshold.
The "hidden" optimal setting is 21°C.
"""

class ReflexAgent:
    """
    Acts based on a fixed hard-coded rule. 
    It doesn't change its behavior even if it performs poorly.
    """
    def __init__(self, threshold=24): # Hardcoded, possibly suboptimal
        self.threshold = threshold
    
    def act(self, temp):
        # 1 for heater ON, 0 for heater OFF
        return 1 if temp < self.threshold else 0

class LearningAgent:
    """
    Starts with a default rule but has a learning mechanism
    that adjusts its internal threshold based on 'correct' feedback.
    """
    def __init__(self, start_threshold=24, learning_rate=0.1):
        self.threshold = start_threshold
        self.learning_rate = learning_rate
        self.history = []

    def act(self, temp):
        return 1 if temp < self.threshold else 0
    
    def learn(self, temp, correct_action):
        # The agent compares its action to what it 'should' have done
        predicted_action = self.act(temp)
        
        if predicted_action != correct_action:
            # If it failed to turn on when it should have...
            if correct_action == 1: # Should be ON but is OFF
                self.threshold += self.learning_rate
            else: # Should be OFF but is ON
                self.threshold -= self.learning_rate
        
        self.history.append(self.threshold)

def simulate_comparison():
    # Environment Variables
    NUM_SAMPLES = 200
    HIDDEN_OPTIMAL = 21.0
    
    # Generate random temperatures from 15 to 30 degrees
    temps = np.random.uniform(15, 30, NUM_SAMPLES)
    
    reflex = ReflexAgent(threshold=24) # Fixed at a poor setting
    learning = LearningAgent(start_threshold=24) # Starts poor but learns
    
    reflex_correct_counts = 0
    learning_correct_counts = []
    
    # Run simulation
    for i, t in enumerate(temps):
        # What the environment actually requires (Ground Truth)
        correct_action = 1 if t < HIDDEN_OPTIMAL else 0
        
        # Reflex Agent performance
        if reflex.act(t) == correct_action:
            reflex_correct_counts += 1
            
        # Learning Agent performance
        if learning.act(t) == correct_action:
            if not learning_correct_counts:
                learning_correct_counts.append(1)
            else:
                learning_correct_counts.append(learning_correct_counts[-1] + 1)
        else:
            if not learning_correct_counts:
                learning_correct_counts.append(0)
            else:
                learning_correct_counts.append(learning_correct_counts[-1])
        
        # Learning agent improves from this experience
        learning.learn(t, correct_action)

    # FINAL RESULTS
    print(f"Simulation Finished ({NUM_SAMPLES} samples)")
    print(f"Target Optimal Threshold: {HIDDEN_OPTIMAL}°C")
    print("-" * 30)
    print(f"Reflex Agent Final Threshold: {reflex.threshold}°C (STUCK)")
    print(f"Learning Agent Final Threshold: {learning.threshold:.2f}°C (EVOLVED)")
    print("-" * 30)
    print(f"Reflex Accuracy: {(reflex_correct_counts/NUM_SAMPLES)*100:.1f}%")
    print(f"Learning Accuracy (cumulative): {(learning_correct_counts[-1]/NUM_SAMPLES)*100:.1f}%")

    # Optional visualization if matplotlib is available (using text if not)
    # Since I'm in a terminal, I'll print a simple trend summary
    print("\nLearning Progress (Last 10 updates):")
    for val in learning.history[-10:]:
        print(f"  Threshold moved to: {val:.2f}°C")

if __name__ == "__main__":
    simulate_comparison()
