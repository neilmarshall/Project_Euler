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

    let divisors = GetDivisors n

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

    Seq.forall (IsSumOfDistinctDivisors divisors) {1..n}


let IsPrime n =
    let limit = int(Math.Sqrt(float n))
    {2..limit} |> Seq.forall (fun p -> n % p <> 0) && n > 1


let IsSexyPair n =
    [n; n+ 6] |> List.forall IsPrime


let IsTriplePair n =
    [n; n + 6; n + 12] |> List.forall IsPrime


let IsPracticalQuadruplet n =
    [n + 1; n + 5; n + 9; n + 13; n + 17] |> List.forall IsPractical

[1..12] |> List.map IsPractical |> List.iter (printfn "%A")
[1..12] |> List.map IsPrime |> List.zip [1..12] |> List.iter (printfn "%A")
[19..25] |> List.map IsSexyPair |> List.iter (printfn "%A")
