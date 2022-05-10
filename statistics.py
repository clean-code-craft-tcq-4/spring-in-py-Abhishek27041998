import math
from typing import Dict


def calculateStats(numbers):
  computedStats: Dict[str: float] = {}

  # Check if the numbers list is empty
  if len(numbers) == 0:
    computedStats['avg'] = math.nan
    computedStats['min'] = math.nan
    computedStats['max'] = math.nan
  else:
    computedStats['avg'] = sum(numbers) / len(numbers)
    computedStats['min'] = min(numbers)
    computedStats['max'] = max(numbers)

  return computedStats