function towerOfHanoi(n, source, auxiliary, target) {
    if (n === 1) {
        console.log(`Move disk 1 from ${source} to ${target}`);
        return;
    }
    towerOfHanoi(n - 1, source, target, auxiliary); //moves the n-1 disks to auxiliary
    console.log(`Move disk ${n} from ${source} to ${target}`); //moves n to target
    towerOfHanoi(n - 1, auxiliary, source, target); //moves n-1 from auxiliary to target
}

let source = prompt("What will you like to denote source with?");
let auxiliary = prompt("What will you like to denote auxiliary with?");
let target = prompt("What will you like to denote target with?");
let n = parseInt(prompt("How many disks are in the source?"));
towerOfHanoi(n, source, auxiliary, target);
