//   The following iterative sequence is defined for the set of positive integers:
//
//       n → n / 2 (n is even)
//       n → 3 * n + 1 (n is odd)
//
//   Using the rule above and starting with 13, we generate the following sequence:
//
//       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
//
//   It can be seen that this sequence (starting at 13 and finishing at 1) contains
//   10 terms. Although it has not been proved yet (Collatz Problem), it is thought
//   that all starting numbers finish at 1.
//
//   Which starting number, under one million, produces the longest chain?
//
//   NOTE: Once the chain starts the terms are allowed to go above one million.
//
//   Solution: 837799

namespace ProjectEuler

module PE14 =
    let rec collatz (n : uint64) =
        match n with
        | 1UL -> 1UL
        | n when n % 2UL = 0UL -> 1UL + collatz (n / 2UL)
        | _ -> 1UL + collatz (3UL * n + 1UL)
    
    [<EntryPoint>]
    let mains args =
        printfn "%d" (seq {1UL..1000000UL} |> Seq.maxBy collatz)
        0 // return code
