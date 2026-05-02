import copy

print("\n===== DICTIONARY OPERATIONS =====")

student = {
    "name": "Akil",
    "age": 22,
    "marks": 85
}

# Accessing
print("\nAccessing Values:")
print(student["name"])
print(student.get("age"))

# Adding / Updating
print("\nAdding / Updating:")
student["city"] = "Chennai"
student["marks"] = 90
print(student)

# Deleting
print("\nDeleting:")
removed = student.pop("age")
print("Removed:", removed)
print(student)

# Checking key
print("\nChecking Key:")
print("name" in student)

# Length
print("\nLength of dictionary:")
print(len(student))


# ===============================
print("\n===== DICTIONARY METHODS =====")

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("\nLooping through dictionary:")
for k, v in student.items():
    print(k, ":", v)

# update()
print("\nUsing update():")
student.update({"age": 23, "country": "India"})
print(student)

# setdefault()
print("\nUsing setdefault():")
student.setdefault("grade", "A")
print(student)

# popitem()
print("\nUsing popitem():")
item = student.popitem()
print("Removed item:", item)
print(student)


# ===============================
print("\n===== ALIASING =====")

a = {"x": 1, "y": 2}
b = a   # aliasing

print("Before change:")
print("a:", a)
print("b:", b)

b["x"] = 100

print("\nAfter modifying b:")
print("a:", a)
print("b:", b)


# ===============================
print("\n===== SHALLOW COPY =====")

a = {"x": 1, "y": 2}
b = a.copy()

print("Before change:")
print("a:", a)
print("b:", b)

b["x"] = 200

print("\nAfter modifying b:")
print("a:", a)
print("b:", b)


# ===============================
print("\n===== SHALLOW COPY (NESTED ISSUE) =====")

a = {"data": [1, 2, 3]}
b = a.copy()

b["data"][0] = 999

print("a:", a)
print("b:", b)


# ===============================
print("\n===== DEEP COPY =====")

a = {"data": [1, 2, 3]}
b = copy.deepcopy(a)

b["data"][0] = 555

print("a:", a)
print("b:", b)


# ===============================
print("\n===== FINAL SUMMARY =====")

print("""
Aliasing:
    Same object reference → changes affect both

Shallow Copy:
    New object → but nested objects shared

Deep Copy:
    Fully independent → no shared references
""")