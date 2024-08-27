# 0° Fahrenheit to Celsius
Fahrenheit = 0
Celsius = round(((Fahrenheit - 32) * (5/9)), 2)
print("A temperature of 0 Fahrenheit is equivalent to", Celsius, "Celsius")
# 100° Fahrenheit to Celsius
Fahrenheit = 100
Celsius = round(((Fahrenheit - 32) * (5/9)), 2)
print("A temperature of 100 Fahrenheit is equivalent to", Celsius, "Celsius")
# Your Age in Seconds
age_in_years = 14
secs_in_min = 60
age_in_seconds = age_in_years * 365 * 24 * 60 * secs_in_min
print("If you are", age_in_years, "years old, then you are", age_in_seconds, "seconds old")
# My Age in Seconds
age_in_years = 51
secs_in_min = 60
age_in_seconds = age_in_years * 365 * 24 * 60 * secs_in_min
print("If you are", age_in_years, "years old, then you are", age_in_seconds, "seconds old")
# My Dog's Age in Seconds
age_in_years = 9
secs_in_min = 60
age_in_seconds = age_in_years * 365 * 24 * 60 * secs_in_min
print("If your dog is", age_in_years, "years old, then she is", age_in_seconds, "seconds old")
# Sphere Surface Area and Volume Part 1
radius = 6
PI = 3.14159
sphere_surface_area = round(4 * PI * (radius ** 2), 2)
sphere_volume = round((4/3) * PI * (radius ** 3), 2)
print("The surface area of a sphere with a radius of", radius, "is", sphere_surface_area, "and its volume is", sphere_volume)
# Sphere Surface Area and Volume Part 2
radius = 18
PI = 3.14159
sphere_surface_area = round(4 * PI * (radius ** 2), 2)
sphere_volume = round((4/3) * PI * (radius ** 3), 2)
print("The surface area of a sphere with a radius of", radius, "is", sphere_surface_area, "and its volume is", sphere_volume)
# Third Digit Part 1
an_int = 13579
third_digit_of_an_int = (an_int // 100) % 10
print("The third digit to the right in", an_int, "is", third_digit_of_an_int)
# Third Digit Part 2
another_int = 246810
third_digit_of_another_int = (another_int // 100) % 10
print("The third digit to the right in", another_int, "is", third_digit_of_another_int)
# Input Radius
radius = int(input("What is the sphere's radius? "))
PI = 3.14159
sphere_volume = round((4/3) * PI * (radius ** 3), 2)
print("The volume of a sphere with a radius of", radius, "is", sphere_volume)