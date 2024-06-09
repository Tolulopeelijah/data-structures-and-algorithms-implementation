function towerOfHanoi(n, source, target, auxiliary) {
    if (n === 1) {
        console.log(`Move disk 1 from ${source} to ${target}`);
        return;
    }
    towerOfHanoi(n - 1, source, auxiliary, target);
    console.log(`Move disk ${n} from ${source} to ${target}`);
    towerOfHanoi(n - 1, auxiliary, target, source);
}

// Number of disks
let n = 3;
towerOfHanoi(n, 'A', 'C', 'B'); // A, B and C are names of rods
