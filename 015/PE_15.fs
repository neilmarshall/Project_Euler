namespace ProjectEuler

open System.Collections.Generic

module PE15 =
    let rec binomialCoefficient n r =
        let memoizer = Dictionary<System.Int64 * System.Int64, System.Int64>()
        let rec Coefficient n r =
            match memoizer.TryGetValue((n, r)) with
            | (true, value) ->
                value
            | _ ->
                let value =
                    match (n, r) with
                    | (n, 0L) ->
                        1L
                    | (n, r) when n = r ->
                        1L
                    | (n, 1L) ->
                        n
                    | (n, r) when n = r + 1L ->
                        n
                    | (n, r) when r > n / 2L ->
                        Coefficient n (n - r)
                    | (n, r) ->
                        (Coefficient (n - 1L) (r - 1L)) + (Coefficient (n - 1L) r)
                memoizer.Add((n, r), value)
                value
        Coefficient n r

    [<EntryPoint>]
    let main args =
        printfn "%d" (binomialCoefficient 40L 20L)
        0  // return code
