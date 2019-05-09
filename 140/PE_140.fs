(*
Consider the infinite polynomial series AG(x) = x.G1 + x^2.G2 + x^3.G3 + ..., where Gk is
the kth term of the second order recurrence relation Gk = Gk−1 + Gk−2, G1 = 1 and G2 = 4; that
is, 1, 4, 5, 9, 14, 23, ...

For this problem we shall be concerned with values of x for which AG(x) is a positive integer.

The corresponding values of x for the first five natural numbers are shown below.
        x        AG(x)
    (√5−1)/4      1
    2/5           2
    (√22−2)/6     3
    (√137−5)/14   4
    1/2           5

We shall call AG(x) a golden nugget if x is rational, because they become increasingly
rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.

Solution: 5673835352990
*)

[<EntryPoint>]
let main argv =
    let rec generateInitialSolution n baseSolution =
        if List.length baseSolution < n then
            let newEntry = List.rev baseSolution |> (fun (lst : int64 List) -> lst.[0] + lst.[1])
            baseSolution @ [newEntry] |> generateInitialSolution  n
        else
            baseSolution

    let F n =
        if n = 1 then [1L]
        elif n = 2 then [1L; 1L]
        else generateInitialSolution n [1L; 1L]

    let G n =
        if n = 1 then [1L]
        elif n = 2 then [1L; 4L]
        else generateInitialSolution n [1L; 4L]


    let rec solveSolution limit baseSolution =
        let Fn = F (2 * limit)
        let Gn = G (2 * limit)
        let rec recLoop baseSolution =
            if List.length baseSolution < limit then
                let n = baseSolution.Length + 2
                let evenSolution = Gn.[2 * n  - 2] + List.last baseSolution
                let fibonnaciOffset = Fn.[2 * n  - 1]
                let oddSolution = evenSolution - fibonnaciOffset
                baseSolution @ [oddSolution; evenSolution] |> recLoop
            else
                baseSolution
        recLoop baseSolution
        
    solveSolution 30 [2L; 5L] |> List.sum |> printfn "%d"

    0 // return an integer exit code
