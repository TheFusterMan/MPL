function NumberProcessor(n) {
    console.log("--- Starting NumberProcessor ---");
    console.log("Configuration: Processing numbers up to " + n);
    let limit = n;
    let totalSum = 0;
    let evenCount = 0;
    let oddCount = 0;
    let divisibleByThreeCount = 0;

    console.log("Initializing loop...");
    for (let i = 0; i < limit; i++) {
        console.log("Current number: " + i);
        if (i % 2 == 0) {
            console.log("Found an even number: " + i);
            totalSum += i;
            evenCount += 1;
        } else {
            console.log("Found an odd number: " + i);
            oddCount += 1;
        }
        if (i % 3 == 0) {
            console.log("This number is also divisible by 3.");
            divisibleByThreeCount += 1;
        }
        console.log("...iteration complete.");
    }

    console.log("Loop finished. Analyzing results...");
    if (evenCount > 5) {
        console.log("There were many even numbers!");
    }
    if (oddCount > evenCount) {
        console.log("Odd numbers were more frequent.");
    } else {
        console.log("Even numbers were more or equally frequent.");
    }
    console.log("Total even numbers: " + evenCount);
    console.log("Total odd numbers: " + oddCount);
    console.log("Total numbers divisible by three: " + divisibleByThreeCount);
    console.log("--- NumberProcessor Finished ---");
    return totalSum;
}

function SummationExplorer(limit1, limit2) {
    console.log("--- Starting Summation Explorer ---");
    let totalSum1 = 0;
    let totalSum2 = 0;

    console.log("Stage 1: Calculating first sum up to " + limit1);
    for (let i = 0; i < limit1; i++) {
        totalSum1 += i;
        if (i % 10 == 0) {
            console.log("Sum1 milestone at index " + i + ": " + totalSum1);
        }
    }
    console.log("Stage 1 complete. Final sum1: " + totalSum1);

    console.log("Stage 2: Calculating second sum up to " + limit2);
    for (let k = 0; k < limit2; k++) {
        totalSum2 += k;
        if (k % 20 == 0) {
            console.log("Sum2 milestone at index " + k + ": " + totalSum2);
        }
    }
    console.log("Stage 2 complete. Final sum2: " + totalSum2);

    let finalSum = totalSum1;
    finalSum += totalSum2;

    console.log("Final combined sum: " + finalSum);

    if (finalSum > 2000) {
        console.log("The combined sum is very large!");
    } else {
        console.log("The combined sum is manageable.");
    }
    console.log("--- Summation Explorer Finished ---");
    return finalSum;
}


function ConditionalCounter(max_val) {
    console.log("--- Starting Conditional Counter up to " + max_val + " ---");
    let countA = 0;
    let countB = 0;
    let countC = 0;
    let countD = 0;
    let countE = 0;
    let countF = 0;

    for (let i = 0; i < max_val; i++) {
        console.log("Analyzing number " + i);
        if (i % 2 == 0) {
            console.log("Category: Even");
            countA += 1;
            if (i % 4 == 0) {
                console.log("Sub-category: Divisible by 4");
                countB += 1;
                if (i % 8 == 0) {
                    console.log("Sub-sub-category: Divisible by 8");
                    countF += 1;
                }
            } else {
                console.log("Sub-category: Even but not divisible by 4");
                countC += 1;
            }
        } else {
            console.log("Category: Odd");
            countD += 1;
            if (i % 3 == 0) {
                console.log("Sub-category: Odd and divisible by 3");
                countE += 1;
            }
        }
        console.log("...analysis for " + i + " done.");
    }
    console.log("--- Final Counts ---");
    console.log("Count A (div by 2): " + countA);
    console.log("Count B (div by 4): " + countB);
    console.log("Count C (even, not div by 4): " + countC);
    console.log("Count D (odd): " + countD);
    console.log("Count E (odd, div by 3): " + countE);
    console.log("Count F (div by 8): " + countF);
    console.log("--- Conditional Counter Finished ---");
    return countA;
}

function PatternPrinter(size) {
    console.log("--- Printing a Pattern of size " + size + " ---");
    let total_prints = 0;
    for (let i = 0; i < size; i++) {
        console.log("--- Printing Row " + i + " ---");
        for (let j = 0; j < size; j++) {
            console.log("Pos (" + i + ", " + j + ")");
            total_prints += 1;
        }
        console.log("--- End of Row " + i + " ---");
    }
    console.log("Total positions printed: " + total_prints);
    console.log("--- Pattern Printing Complete ---");
    return total_prints;
}

function VerboseLoop(iterations) {
    console.log("--- Starting Verbose Loop for " + iterations + " iterations ---");
    let counter = 0;
    let check_point = 0;
    for (let i = 0; i < iterations; i++) {
        console.log("Iteration " + i + " is starting now.");
        counter += 1;
        console.log("The main counter is now: " + counter);
        if (i % 2 == 0) {
            console.log("This is an EVEN iteration number.");
            check_point += 1;
        } else {
            console.log("This is an ODD iteration number.");
            check_point += 2;
        }
        console.log("Performing some dummy work...");
        console.log("... more dummy work ...");
        console.log("Internal checkpoint value is: " + check_point);
        console.log("Iteration " + i + " has finished.");
        console.log("========================================");
    }
    console.log("--- Verbose Loop Finished ---");
    return counter;
}

