# Tower of Hanoi

## Introduction

The Tower of Hanoi is a classic algorithmic problem involving three rods and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks neatly stacked in ascending order of size on one rod, the smallest at the top, making a conical shape.

## Problem Statement

The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.

## My initial thoughts and observations

- This problem is best solved using a recursive technique. The base case occurs when there is only one disk, which can be moved directly to the target rod.
- With two disks, the smaller disk is moved to the auxiliary rod, the larger disk is moved to the target rod, and then the smaller disk is placed on top of the larger disk on the target rod.
- With three disks, the first two disks are moved to the auxiliary rod, the third (largest) disk is moved to the target rod, and then the first two disks are moved from the auxiliary rod to the target rod.
- Generalizing this pattern, for n disks, n-1 disks are first moved to the auxiliary rod, then the nth (largest) disk is moved to the target rod, and finally, the n-1 disks are moved from the auxiliary rod to the target rod.
- After moving the nth disk to the target rod, the auxiliary rod effectively becomes the source rod for the remaining n-1 disks, and the original source rod becomes the new auxiliary rod. This process continues recursively until the base case is reached.


## Algorithm

The algorithm to solve the Tower of Hanoi problem can be described recursively:

1. Move `n-1` disks from source rod to auxiliary rod.
2. Move the `nth` disk from source rod to target rod.
3. Move the `n-1` disks from auxiliary rod to target rod.

### Pseudocode

```plaintext
procedure TowerOfHanoi(n, source, target, auxiliary):
    if n == 1:
        print "Move disk 1 from", source, "to", target
        return
    TowerOfHanoi(n - 1, source, auxiliary, target)
    print "Move disk", n, "from", source, "to", target
    TowerOfHanoi(n - 1, auxiliary, target, source)