source_file="i.txt"
output_file="o.txt"

with open(source_file, "r") as f:
    content = f.read()

rev_content=content[::-1]

with open(output_file, "w+") as f:
    f.write(rev_content)

print("Helllowwwwww")