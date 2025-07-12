"""
Programming Task - Instrument test
Time Estimate: 25 mins
Actual Time: 30 mins
"""

from prac_06.instrument import Instrument

# Sample instruments
instrument1 = Instrument("Gibson L-5 CES", 1922, 16035.40)
instrument2 = Instrument("Yamaha F310", 2013, 765.40)

# Age checks (based on year 2022)
print(f"{instrument1.model} calculate_age() - Expected 100. Got {instrument1.calculate_age()}")
print(f"{instrument2.model} calculate_age() - Expected 9. Got {instrument2.calculate_age()}")

# Vintage/classic status
print(f"{instrument1.model} is_classic() - Expected True. Got {instrument1.is_classic()}")
print(f"{instrument2.model} is_classic() - Expected False. Got {instrument2.is_classic()}")
