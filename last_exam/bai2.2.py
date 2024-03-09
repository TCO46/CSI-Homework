def tower_of_hanoi(n, source, temp, destination):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return

    tower_of_hanoi(n-1, source, destination, temp)
    print(f"Move disk {n} from source {source} to destination {destination}")
    tower_of_hanoi(n-1, temp, source, destination)


tower_of_hanoi(3, "A", "B", "C")
