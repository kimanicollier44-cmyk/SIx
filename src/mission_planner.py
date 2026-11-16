import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AutonomousMissionPlanner:
    """Decomposes complex macro missions into low-level execution pipelines."""
    def __init__(self, mission_name: str):
        self.mission_name = mission_name
        self.objectives = []

    def add_objective(self, description: str, priority: int):
        self.objectives.append({"desc": description, "priority": priority, "status": "pending"})

    def execute_mission(self):
        logging.info(f"Executing Mission: {self.mission_name}")
        sorted_objs = sorted(self.objectives, key=lambda x: x['priority'], reverse=True)
        for obj in sorted_objs:
            obj['status'] = 'completed'
            logging.info(f"Objective Accomplished: {obj['desc']}")
