module MR
    type MillerRabin() =

        let getPrimes (limit : uint64) : seq<uint64> =
            let flags = seq { yield [| false; false |]; yield [| for _ in 2UL..limit -> true |] } |> Array.concat
            for p in 2UL..uint64(sqrt(float(limit))) do
                for q in 2UL..(limit / p) do
                    flags.[int(p) * int(q)] <- false
            seq { for p, flag in Seq.zip {0UL..limit} flags do if flag then p }

        let known = getPrimes 5000UL |> Seq.toArray

        let millerRabinReduction n =

            let factorisePowersOfTwo n =
                let mutable s, m, d = 0, n - 1UL, 0UL
                while m % 2UL = 0UL do
                    s <- s + 1
                    m <- m >>> 1
                d <- n >>> s
                uint64(s), d

            let rec witnessReduction s d witnesses =
                let pow (x : uint64) (y : uint64) = float(x)**float(y) |> uint64   
                let powmod b e m =
                    if m = 1UL then
                        0UL
                    else
                        let mutable c = 1UL
                        for p in  0UL .. (e - 1UL) do
                            c <- (c * b) % m
                        c
                match witnesses with
                | [] ->
                    true
                | a::tail ->
                    if powmod a d n <> 1UL then
                        if Seq.exists (fun r -> powmod a ((pow 2UL r) * d) n = n - 1UL) {0UL .. s - 1UL}
                            then witnessReduction s d tail
                            else false
                    else
                        witnessReduction s d tail

            if Seq.exists (fun p -> n % p = 0UL) known then  // perform trial division based on initial primes
                Seq.contains n known
            else  // test compositeness using Miller-Rabin algorithm, with suitable witnesses
                let s, d = factorisePowersOfTwo n
                let witnesses =
                    match n with
                    | n when n < 2047UL -> [2UL]
                    | n when n < 1373653UL -> [2UL; 3UL]
                    | n when n < 9080191UL -> [31UL; 73UL]
                    | n when n < 25326001UL -> [2UL; 3UL; 5UL]
                    | n when n < 3215031751UL -> [2UL; 3UL; 5UL; 7UL]
                    | n when n < 4759123141UL -> [2UL; 7UL; 61UL]
                    | n when n < 1122004669633UL -> [2UL; 13UL; 23UL; 1662803UL]
                    | n when n < 2152302898747UL -> [2UL; 3UL; 5UL; 7UL; 11UL]
                    | n when n < 3474749660383UL -> [2UL; 3UL; 5UL; 7UL; 11UL; 13UL]
                    | n when n < 341550071728321UL -> [2UL; 3UL; 5UL; 7UL; 11UL; 13UL; 17UL]
                    | n when n < 3825123056546413051UL -> [2UL; 3UL; 5UL; 7UL; 11UL; 13UL; 17UL; 19UL; 23UL]
                    | _ -> sprintf "Value of n too high :: %d" n |> failwith
                witnessReduction s d witnesses

        member this.IsPrime(n) =
            if n <= 2UL || n % 2UL = 0UL then n = 2UL else millerRabinReduction n


    (*
    let trivialPrime n =
        if n <= 2 then n = 2 else {2..int(sqrt(float(n)))} |> Seq.forall(fun p -> n % p <> 0)
    let mr = MillerRabin()
    *)

    //for n in 1..20 do printfn "%d: %b" n (trivialPrime n)
    //for n in 1UL..20UL do printfn "%d: %b" n (mr.IsPrime(n))

    (*
    let trivial = [1 .. 10000000] |> List.map trivialPrime
    let millerrabin = [1UL .. 10000000UL] |> List.map (fun n -> mr.IsPrime(n))
    printfn "%b" (trivial = millerrabin)
    *)

    (*
    #time
    for n in 1..100000 do
        if trivialPrime(n) then ()
    #time
    #time
    for n in 1UL..100000UL do
         if mr.IsPrime(uint64(n)) then ()
    #time
    *)

    //printfn "%b" <| mr.IsPrime(5003UL)
