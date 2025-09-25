import  time
from    datetime import date

t = time.gmtime(0)
sec = time.time()

# Using f-string to insert sec and modify it directly
thousands_comma = f"{sec:,.3f}" # .3f to convert in float with max 3 number
scientific_notation = f"{sec:.2e}" # .2e to use exponential and round to 2 digits

print("Seconds since Janunary 1, 1970:", thousands_comma, "or", scientific_notation, "in scientific notation")
print(time.strftime("%b %d %Y"))
