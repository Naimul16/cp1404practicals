"""Programming Exercise - Vehicle class demonstration."""


class Vehicle:
    """Defines a basic vehicle with fuel tracking and distance traveled."""

    def __init__(self, model_name="", fuel_level=0):
        """Create a new Vehicle instance.

        model_name: str - name of the vehicle
        fuel_level: float - how much fuel is in the tank (1 unit = 1 km)
        """
        self.model_name = model_name
        self.fuel_level = fuel_level
        self._distance_covered = 0

    def refuel(self, litres):
        """Increase the fuel level by the specified amount."""
        self.fuel_level += litres

    def travel(self, km):
        """Move the vehicle forward by a certain distance.

        It will drive as far as the fuel allows. Returns the actual km driven.
        """
        if km > self.fuel_level:
            km = self.fuel_level
            self.fuel_level = 0
        else:
            self.fue

