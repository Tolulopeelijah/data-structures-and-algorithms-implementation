function gcd(a, b) { //the greatest common divisor
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

let a = 56, b = 98;
console.log(`GCD of ${a} and ${b} is ${gcd(a, b)}`);
