import random

# ==========================================
# 1. ENCAPSULATION & DATA HIDING
# ==========================================
class Environment:
    """Represents the world/room the agent interacts with."""
    def __init__(self, initial_temp: float):
        # Private attributes (encapsulation) preventing direct outside tampering
        self.__temperature = initial_temp
        self.__ac_on = False

    # Getters and Setters to control access safely
    def get_temperature(self) -> float:
        return self.__temperature

    def set_temperature(self, value: float):
        self.__temperature = round(value, 2)

    def is_ac_on(self) -> bool:
        return self.__ac_on

    def set_ac_status(self, status: bool):
        self.__ac_on = status

    def simulate_weather(self):
        """Simulates environment changes over time."""
        # Randomly fluctuates temperature up or down
        change = random.choice([0.5, 1.0, -0.5])
        self.set_temperature(self.__temperature + change)


# ==========================================
# 2. BASE AGENT CLASS (Abstraction)
# ==========================================
from abc import ABC,abstractmethod
class Agent(ABC):
    """A generic blueprint for a Software Agent."""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def perceive(self, environment: Environment) -> float:
        """Senses the environment data."""
        raise NotImplementedError("Subclasses must implement perceive().")

    @abstractmethod
    def think(self, perception_data: float) -> str:
        """Processes data and determines an action."""
        raise NotImplementedError("Subclasses must implement think().")

    @abstractmethod
    def act(self, action: str, environment: Environment):
        """Executes the chosen action on the environment."""
        raise NotImplementedError("Subclasses must implement act().")


# ==========================================
# 3. INHERITANCE & POLYMORPHISM
# ==========================================
class SmartACAgent(Agent):
    """A specialized reflex agent inheriting from the base Agent class."""
    def __init__(self, name: str, threshold_temp: float):
        super().__init__(name)
        self.threshold = threshold_temp  # Target temperature trigger

    # Polymorphism: Overriding the base class methods with agent logic
    def perceive(self, environment: Environment) -> float:
        current_temp = environment.get_temperature()
        print(f"[{self.name}] Sensed Room Temperature: {current_temp}°C")
        return current_temp

    def think(self, current_temp: float) -> str:
        if current_temp > self.threshold:
            return "TURN_ON_AC"
        elif current_temp < (self.threshold - 2.0):
            return "TURN_OFF_AC"
        return "DO_NOTHING"

    def act(self, action: str, environment: Environment):
        if action == "TURN_ON_AC":
            if not environment.is_ac_on():
                environment.set_ac_status(True)
                print(f"[{self.name}] Action: 🟢 Turning ON the AC.")
            # AC lowers the room temperature
            environment.set_temperature(environment.get_temperature() - 1.5)
        
        elif action == "TURN_OFF_AC":
            if environment.is_ac_on():
                environment.set_ac_status(False)
                print(f"[{self.name}] Action: 🔴 Turning OFF the AC.")
                
        else:
            print(f"[{self.name}] Action: 💤 Maintaining status quo.")


# ==========================================
# 4. EXECUTION LOOP (Simulation)
# ==========================================
if __name__ == "__main__":
    # Instantiate Objects
    living_room = Environment(initial_temp=26.0)
    home_agent = SmartACAgent(name="ThermoAgent-v1", threshold_temp=25.0)

    print(f"--- Starting Simulation with {home_agent.name} ---")
    
    # Simple agent execution loop
    for step in range(1, 6):
        print(f"\n--- Hour {step} ---")
        living_room.simulate_weather()
        
        # The Core Agent Cycle: Sense -> Think -> Act
        reading = home_agent.perceive(living_room)
        decision = home_agent.think(reading)
        home_agent.act(decision, living_room)
        
        print(f"Room Status -> AC On: {living_room.is_ac_on()}, Real Temp: {living_room.get_temperature()}°C")
