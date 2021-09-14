contacts = {
    "number":4,
    "students":
    [
        {"name":"Sarah Holderness", "email":"sarah@example.com"},
        {"name":"Scatman John", "email":"scatman@example.com"},
        {"name":"Masterchief", "email":"mc@example.com"},
        {"name":"Hugh Mongous", "email":"hugh@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])