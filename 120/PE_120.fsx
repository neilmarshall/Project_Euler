(*
Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And
as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For 3 ≤ a ≤ 1000, find ∑ r_max.

Solution: 333082500
*)

let calcRMax a =
    let a' = (a * a - 1) / a
    let a'' = if a' % 2 = 0 then a' else a' - 1
    a * a''

[3..1000] |> List.map calcRMax |> List.sum |> printfn "%d"
