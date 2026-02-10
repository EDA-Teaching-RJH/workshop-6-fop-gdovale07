sample_bay = ["basalt","silica","iron","dust"]

print(sample_bay[0])

print(sample_bay[-1])

print(len(sample_bay))

for sample in sample_bay:
    print(f"transmitting data for: {sample}")

new_findings = []

for _ in range(3):
    rock = input("enter rock type:")
    new_findings.append(rock)
print(new_findings)

if "dust" in sample_bay:
    sample_bay.remove("dust")

print(sample_bay)