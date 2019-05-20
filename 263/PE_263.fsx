#! /usr/bin/env fsharpi

open System

let IsPractical n =

    let GetDivisors n =
        let limit = int(Math.Sqrt(float n))
        {1..limit}
        |> Seq.filter (fun x -> n % x = 0)
        |> Seq.map (fun x -> [x; n / x])
        |> Seq.concat
        |> Seq.sort
        |> Seq.distinct
        |> List.ofSeq

    let rec IsSumOfDistinctDivisors divisors p =
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

    if n % 2 = 0 then
        Seq.forall (IsSumOfDistinctDivisors (GetDivisors n)) {1..n}
    else
        n = 1


let IsPrime n =
    let limit = int(Math.Sqrt(float n))
    {2..limit} |> Seq.forall (fun p -> n % p <> 0) && n > 1


let IsSexyPair n =
    [n; n + 6] |> List.forall IsPrime


let IsTriplePair n =
    [n; n + 6; n + 12] |> List.forall IsSexyPair


let IsPracticalQuadruplet n =
    [n + 1; n + 5; n + 9; n + 13; n + 17] |> List.forall IsPractical


let IsEngineersParadise n =
    if n % 1000 = 0 then printfn "%d" n
    IsTriplePair n && IsPracticalQuadruplet n

// Seq.find IsEngineersParadise (Seq.initInfinite (fun idx -> idx)) |> printfn "%d"
// Seq.take 4 (Seq.filter IsEngineersParadise (Seq.initInfinite (fun idx -> idx))) |> printfn "%A"

(*
11
    --> (11, 17), (17, 23), (23, 29)
    --> (12, 16, 20, 24, 28)
*)
