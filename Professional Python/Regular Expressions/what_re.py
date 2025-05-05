import re  # Regular expressions module

# Sample text
text = "BTK Akademi Python Dersleri BTK"

# Pattern to search
pattern = "BTK"

# Search for the first match of 'BTK'
match = re.search(pattern, text)

# Save the match object
sonuc = match

# Get the start index of the match
sonuc = match.start()

# Get the end index of the match
sonuc = match.end()

# Find all matches of 'BTK' in the text
match = re.findall(pattern, text)

# Save all matches in 'sonuc'
sonuc = match

# Print the result
print(sonuc)
