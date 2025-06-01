import math

def calculate_forward_price(spot_price, risk_free_rate, time_to_maturity):
    return round(spot_price * math.exp(risk_free_rate * time_to_maturity), 2)

if __name__ == "__main__":
    # Exercise 1.2
    spot_price, risk_free_rate, time_to_maturity = 303, 0.01, 253 / 365
    print(calculate_forward_price(spot_price, risk_free_rate, time_to_maturity))