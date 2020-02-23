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

let solve (n : float) : int =
    WriteLine(sprintf "Calculating value for %d on thread id %d" (int64 n) (Thread.CurrentThread.ManagedThreadId))
    let infer (p : float) (a : float) = (pow(10.0, n) * a) / (p * a - pow(10.0, n))
    let solve_for_a (a : float) : int =
        let check_solution (b : float) =
            let a, b = int64 a, int64 b
            let scale = int64(pow(10.0, n))
            scale * (a + b) % (a * b) = 0L
        let mutable p = Math.Floor(pow(10.0, n) / a) + 1.0
        let mutable b = infer p a
        let solutions = System.Collections.Generic.HashSet<int64 * int64>()
        while b >= a do
            if check_solution b then
                solutions.Add(int64 a, int64 b) |> ignore
            if check_solution (b + 1.0) then
                solutions.Add(int64 a, int64 (b + 1.0)) |> ignore
            p <- p + 1.0
            b <- infer p a
        Seq.length solutions
    let mutable a = 1.0
    let mutable solutions = 0
    let rec increment() =
        solutions <- solutions + solve_for_a a
        a <- a + 1.0
        let p = Math.Floor(pow(10.0, n) / a) + 1.0
        let b = infer p a
        if b < a then solutions else increment()
    let solutions = increment()
    WriteLine(sprintf "%d: %d" (n |> int) solutions)
    solutions

//[1.0 .. 5.0] |> List.iter (fun n -> printfn "%d: %d" (n |> int) (solve n))
[|1.0 .. 9.0|] |> Array.Parallel.map solve |> printfn "%A"
