(*
>>> solve(1)
20

>>> solve(2)
102

>>> solve(3)
356

>>> solve(4)
958

>>> solve(5)
2192

>>> solve(6)
4456

>>> solve(7)
8260 --> is this 8230?

>>> solve(8)
14108 --> is this 13361?

>>> solve(9)
28433 --> is this 18520?

Total: 58885
 or [|20; 102; 356; 958; 2192; 4456; 8230; 13361; 18520|] ???
*)

open System
open System.Threading

let WriteLine (s : string) = System.Console.WriteLine(s)
let pow = Math.Pow

let solve (n : int) : int =
    WriteLine(sprintf "Calculating value for %d on thread id %d" (int64 n) (Thread.CurrentThread.ManagedThreadId))
    let solve_for_a (a : int64) : int =
        let mutable pmin = int64(ceil(pow(10.0, float(n)) / (float(a))))
        //let pmax = (int64(pow(10.0, float(n)) / (float(a)))) * 2L
        let pmax = pmin * 2L
        if pmin * a = int64(pow(10.0, float(n))) then
            pmin <- pmin + 1L
        //printfn "a: %d, p-min: %d, p-max: %d" a pmin pmax
        let mutable s = 0
        for p in pmin .. pmax do
            if (a * int64(pow(10.0, float(n)))) % (p * a - int64(pow(10.0, float(n)))) = 0L then
                s <- s + 1
        s
    let mutable solutions = 0
    for a in 1L .. (2L * int64(pow(10.0, float(n)))) do
        solutions <- solutions + solve_for_a a
    WriteLine(sprintf "%d: %d" (n |> int) solutions)
    solutions

[|1 .. 9|] |> Array.Parallel.map solve |> printfn "%A"