function subProcessA(val) {
    console.log("Sub-process A starting with " + val);
    let result = 0;
    let limit = 10;
    console.log("Sub-process loop will run " + limit + " times.");
    for (let i = 0; i < limit; i++) {
        console.log("Sub A loop " + i);
        result += val;
    }
    console.log("Sub-process A finished with result: " + result);
    return result;
}

function subProcessB(val) {
    console.log("Sub-process B starting with " + val);
    let result = val;
    if (val > 500) {
        console.log("Value is large, adding a large bonus.");
        result += 100;
    } else {
        console.log("Value is small, adding a smaller bonus.");
        result += 10;
    }
    console.log("Sub-process B finished with result: " + result);
    return result;
}

function MultiStageProcessor(initialValue) {
    console.log("--- Starting Multi-Stage Processor ---");
    console.log("Initial value: " + initialValue);

    console.log("--- STAGE 1: Calling Sub-Process A ---");
    let stage1_result = subProcessA(initialValue);
    console.log("Result after Stage 1: " + stage1_result);

    if (stage1_result > 100) {
        console.log("Stage 1 result is significant. Proceeding to Stage 2.");
    } else {
        console.log("Stage 1 result is minor. Stage 2 will have less work.");
    }

    console.log("--- STAGE 2: Calling Sub-Process B ---");
    let stage2_result = subProcessB(stage1_result);
    console.log("Result after Stage 2: " + stage2_result);

    console.log("--- Multi-Stage Processor Finished ---");
    return stage2_result;
}

function runAllProcesses() {
    console.log("<<<<<<<<<< STARTING FULL SIMULATION >>>>>>>>>>");
    let grandTotal = 0;

    console.log("\n\n--- Step 1: Running NumberProcessor ---");
    let res1 = NumberProcessor(25);
    console.log("NumberProcessor returned: " + res1);
    grandTotal += res1;

    console.log("\n\n--- Step 2: Running SummationExplorer ---");
    let res2 = SummationExplorer(40, 60);
    console.log("SummationExplorer returned: " + res2);
    grandTotal += res2;

    console.log("\n\n--- Step 3: Running ConditionalCounter ---");
    let res3 = ConditionalCounter(30);
    console.log("ConditionalCounter returned: " + res3);
    grandTotal += res3;

    console.log("\n\n--- Step 4: Running PatternPrinter ---");
    let res4 = PatternPrinter(4);
    console.log("PatternPrinter returned: " + res4);
    grandTotal += res4;

    console.log("\n\n--- Step 5: Running VerboseLoop ---");
    let res5 = VerboseLoop(5);
    console.log("VerboseLoop returned: " + res5);
    grandTotal += res5;

    console.log("\n\n--- Step 6: Running MultiStageProcessor ---");
    let res6 = MultiStageProcessor(15);
    console.log("MultiStageProcessor returned: " + res6);
    grandTotal += res6;

    console.log("\n\n--- FINAL TALLY OF ALL RESULTS ---");
    console.log("The grand total of all returned values is: " + grandTotal);

    if (grandTotal > 5000) {
        console.log("SIMULATION RESULT: HIGH ACTIVITY");
    } else {
        console.log("SIMULATION RESULT: NORMAL ACTIVITY");
    }

    console.log("<<<<<<<<<< SIMULATION FINISHED >>>>>>>>>>");
    return grandTotal;
}


function helperFunctionOne(limit) {
    console.log("--- Starting Helper Function One ---");
    let sum_a = 0;
    let sum_b = 0;
    console.log("Processing up to limit: " + limit);
    for (let i = 0; i < limit; i++) {
        if (i % 2 == 0) {
            console.log("Even branch: " + i);
            sum_a += i;
        } else {
            console.log("Odd branch: " + i);
            sum_b += i;
        }
    }
    console.log("Helper one sum of evens (a): " + sum_a);
    console.log("Helper one sum of odds (b): " + sum_b);
    console.log("--- Helper Function One Finished ---");
    return sum_a;
}

function helperFunctionTwo(some_number) {
    console.log("--- Starting Helper Function Two ---");
    let result = 0;
    result += some_number;
    result += some_number;
    console.log("Helper two doubled the number: " + result);
    if (result > 100) {
        console.log("Helper two received a large number, result is large.");
    } else {
        console.log("Helper two received a small number, result is small.");
    }
    console.log("--- Helper Function Two Finished ---");
    return result;
}


function NumberProcessor(n) {
    let limit = n;
    let totalSum = 0;
    let evenCount = 0;
    console.log("Starting duplicate NumberProcessor for limit: " + n);
    for (let i = 0; i < limit; i++) {
        if (i % 2 == 0) {
            console.log("Duplicate found an even number: " + i);
            totalSum += i;
            evenCount += 1;
        } else {
            console.log("Duplicate found an odd number: " + i);
        }
    }
    console.log("Duplicate loop finished.");
    if (evenCount > 5) {
        console.log("There were many even numbers in the duplicate function too!");
    }
    return totalSum;
}