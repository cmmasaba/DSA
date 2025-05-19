package main

// Optimization 1: Consider the total amount of gas available and the
// total cost of going around the circuit. If the sum of all the gas
// is less than the sum of all the cost, it's impossible to complete
// the circuit regardless of the stating point.
//
// Optimization 2: Imagin we stat at some point and begin our journey.
// If at some point our gas level becomes negative, it means the
// starting point we chose was not a valid one. In addition, any station
// between our initial starting point and the point where the gas became
// negativeis also invalid because if we started at any of those intermediate
// point we would have ended up with negative gas level sooner

func canCompleteCircuit(gas []int, cost []int) int {
    var startingIndex, totalGas, currentGas int

    for i := range gas {
        currentGas += gas[i] - cost[i]
        totalGas += gas[i] - cost[i]

        if currentGas < 0 {
            startingIndex = i + 1
            currentGas = 0
        }
    }

    if totalGas < 0 {
        return -1
    }

    return startingIndex
}