# Basic types
name = "Brenden"
age = 25
skills = ["security", "python", "automation"]
profile = {"name": name, "age": age, "skills": skills}

print("Profile:", profile)

# Conditionals
if age >= 21:
    print("Adult access granted.")
else:
    print("Minor access.")

# Loops and list ops
upper_skills = []
for s in skills:
    upper_skills.append(s.upper())
print("Upper skills:", upper_skills)

# List comprehension
short_skills = [s for s in skills if len(s) <= 7]
print("Short skills:", short_skills)

# Functions
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

print("Average ages example:", average([24, 25, 29]))
