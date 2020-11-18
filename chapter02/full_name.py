# f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# python 3.5 or earlier -> format
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# tabs and newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# striping whitespace
favorite_language = 'python '
print(f"'{favorite_language}'")
print(f"'{favorite_language.rstrip()}'")

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(f"'{favorite_language}'")

favorite_language = ' python3 '
print(f"'{favorite_language.rstrip()}'")
print(f"'{favorite_language.lstrip()}'")
print(f"'{favorite_language.strip()}'")