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
8260

>>> solve(8)
14108

>>> solve(9)
28433

Total: 58885
*)

open System

let pow = Math.Pow

let solve (n : float) : int =
    let infer (p : float) (a : float) = (pow(10.0, n) * a) / (p * a - pow(10.0, n))
    let solve_for_a (a : float) : int =
        let mutable solutions = 0
        let mutable p = Math.Floor(pow(10.0, n) / a) + 1.0
        let mutable b = infer p a
        while b >= a do
            if Math.Abs(Math.Floor(b) - b) <= System.Double.Epsilon then
                solutions <- solutions + 1
            p <- p + 1.0
            b <- infer p a
        solutions
    let mutable a = 1.0
    let mutable solutions = 0
    let rec increment() =
        solutions <- solutions + solve_for_a a
        a <- a + 1.0
        let p = Math.Floor(pow(10.0, n) / a) + 1.0
        let b = infer p a
        if b < a then solutions else increment()
    increment()

[1.0 .. 9.0] |> List.iter (fun n -> printfn "%d: %d" (n |> int) (solve n))
