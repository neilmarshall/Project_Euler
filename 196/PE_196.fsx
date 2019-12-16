(*
Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37.

You are given that S(10000)=950007619.

Find  S(5678027) + S(7208785).
*)

#load "./miller_rabin.fsx"

module PE196 =

    let private triangle n = n * (n - 1UL) / 2UL

    let private getRow n =
        let t = triangle n
        [|t + 1UL .. t + n|]

    type private PrimeChecker() =
        let mr = MR.MillerRabin()

        let isPrime n = {2UL..uint64(sqrt(float(n)))} |> Seq.forall (fun p -> n % p <> 0UL)

        let known = System.Collections.Generic.Dictionary<uint64, bool>()

        member this.Check n =
            //if known.ContainsKey(n) |> not then known.Add(n, isPrime n)
            //known.[n]
            //isPrime n
            mr.IsPrime(n)

    let private getNeighbours (pc : PrimeChecker) row n =
        let lowerBound = 1UL + triangle row
        let upperBound = row + triangle row
        if n < lowerBound || n > upperBound then failwith "invalid arguments"
        let previousRowLowerBound = 1UL + triangle (row - 1UL)
        let previousRowUpperBound = lowerBound - 1UL
        let subsequentRowLowerBound = upperBound + 1UL
        let subsequentRowUpperBound = subsequentRowLowerBound + row
        let neighbours = seq {
            // previous row
            let t = n - row
            if t >= previousRowLowerBound && t <= previousRowUpperBound then yield t, row - 1UL
            let t = n - row + 1UL
            if t >= previousRowLowerBound && t <= previousRowUpperBound then yield t, row - 1UL
            let t = n - row + 2UL
            if t >= previousRowLowerBound && t <= previousRowUpperBound then yield t, row - 1UL

            // current row
            let t = n - 1UL
            if t >= lowerBound && t <= upperBound then yield t, row
            let t = n + 1UL
            if t >= lowerBound && t <= upperBound then yield t, row

            // subsequent row
            let t = n + row - 1UL
            if t >= subsequentRowLowerBound && t <= subsequentRowUpperBound then yield t, row + 1UL
            let t = n + row
            if t >= subsequentRowLowerBound && t <= subsequentRowUpperBound then yield t, row + 1UL
            let t = n + row + 1UL
            if t >= subsequentRowLowerBound && t <= subsequentRowUpperBound then yield t, row + 1UL
        }
        neighbours |> Seq.filter (fun (t, _) -> pc.Check(t))

    let private isPrimeTriplet (pc : PrimeChecker) row n =
        if pc.Check(n) then
            let neighbours = getNeighbours pc row n |> Seq.toList
            if neighbours.Length = 0 then
                false
            else if neighbours.Length >= 2 then
                true
            else
                let extendedNeighbours =
                    seq {
                        for neighbour, row in neighbours do
                            yield! (getNeighbours pc row neighbour) }
                Seq.length extendedNeighbours >= 2
        else
            false

    let private solveRow (pc : PrimeChecker) row =
        //row
        //|> getRow
        //|> List.map (isPrimeTriplet pc row)
        //|> List.zip (getRow row)
        //|> List.filter (fun (_, flag) -> flag)
        //|> List.map fst
        //|> List.sum
        row
        |> getRow
        |> Array.Parallel.map (isPrimeTriplet pc row)
        |> Array.zip (getRow row)
        |> Array.filter (fun (_, flag) -> flag)
        |> Array.sumBy fst

    let solveRowNoChecker row =
        let pc = PrimeChecker()
        solveRow pc row

    let getPrimeTriplets range =
        let pc = PrimeChecker()
        for row in range do
            let row' = getRow row
            for n in row' do
                let flag = isPrimeTriplet pc row n
                if (pc.Check(n)) then printfn "%d, %d, %b" row n flag

//[1UL..20UL] |> List.map PE196.solveRowNoChecker |> printfn "%A"
10000UL |> PE196.solveRowNoChecker |> printfn "%A"  // 950007619L - c. <<< 1 second
//100000UL |> PE196.solveRowNoChecker |> printfn "%A"  // 549999566882L - c. 6 seconds
//1000000UL |> PE196.solveRowNoChecker |> printfn "%A"  // 463999977061648L - c. 8 minutes 43 seconds (2 minutes 21 seconds if use Array.Parallel...)
//5678027UL |> PE196.solveRowNoChecker |> printfn "%A"
//7208785UL |> PE196.solveRowNoChecker |> printfn "%A"
