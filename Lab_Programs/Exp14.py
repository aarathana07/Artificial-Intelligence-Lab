
hours = int(input("Enter study hours: "))

if hours >= 5:
    if hours >= 7:
        result = "Pass with good marks"
    else:
        result = "Pass"
else:
    result = "Fail"

print("Prediction:", result)
