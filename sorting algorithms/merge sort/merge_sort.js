function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
    let sortedArray = [];
    let l = 0, r = 0;

    while (l < left.length && r < right.length) {
        if (left[l] < right[r]) {
            sortedArray.push(left[l]);
            l++;
        } else {
            sortedArray.push(right[r]);
            r++;
        }
    }

    return sortedArray.concat(left.slice(l)).concat(right.slice(r));
}

// Example usage:
const arr = [12, 11, 13, 5, 6, 7];
const sortedArr = mergeSort(arr);
console.log("Sorted array is:", sortedArr);
