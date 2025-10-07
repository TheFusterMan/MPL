function NumberProcessor(n) {
    let limit = n;
    let totalSum = 0;

    let evenCount = 0;

    for (let i = 0; i < limit; i++) {
        if (i % 2 == 0) {
            console.log("Found an even number: " + i);
            totalSum += i;
            evenCount += 1;
        }
        else {
            console.log("Found an odd number: " + i);
        }
    }

    if (evenCount > 5) {
        console.log("There were many even numbers!");
    }

    return totalSum;
}

function NumberProcessor(n) {
    let limit = n;
    let totalSum = 0;

    let evenCount = 0;

    for (let i = 0; i < limit; i++) {
        if (i % 2 == 0) {
            console.log("Found an even number: " + i);
            totalSum += i;
            evenCount += 1;
        }
        else {
            console.log("Found an odd number: " + i);
        }
    }

    if (evenCount > 5) {
        console.log("There were many even numbers!");
    }

    return totalSum;
}