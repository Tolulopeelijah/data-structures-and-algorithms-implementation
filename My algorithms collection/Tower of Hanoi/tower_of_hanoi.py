def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary) #moves n-1 from source to auxiliary
    print(f"Move disk {n} from {source} to {target}") #moves the nth from source to target
    tower_of_hanoi(n - 1, auxiliary, auxiliary, target) #moves the n-1 from auxiliary to target


tower_of_hanoi(3, 'A', 'B', 'C')