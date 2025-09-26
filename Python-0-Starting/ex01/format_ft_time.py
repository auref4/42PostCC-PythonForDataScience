import time

t = time.gmtime(0)
sec = time.time()

# Using f-string to insert sec and modify it directly
thousands_comma = f"{sec:,.3f}"  # .3f for convert in float with max 3 number
scientific_notation = f"{sec:.2e}"  # .2e for exponential and round to 2 digits

print("Seconds since Janunary 1, 1970:", thousands_comma,
      "or", scientific_notation, "in scientific notation")
print(time.strftime("%b %d %Y"))
