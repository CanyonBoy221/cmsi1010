import sys
move_counter = 0


def move(n, source, destination, auxiliary):
    global move_counter
    if n > 0:
        move(n - 1, source, auxiliary, destination)
        move_counter += 1
        print(
            f"Move {move_counter}: Move disk {n} from {source} to {destination}")
        move(n - 1, auxiliary, destination, source)


try:
    if len(sys.argv) != 2:
        raise ValueError("Exactly one argument is required")
    if not sys.argv[1].isdigit():
        raise ValueError("The argument must be a positive integer")
    number_of_disks = int(sys.argv[1])
    if number_of_disks < 1 or number_of_disks > 20:
        raise ValueError(
            "The argument must be between 1 and 20, inclusive")

    # Reset move counter before starting
    move_counter = 0
    move(number_of_disks, "A", "B", "C")

    # Display total number of moves
    print(f"\nTotal number of moves: {move_counter}")
    print(
        f"Theoretical minimum moves for {number_of_disks} disks: {2**number_of_disks - 1}")

except ValueError as e:
    print(f"Error: {e}")
