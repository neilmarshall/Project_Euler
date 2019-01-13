#! /usr/bin/env fsharpi

// Find the unique positive integer whose square has the
// form 1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.

// Solution: 1389019170

open System.Text.RegularExpressions

let regex = Regex(@"1\d2\d3\d4\d5\d6\d7\d8\d9\d0")
let seed = 1010101010I  // integer part of sqrt(1020304050607080900)

let rec f n =
    if regex.IsMatch(string(n * n)) then n else f (n + 10I)  // solution must end in '0', so we can increment in units of 10

printfn "%A" (f seed)
