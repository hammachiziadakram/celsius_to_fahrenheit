def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be numeric")

    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")

    return celsius * 9 / 5 + 32