# Program Name: Question 2
# Program Description: Question 2 analyzes a log file (part2.log) containing Linux server log entries, where each entry includes a timestamp, log level,
# and component information. It parses the log file to identify and print the three most commonly used components, provides brief descriptions for these components,
# and generates a bar graph that illustrates the usage patterns of these components during both working and after hours, dividing the day into distinct periods.
# Written By: Vanessa Rice
# Written On: September 19, 2023

# Imports
import re
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

# Step 1: Open the log file and read lines one at a time
log_entries = []
log_file_path = 'part2.log'

# Read lines one at a time
def get_line(file_path: str):
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            yield line

for line in get_line(log_file_path):
    # Split each line by spaces
    parts = line.split()
    if len(parts) >= 6:
        # Extract date and component fields
        date_str = " ".join(parts[:3])
        component = parts[4].split('[')[0]
        log_entries.append((date_str, component))

# Step 2: Create a datetime object to record the date
date_format = "%b %d %H:%M:%S"
dates = [datetime.datetime.strptime(date_str, date_format) for date_str, _ in log_entries]
print(len(log_entries))

# Step 3: Find and print the three most commonly used components
component_counts = Counter(component for _, component in log_entries)
common_components = component_counts.most_common(3)
print("Three most common components:")
for component, count in common_components:
    print(f"{component}: {count} occurrences")

# Step 4: Create dictionaries to count component usage during working and after hours
working_hours_start = 9
working_hours_end = 17
working_hours_components = defaultdict(int)
after_hours_components = defaultdict(int)

# Step 5: Count component usage during working and after hours
for date, component in zip(dates, (comp for _, comp in log_entries)):
    if working_hours_start <= date.hour < working_hours_end:
        working_hours_components[component] += 1
    else:
        after_hours_components[component] += 1

# Extract data for plotting
common_components_names = [component for component, _ in common_components]
working_hours_counts = [working_hours_components[component] for component in common_components_names]
after_hours_counts = [after_hours_components[component] for component in common_components_names]

# Step 6: Create a bar plot to visualize component usage
plt.figure(figsize=(10, 6))

bar_width = 0.4
index = range(len(common_components_names))

plt.bar(index, working_hours_counts, bar_width, label='Working Hours', color='red')
plt.bar([i + bar_width for i in index], after_hours_counts, bar_width, label='After Hours', color='blue')

plt.xlabel('Components')
plt.ylabel('Number of Entries')
plt.title('Component Usage During Working Hours and After Hours')
plt.xticks([i + bar_width / 2 for i in index], common_components_names, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


