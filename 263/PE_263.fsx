#! /usr/bin/env fsharpi

open System

let GetPrimes n =

    let flags = Array.concat [ [| false; false |]; [| for _ in 2..n -> true |] ]
    for p in 2..(int(sqrt(float n))) do
        for q in 2..(n / p) do
            flags.[p * q] <- false
    seq { for i in 2..n do if flags.[i] then yield i }


let FilterTriplePairs limit =
    let primes = GetPrimes limit |> Set.ofSeq
    seq {1..limit}
    |> Seq.filter (fun n -> seq {n .. 6 .. n + 18} |> Seq.forall (fun n -> Set.contains n primes))


let IsPractical n =

    let GetDivisors n =
        let limit = int(sqrt(float n))
        seq {1..limit}
        |> Seq.filter (fun x -> n % x = 0)
        |> Seq.map (fun x -> [x; n / x])
        |> Seq.concat
        |> Seq.sort
        |> Seq.distinct
        |> List.ofSeq

    let divisors = GetDivisors n

    let rec LimitedSubsetSums knownSums divisors =
        let GetNewSums knownSums divisor =
            knownSums
            |> List.filter (fun k -> k + divisor <= n)
            |> List.map (fun k -> k + divisor)
            |> List.append knownSums
            |> List.append [divisor]
            |> List.distinct
            |> List.sort
        match divisors with
        | [] -> knownSums
        | [head] -> GetNewSums knownSums head
        | head::tail -> LimitedSubsetSums (GetNewSums knownSums head) tail

    let head::tail = divisors
    let knownSums = LimitedSubsetSums [head] tail
    List.length knownSums = n


let IsPracticalQuadruplet n =
    //printfn "%d" n
    let result = {n + 1 .. 4 .. n + 17} |> Seq.forall IsPractical
    if result then printfn "\tresult found: %d" n
    result


let GetEngineersParadise limit =
    printfn "%d" limit
    limit
    |> FilterTriplePairs
    |> Seq.filter IsPracticalQuadruplet
    |> Seq.toList


let PE263 =
    let rec GetSolution seed =
        let results = GetEngineersParadise seed
        if List.length results >= 4 then
            Seq.take 4 results |> Seq.toList
        else
            GetSolution (seed * 2)
    GetSolution 1


//1000000 |> FilterTriplePairs |> Seq.filter IsPracticalQuadruplet |> Seq.toList |> printfn "%A"
PE263 |> printfn "%A"
