# List - ordered (indexed) collection of items - mutable - can have duplicates

# Dictionary (dict) - collection of  items - mutable - unordered - not indexed
# keyed - key/ value pairs - key cannot have duplicates

person1 = {
    "name": "Matt",
    "Last_name": "Flynn",
    "age": 20
}

print(person1["age"])
print(person1.get("name"))
print(person1.get("uo"))
print(person1.get("uo", "keynotfound"))

person1["address"] = {"State": "VIC", "PostCode":3000}
print(person1["address"]["PostCode"])

person1.update({"name" : "kate"}), {"age" : 36}, {"height" : 160}
print(person1)

for key ,val in person1.items():
    print(f"key: {key}")
    print(f"Value: {val}")
