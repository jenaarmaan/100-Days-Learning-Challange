"""
Day 1 Task: The Thermostat Agent
Demonstrating the Intelligence Loop (Perception -> Reasoning -> Action -> Learning)
"""

# 1. Create a simple environment
# Temperature values simulating different states (cold, normal, hot)
environment_temperatures = [16, 20, 24, 18, 26, 21, 15]

# 2. Define an agent
class ThermostatAgent:
    def __init__(self):
        # Initial reasoning rule
        self.threshold = 18
        # Track mistakes
        self.mistakes = 0

    def perceive(self, temperature):
        # Perception: Agent observes the environment
        return temperature

    def act(self, temperature):
        # Reasoning & Action: Agent processes information and changes environment
        if temperature < self.threshold:
            return "HEATER_ON"
        else:
            return "HEATER_OFF"
            
    def learn(self, is_mistake):
        # Learning: Agent updates behavior using feedback
        if is_mistake:
            self.mistakes += 1
            # Adjust thresholds
            self.threshold += 1


def main():
    agent = ThermostatAgent()

    print(f"Initial threshold: {agent.threshold}")
    print("-" * 30)

    for temp in environment_temperatures:
        # --- The Intelligence Loop ---
        
        # Step 1: Perception
        perceived_temp = agent.perceive(temp)
        
        # Step 2 & 3: Reasoning & Action
        action = agent.act(perceived_temp)
        print(f"Temp: {temp} -> Action: {action}")
        
        # Let's simulate feedback. Assume the true comfortable threshold is 22.
        # If it's colder than 22 but the heater is OFF, it's a mistake.
        mistake = False
        if temp < 22 and action == "HEATER_OFF":
            mistake = True
            print("  -> Feedback: Mistake! Too cold.")
            
        # Step 4: Learning
        agent.learn(mistake)

    print("-" * 30)
    print(f"Total mistakes tracked: {agent.mistakes}")
    print(f"Final adjusted threshold: {agent.threshold}")

if __name__ == "__main__":
    main()
