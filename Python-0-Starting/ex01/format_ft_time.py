import  time
from    datetime import date

t = time.gmtime(0)
sec = time.time()
thousands_comma = f"{sec:,.3f}"
scientific_notation = f"{sec:.2e}"

print("Seconds since Janunary 1, 1970:", thousands_comma, "or", scientific_notation, "in scientific notation")
print(time.strftime("%b %d %Y"))
