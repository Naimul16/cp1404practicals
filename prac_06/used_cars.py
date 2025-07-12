"""
CP1404 Practical - Demo code using the Vehicle class.
Demonstrates how to create and use a vehicle object.
"""

from vehicle import Vehicle


def main():
    van = Vehicle("Shuttle Van", 100)
    van.refuel(20)
    print(f"Fuel after refueling: {van.fuel_level}")

    km_driven = van.travel(115)
    print(f"{van.model_name} traveled {km_driven} km")
    print(van)


main()
