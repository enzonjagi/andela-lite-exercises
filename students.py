from datetime import datetime

current_year = datetime.now().year


student = {
    "name":["Amos", "Ndungo"],
    "date-of-birth": 1998,
    "phone number":"0791018694",
}

full_name = student.get("name")
last_name = full_name[1]
year_of_birth = student.get("date-of-birth")
age = current_year - year_of_birth
print (last_name)
print (full_name[0], full_name[1])
print (student.get("phone number"))
print (year_of_birth)
print (age)
