def print_triangle(charecter, lines):
    for count in range(1, lines + 1):
        print(charecter * count)

print_triangle(charecter="@", lines=8)
print_triangle(charecter="&", lines=13)
print_triangle(charecter="o", lines=5)
