# Format this name dictionary into 'Last, First M.' format:
# Expected: "Smith, John R."

name = {
    "first": "John",
    "middle": "Robert",
    "last": "Smith"
}


print(name["last"] + "," + name["first"] + "," + name["middle"][0]+ ".")


