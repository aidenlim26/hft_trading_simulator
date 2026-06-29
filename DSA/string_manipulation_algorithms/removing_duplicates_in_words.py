text = "programming"
# dict.fromkeys creates a dictionary with characters as keys, automatically removing duplicates
unique_text = "".join(dict.fromkeys(text))
print(unique_text)  # Output: progamin