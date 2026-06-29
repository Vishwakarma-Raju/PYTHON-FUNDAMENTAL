marks = {
    "key":"value",
    "Raju": 67,
    "Hari": 69,
    "Jojo": 79,
    0 : "Lalu"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Raju":89 , "Babu" :59})
print(marks)

print(marks.get("Bheem")) # Ye None return karega
print(marks["Bheem"]) # Ye error return karega