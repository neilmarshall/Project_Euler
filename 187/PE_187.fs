(* function that returns primes up to a given number using
   the "sieve of Eratosthenes" algorithm *)
let prime_sieve n =
    let update_composites p composites =
        let multiples_of_p = [for q in [1 .. n] do yield q % p = 0 && q <> p]
        [for a, b in List.zip multiples_of_p composites do yield a || b]
    let rec generate_composites p composites =
        match p with
        | p when p > n / 2 -> composites
        | p -> generate_composites (p + 1) (update_composites p composites)
    let get_composites = 
        generate_composites 2 (true :: [for p in [2..n] do yield false])
    [for number, is_composite in List.zip [1..n] get_composites do
        if not is_composite then yield number]


let main n =
    let primes = prime_sieve (n / 2)
    let primes_less_than_root_n = List.filter (fun x -> float x <= sqrt (float n)) primes
    let composite_product_counts p = List.filter (fun x -> x >= p && x <= n / p) primes |> List.length
    primes_less_than_root_n |> List.map composite_product_counts |> List.sum


printfn "%d" (main 100000000)
