# Input your weight on earth.
weight_on_earth = float(input("Enter your weight on earth: "))

# Your weigh_on_moon = ((weight on earth) * 1.622/9.81 ,2) 
weight_on_moon = round((weight_on_earth) * 1.622/9.81 ,2)

# Finaly it will print your weight on moon.
print(f"Your weight on moon is {weight_on_moon}")