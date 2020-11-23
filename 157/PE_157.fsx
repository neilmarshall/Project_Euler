(*
Solutions:
    1 -    20
    2 -   102
    3 -   356
    4 -   958
    5 -  2192
    6 -  4456
    7 -  8260
    8 - 14088
    9 - 23058
-------------
Total - 53490
-------------
*)

let solve n =
    let pow x y = System.Math.Pow(x, y)
    let n' = float(n)
    let solve' (a : int64) : int =
        let mutable pmin, pmax = ceil((pow 10.0 n') / float a) |> int64, floor(2.0 * (pow 10.0 n') / float a) |> int64
        if pmin * a = int64(pow 10.0 n') then pmin <- pmin + 1L
        { pmin .. pmax }
        |> Seq.map (fun p -> if (a * int64((pow 10.0 n'))) % (p * a - int64((pow 10.0 n'))) = 0L then 1 else 0)
        |> Seq.sum
    let solutions = { 1L .. (2L * int64(pow 10.0 n')) } |> Seq.map solve' |> Seq.sum
    System.Console.WriteLine(sprintf "%d: %d" n solutions)  // thread-safe compared with printfn
    solutions

[|1 .. 9|] |> Array.Parallel.map solve |> Array.sum |> printfn "%A"
