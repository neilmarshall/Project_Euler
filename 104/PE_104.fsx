#! /usr/bin/env fsharpi

// The Fibonacci sequence is defined by the recurrence relation:
//     F(n) = F(n − 1) + F(n − 2), where F(1) = 1 and F(2) = 1.
//
// It turns out that F(541), which contains 113 digits, is the first Fibonacci number
// for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9,
// but not necessarily in order). And F(2749), which contains 575 digits, is the first
// Fibonacci number for which the first nine digits are 1-9 pandigital.
//
// Given that F(k) is the first Fibonacci number for which the first nine digits AND
// the last nine digits are 1-9 pandigital, find k.
//
// Solution: 329468

let fibonacciGenerator =
    seq {
        let mutable n, n0, n1 = 1, 0I, 1I
        while true do
            yield n, n1
            let temp = n1
            n1 <- n0 + n1
            n0 <- temp
            n <- n + 1
    }

let isDoublyPandigital n =
    let isLeadingPandigital (str : string) =
        let leadingString = str.ToCharArray().[0..8] |> Array.sort |> System.String.Concat
        leadingString = "123456789"
    let isTrailingPandigital (str : string) =
        str.ToCharArray() |> Array.rev |> System.String.Concat |> isLeadingPandigital
    let str = n.ToString()
    if str.Length < 9 then
        false
    else
        isLeadingPandigital str && isTrailingPandigital str

Seq.find (fun (n, fib) -> isDoublyPandigital fib) fibonacciGenerator |> fst |> printfn "%d"
