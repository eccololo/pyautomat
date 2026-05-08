from pathlib import Path


p1 = Path("./exercises/files/ghi.txt")

if not p1.exists():
    with open(p1, "w") as file:
        file.write("Content 3")
else:
    print("This file doesn't exists.")


print(p1.name)
print(p1.stem)
print(p1.suffix)


p2 = Path("./exercises/files/")

for i in p2.iterdir():
    print(i)