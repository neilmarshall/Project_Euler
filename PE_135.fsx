// Given the positive integers, x, y, and z, are consecutive terms of an arithmetic
// progression, the least value of the positive integer, n, for which the equation,
// x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:
//
//     34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27
//
// It turns out that n = 1155 is the least value which has exactly ten solutions.
//
// How many values of n less than one million have exactly ten distinct solutions?
//
// Solution: 4989

open System

let PE135 limit numberOfSolutions =
    let countSolutions n =
        seq {1..int(Math.Sqrt(float n))}
        |> Seq.filter(fun d -> n % d = 0)
        |> Seq.map (fun d -> Set.ofList [d; n / d])
        |> Set.unionMany
        |> Set.filter (fun d -> 3 * d > n / d && (d + n / d) % 4 = 0)
        |> Set.count
    [1..limit]
    |> List.filter (fun n -> countSolutions n = numberOfSolutions)
    |> List.length

PE135 1000000 10 |> printfn "%d"