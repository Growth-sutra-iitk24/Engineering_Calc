# Thermodynamics Calculations

"""
This file contains thermodynamic calculations and steam tables.
"""

class Thermodynamics:
    @staticmethod
    def calculate_heat_transfer(mass, specific_heat, delta_temperature):
        """
        Calculate heat transfer.
        :param mass: Mass of the substance (kg)
        :param specific_heat: Specific heat capacity (J/kg.K)
        :param delta_temperature: Change in temperature (K)
        :return: Heat transfer (J)
        """
        return mass * specific_heat * delta_temperature

    @staticmethod
    def steam_table(pressure):
        """
        Returns the saturated temperature for a given pressure in kPa.
        :param pressure: Pressure in kPa
        :return: Saturated temperature in °C
        """
        # Example values (in reality, you would need a full steam table):
        steam_tables = {
            0.1: 45.81,
            0.2: 120.23,
            0.5: 151.83,
            1.0: 179.88,
            5.0: 233.25
        }
        return steam_tables.get(pressure, "Pressure not found")

if __name__ == '__main__':
    # Example usage
    heat = Thermodynamics.calculate_heat_transfer(5, 4.18, 10)  # 5 kg, 4.18 J/kg.K, 10 K
    print(f'Heat transfer: {heat} J')
    temp = Thermodynamics.steam_table(1.0)  # Example pressure
    print(f'Saturated temperature at 1.0 kPa: {temp} °C')
