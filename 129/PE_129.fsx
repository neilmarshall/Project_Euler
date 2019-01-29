#! /usr/bin/env fsharpi

// A number consisting entirely of ones is called a repunit. We shall define
// R(k) to be a repunit of length k; for example, R(6) = 111111.
// 
// Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that
// there always exists a value, k, for which R(k) is divisible by n, and let
// A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.
// 
// The least value of n for which A(n) first exceeds ten is 17.
// 
// Find the least value of n for which A(n) first exceeds one-million.
//
// Solution: 1000023

// -----------------------

let rec PE129 n =
    let A n =
        let rec f k r a =
            if ((r % n) <> (n - 1))
                then f (k + 1) ((r + a) % n) ((10 * a) % n)
                else k
        f 2 (10 % n) ((10 * (10 % n)) % n)
    if n % 5 <> 0 && A(n) >= 1000000 then n else PE129 (n + 2)

PE129 1000001 |> printfn "%d"
