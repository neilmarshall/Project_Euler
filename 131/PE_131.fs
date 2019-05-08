(*
There are some prime values, p, for which there exists a positive integer, n, 
such that the expression n^3 + n^2 * p is a perfect cube. 

For example, when p = 19, 8^3 + 8^2 × 19 = 12^3. 

What is perhaps most surprising is that for each prime with this property the 
value of n is unique, and there are only four such primes below one-hundred. 

How many primes below one million have this remarkable property? 

Solution: 173 
*)

open System

let PE_131 limit =
    let getPrimesUpToN n =
        let flags = Array.concat [[|false; false|]; (Array.create (n - 1) true)]
        for p in 2..(n / 2) do
            if flags.[p] then
                for q in 2..(n / p) do
                    flags.[p * q] <- false
        Set.ofSeq(seq {for p in 2..n do if flags.[p] then yield p})
    let primes = getPrimesUpToN limit
    let rec accumulateSolution agg g =
        let x = float g + Math.Pow(float g, 3.0 / 2.0)
        if Math.Floor(x) = x then
            let n = x - float g
            let p = int(Math.Round((Math.Pow(x, 3.0) - Math.Pow(n, 3.0)) / Math.Pow(n, 2.0), 0))
            if p > limit then
                agg
            elif Set.contains p primes then
                accumulateSolution (agg + 1) (g + 1)
            else
                accumulateSolution agg (g + 1)
        else
            accumulateSolution agg (g + 1)
    accumulateSolution 0 1


[<EntryPoint>]
let main argv =
    PE_131 1000000 |> printfn "%d"
    0 // return an integer exit code
