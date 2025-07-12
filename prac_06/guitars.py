"""
Programming Task - Instrument input/output app
Time Estimated: 30 mins
Time Spent: 28 mins
"""

from instrument import Instrument

print("My instruments!")
instruments = []

instrument_name = input("Model name: ")
while instrument_name != "":
    made_year = int(input("Year made: "))
    price = float(input("Price: $"))
    new_instrument = Instrument(instrument_name, made_year, price)
    instruments.append(new_instrument)
    print(f"{new_instrument} added.\n")
    instrument_name = input("Model name: ")

# Optional hardcoded additions (commented)
# instruments.append(Instrument("Gibson L-5 CES", 1922, 16035.40))
# instruments.append(Instrument("Yamaha F310", 2013, 765.40))

# Display results
print("\nThese are my instruments:")
for idx, item in enumerate(instruments, 1):
    status = " (classic)" if item.is_classic() else ""
    print(f"Instrument {idx}: {item.model:>20} ({item.made_year}), worth ${item.price:10,.2f}{status}")
