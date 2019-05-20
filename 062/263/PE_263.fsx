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

[1..12] |> List.map IsPractical |> List.iter (printfn "%A")
