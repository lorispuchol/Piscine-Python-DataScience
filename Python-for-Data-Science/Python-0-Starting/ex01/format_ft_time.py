from datetime import datetime
from time import time

# Unix epoch
seconds_since_epoch = time()

# Format the seconds
formatted_seconds = "{:,.4f}".format(seconds_since_epoch)
scientific_notation = "{:.2e}".format(seconds_since_epoch)

# Print the formatted output
print("Seconds since January 1, 1970:", formatted_seconds, "or", scientific_notation, "in scientific notation")

current_date = datetime.now()
print(current_date.strftime("%b %d %Y"))
