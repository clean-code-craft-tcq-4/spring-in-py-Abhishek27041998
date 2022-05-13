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


class EmailAlert:
  def __init__(self):
    self.emailSent = False


class LEDAlert:
  def __init__(self):
    self.ledGlows = False


class StatsAlerter:
  def __init__(self, maxThreshold, email_led_alert):
    self.maxThreshold = maxThreshold
    self.email_alert: EmailAlert = email_led_alert[0]
    self.led_alert: LEDAlert = email_led_alert[1]

  def checkAndAlert(self, numbers):
    computedStats = calculateStats(numbers)

    if computedStats['max'] > self.maxThreshold:
      self.email_alert.emailSent = True
      self.led_alert.ledGlows = True
