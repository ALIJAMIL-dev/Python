import re  # Import the re (regular expressions) module

text = "A343a 123 XYZ 456 @&% 300 2 A343a 123456 1_2 abc"

# pattern = r"\d\d\d"              # Matches exactly 3 digits (e.g., 123)
# pattern = r"\d+"                 # Matches one or more digits (e.g., 123, 456)
# pattern = r"\d*"                 # Matches zero or more digits
# pattern = r"\d{3}"               # Matches exactly 3 digits
# pattern = r"\d{3,5}"             # Matches between 3 and 5 digits
# pattern = r"\d{3,}"              # Matches 3 or more digits
# pattern = r"\d{,5}"              # Matches up to 5 digits
# pattern = r"\d.\d"               # Matches a digit, any character, then another digit (e.g., 1_2)
# pattern = r"[a-zA-Z0-9]"         # Matches a single alphanumeric character (letter or digit)
# pattern = r"\d|[a-z]"            # Matches either a digit or a lowercase letter
# pattern = r"\d\w\w\w"            # Matches a digit followed by 3 word characters (letters, digits, or _)
# pattern = r"^A\d\w\w\w"          # Matches string that starts with 'A', followed by a digit and 3 word characters
pattern = r"A\d\w\w\w$"            # Matches string that ends with 'A', a digit, and 3 word characters

# matches = re.search(pattern, text)   # Searches for the first match
# matches = re.findall(pattern, text)  # Finds all matches and returns a list
matches = re.finditer(pattern, text)   # Finds all matches and returns an iterator

for match in matches:
    print(match.group())              # Prints the matched substring
