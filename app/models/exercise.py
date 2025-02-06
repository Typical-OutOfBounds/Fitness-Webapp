from dataclasses import dataclass

@dataclass
class Exercise:
    location: str
    name: str
    sets: int
    reps: str
    rpe: str
    suggested_load: str
    actual_load: str
    actual_rpe: str
    notes: str
    actual_per: str