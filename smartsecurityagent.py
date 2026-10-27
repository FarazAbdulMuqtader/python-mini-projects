import random
from abc import ABC, abstractmethod


# ==========================================
# 1. ENVIRONMENT
# ==========================================
class Environment:
    def __init__(self, initial_temp: float):
        self.__temperature = initial_temp
        self.__ac_on = False
        self.__motion_detected = False  

    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        self.__temperature = round(value, 2)

    @property
    def ac_on(self) -> bool:
        return self.__ac_on

    @ac_on.setter
    def ac_on(self, status: bool):
        self.__ac_on = status

    @property
    def motion_detected(self) -> bool:
        return self.__motion_detected

    @motion_detected.setter
    def motion_detected(self, status: bool):
        self.__motion_detected = status

    def simulate_weather(self):
        change = random.choice([0.5, 1.0, -0.5])
        self.temperature = self.temperature + change

    def simulate_intruder(self):
        self.motion_detected = random.choice([True, False])

# ==========================================
# 2. BASE AGENT CLASS
# ==========================================
class Agent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def perceive(self, environment: Environment):
        pass

    @abstractmethod
    def think(self, perception_data):
        pass

    @abstractmethod
    def act(self, action: str, environment: Environment):
        pass


# ==========================================
# 3. AC AGENT
# ==========================================
class SmartACAgent(Agent):
    def __init__(self, name: str, threshold_temp: float):
        super().__init__(name)
        self.threshold = threshold_temp

    def perceive(self, environment: Environment) -> float:
        current_temp = environment.temperature
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
            if not environment.ac_on:
                environment.ac_on = True
                print(f"[{self.name}] Action: Turning ON the AC.")
            environment.temperature = environment.temperature - 1.5
        elif action == "TURN_OFF_AC":
            if environment.ac_on:
                environment.ac_on = False
                print(f"[{self.name}] Action: Turning OFF the AC.")
        else:
            print(f"[{self.name}] Action: Maintaining status quo.")


# ==========================================
# 4. SECURITY AGENT
# ==========================================
class SmartSecurityAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name)
        self.__alarm_triggered = False 

    @property
    def alarm_triggered(self) -> bool:
        return self.__alarm_triggered

    @alarm_triggered.setter
    def alarm_triggered(self, value: bool):
        self.__alarm_triggered = value

    def perceive(self, environment: Environment) -> bool:
        motion = environment.motion_detected
        print(f"[{self.name}] Sensed Motion: {motion}")
        return motion

    def think(self, motion_status: bool) -> str:
        if motion_status:
            return "TRIGGER_ALARM"
        return "STANDBY"

    def act(self, action: str, environment: Environment):
        if action == "TRIGGER_ALARM":
            self.alarm_triggered = True
            print("ALERT! Intruder detected! Alarm sounding!")
        elif action == "STANDBY":
            self.alarm_triggered = False
            print("Room is secure.")


# ==========================================
# 5. SIMULATION
# ==========================================
if __name__ == "__main__":
    living_room = Environment(initial_temp=26.0)

    climate_agent = SmartACAgent(name="ThermoAgent", threshold_temp=25.0)
    security_agent = SmartSecurityAgent(name="GuardAgent")

    print("--- Starting Multi-Agent Simulation ---")

    for step in range(1, 6):
        print(f"\n--- Hour {step} ---")
        living_room.simulate_weather()
        living_room.simulate_intruder()

        # 1. Climate Agent cycle
        temp_reading = climate_agent.perceive(living_room)
        ac_decision = climate_agent.think(temp_reading)
        climate_agent.act(ac_decision, living_room)

        # 2. Security Agent cycle
        motion_reading = security_agent.perceive(living_room)
        sec_decision = security_agent.think(motion_reading)
        security_agent.act(sec_decision, living_room)