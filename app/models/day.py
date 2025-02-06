from dataclasses import dataclass, field
from typing import List
from app.models.exercise import Exercise

@dataclass
class Day:
    date: str
    sleep: int
    daily_steps: int
    cal_bef_training: int
    daily_protein_intake: int
    hydration: int
    caffeine: int
    stress: int
    external_fatigue: int
    training_time: str
    training_duration: str
    coach_notes: str
    client_feedback: str
    exercises: List[Exercise] = field(default_factory=list)