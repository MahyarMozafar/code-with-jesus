name = "sarah"
print(name.upper())
print(name.title())
print(len(name))

# slicing: counting starts at 0
print(name[0])
print(name[0:3])

# the messy name from the start of the video
print("  sARah  ".strip().title())

# a real example
user = "  SARAH  "
clean = user.strip()
print(clean.lower())
