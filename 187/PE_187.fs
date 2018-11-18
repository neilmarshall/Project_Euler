let sieve n =
    let flags = Array.concat [ [| false; false |]; [| for _ in 2..n -> true |] ]
    for p in 2..(int(sqrt(float n))) do
        for q in 2..(n / p) do
            flags.[p * q] <- false
    [for i in 2..n do if flags.[i] then yield i]

let PE_187 limit =
    let primes = sieve (limit / 2)
    primes
    |> List.filter (fun x -> x <= int(sqrt(float limit)))
    |> List.map (fun p -> List.filter (fun x -> x >= p && x <= limit / p) primes |> List.length)
    |> List.sum

printfn "%d" (PE_187 100_000_000)