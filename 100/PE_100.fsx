#! /usr/bin/env fsharpi

// If a box contains twenty-one coloured discs, composed of fifteen blue discs 
// and six red discs, and two discs were taken at random, it can be seen that
// the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
//
// The next such arrangement, for which there is exactly 50% chance of taking 
// two blue discs at random, is a box containing eighty-five blue discs and
// thirty-five red discs.
//
// By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
// discs in total, determine the number of blue discs that the box would contain.
//
// Solution: 756872327473

let rec calculate x =
    let limit = 1000000000000.0
    let multiplier = 3.0 + System.Math.Sqrt(8.0)
    let x = System.Math.Round(x * multiplier)
    let B = (1.0 + System.Math.Sqrt((x**2.0 - 1.0) / 2.0 + 1.0)) / 2.0
    let R = ((1.0 - 2.0 * B) + System.Math.Sqrt(8.0 * B**2.0 - B) + 1.0) / 2.0;
    if B + R < limit
        then calculate x
        else uint64 B

printfn "%A" (calculate 7.0)
