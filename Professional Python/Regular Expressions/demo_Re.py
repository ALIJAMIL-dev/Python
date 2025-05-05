import re  # Import the regular expressions module

text = "BTK Akademi ile Python kurs tarihleri 15-May-2025 15.May.2025 15/May/2025 15.05.2025. Telefon numaralarımız +90-530-999-9999 +90 530 999 9999. Mail adreslerimiz abc@gmail.com abc@gmail.co.tr abc@hotmail.com"

# pattern = r"\d\d-[a-zA-Z][a-zA-Z][a-zA-Z]-\d\d\d\d"           # Matches dates like 15-May-2025
# pattern = r"\d{2}-[a-zA-Z]{3}-\d{4}"                         # Same, using quantifiers for digits and letters
# pattern = r"\d{2}[-./][a-zA-Z0-9]{2,3}[-./]\d{4}"            # Matches dates in formats like 15/May/2025 or 15.05.2025
# pattern = r"\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}"         # Matches both 15/May/2025 and 15.05.2025

# pattern = r"\w+@[a-z]+(\.[a-z]{2,3})+"                       # Matches emails like abc@gmail.com or abc@gmail.co.tr

pattern = r"\+\d{2}[-\s]\d{3}[-\s]\d{3}[-\s]\d{4}"             # Matches phone numbers like +90-530-999-9999 or +90 530 999 9999

matches = re.finditer(pattern, text)  # Find all matches with detailed match info

for match in matches:
    print(match)  # Print each match object
