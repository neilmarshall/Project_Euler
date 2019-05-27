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
    {1..limit}
    |> Seq.filter (fun n ->
        seq [n; n + 6; n + 12; n + 18]
        |> Seq.forall (fun n -> Set.contains n primes))


let IsPracticalSecondAttempt n =

    let GetDivisors n =
        let limit = int(Math.Sqrt(float n))
        {1..limit}
        |> Seq.filter (fun x -> n % x = 0)
        |> Seq.map (fun x -> [x; n / x])
        |> Seq.concat
        |> Seq.sort
        |> Seq.distinct
        |> List.ofSeq

    let divisors = GetDivisors n
    //printfn "%A" divisors

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

    //if List.length divisors < int(System.Math.Log(float n, 2.0)) then
        //false
    //else
    let head::tail = divisors
    let knownSums = LimitedSubsetSums [head] tail
    //printfn "%A" knownSums
    List.length knownSums = n


let IsPractical verbose n =

    let GetDivisors n =
        if verbose then printfn "getting divisors..."
        let limit = int(Math.Sqrt(float n))
        {1..limit}
        |> Seq.filter (fun x -> n % x = 0)
        |> Seq.map (fun x -> [x; n / x])
        |> Seq.concat
        |> Seq.sort
        |> Seq.distinct
        |> List.ofSeq

    let rec IsSumOfDistinctDivisors divisors p =
        if verbose then printfn "calculating if is sum of divisors > %d" p
        //if verbose then printfn "calculating if is sum of divisors > %d, %A" p divisors
        match divisors with
        | [] -> false
        | [head] -> head = p
        | head::tail ->
            if p < head then
                false
            else if Set.contains p (Set.ofList divisors) then
                true
            else
                if IsSumOfDistinctDivisors tail (p - head) then
                    true
                else
                    IsSumOfDistinctDivisors tail p

    //if n % 2 = 0 then
    Seq.forall (IsSumOfDistinctDivisors (GetDivisors n)) {1..n}
    //else
        //n = 1


let IsPrime n =
    let limit = int(Math.Sqrt(float n))
    {2..limit} |> Seq.forall (fun p -> n % p <> 0) && n > 1


let IsSexyPair n =
    [n; n + 6] |> List.forall IsPrime


let IsTriplePair n =
    [n; n + 6; n + 12] |> List.forall IsSexyPair


let IsPracticalQuadruplet n =
    printfn "%d" n
    let result = [n + 1; n + 5; n + 9; n + 13; n + 17] |> List.forall IsPracticalSecondAttempt
    if result then
        printfn "result found: %d" n
        result
    else
        result


let IsEngineersParadise n =
    //if n % 1000 = 0 then printfn "%d" n
    printfn "%d" n
    IsTriplePair n && IsPracticalQuadruplet n

// Seq.find IsEngineersParadise (Seq.initInfinite (fun idx -> idx)) |> printfn "%d"
// Seq.take 4 (Seq.filter IsEngineersParadise (Seq.initInfinite (fun idx -> idx))) |> printfn "%A"

(*
11
    --> (11, 17), (17, 23), (23, 29)
    --> (12, 16, 20, 24, 28)
*)

FilterTriplePairs 200 |> printfn "%A"
//FilterTriplePairs 50000 |> Seq.toList |> printfn "%A"
IsPractical true 14741 |> printfn "14741: %A"
//IsPractical true 14742 |> printfn "14741: %A"
IsPracticalSecondAttempt 6 |> printfn "6: %A"
IsPracticalSecondAttempt 7 |> printfn "7: %A"
IsPracticalSecondAttempt 8 |> printfn "8: %A"
IsPracticalSecondAttempt 9 |> printfn "9: %A"
IsPracticalSecondAttempt 12 |> printfn "12: %A"
IsPracticalSecondAttempt 14742 |> printfn "14742: %A"
500000 |> FilterTriplePairs |> Seq.filter IsPracticalQuadruplet |> Seq.toList |> printfn "%A"
