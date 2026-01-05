#1
import re
"""
print list of dates
"""

text = """The events N 123456 happened on
15/03/2025, 01.12.2024 and 09-09-2023.
Deadline: 28/02/2022."""

print("Dates:", re.findall(r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}.\d{2}.\d{4}|\d{2}-\d{2}-\d{4})",
text))

#2
"""
print list of words 
"""
tag_input = "python, data-science / machine-learning; AI neural-networks"
output_ = [x for x in re.split(r"[,\s./;]",tag_input) if x != ""]


print("Output:", output_)
