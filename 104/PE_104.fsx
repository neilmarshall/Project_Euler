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

Seq.unfold (fun (n1, n0) -> Some (n1, (n0 + n1, n1))) (1I, 0I)
|> Seq.mapi (fun n f -> (n + 1, isDoublyPandigital(f)))
|> Seq.find snd
|> fst
|> printfn "%A"
