import re

text = """Contact: test.user@gmail.com, admin@site.org. 
Event dates: 12-05-2023, 14/08/2024. Old date: 31-12-1999."""

# Extract Emails
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Emails:", emails)

# Extract Dates (dd-mm-yyyy or dd/mm/yyyy)
dates = re.findall(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b', text)
print("Dates:", dates)