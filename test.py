def move_position(x, y, direction):
    match direction:
        case "east":
            x += 1
        case "west":
            x -= 1
        case "north":
            y += 1
        case "south":
            y -= 1
        case _:
            raise ValueError("Invalid direction")
    return x, y


print("Testing valid directions:")
x, y = 0, 0

x, y = move_position(x, y, "east")
print(f"After moving east: x: {x}, y: {y}")

x, y = move_position(x, y, "north")
print(f"After moving north: x: {x}, y: {y}")

x, y = move_position(x, y, "west")
print(f"After moving west: x: {x}, y: {y}")

x, y = move_position(x, y, "south")
print(f"After moving south: x: {x}, y: {y}")

print("\nTesting multiple moves:")
x, y = 0, 0
directions = ["east", "east", "north", "west", "south"]

for direction in directions:
    x, y = move_position(x, y, direction)
    print(f"After moving {direction}: x: {x}, y: {y}")

print("\nTesting invalid direction:")
try:
    x, y = move_position(0, 0, "northeast")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    x, y = move_position(0, 0, "up")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    x, y = move_position(0, 0, 123)
except ValueError as e:
    print(f"ValueError: {e}")
