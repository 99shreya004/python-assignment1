# Define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Example input string
my_str = "Hello!!!, he said ---and went."

# Remove punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct += char

# Display the unpunctuated string
print(no_punct)
