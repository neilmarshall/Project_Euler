(*
for target t:
    for p = 2 ... t:
        yield from p, f(t / p)

i.e. for t = 10:
    2, ...f(5) -> 2, (2, ...f(2), (3, ...f(1)), (4, ...f(1)), (5, ...f(1)) -> 
    3, ...f(3)
    4, ...f(2)
    5, ...f(2)
    10, ...f(1)
*)

let rec generateCompoundNumbers limit =
    if limit <= 1 then
        Seq.empty
    else
        seq {
            for p in 2..limit do
                yield [p]
                let tail = generateCompoundNumbers (limit / p)
                for t in tail do
                    yield p::t
        }

let rec digitalRoot n =
    if n < 10 then
        n
    else
        n |> string |> Seq.map string |> Seq.map int |> Seq.sum |> digitalRoot

let buildDigitalRootMap limit =
    let compoundNumbers = generateCompoundNumbers limit
    let accumulator acc c =
        let k = c |> Seq.reduce (*)
        let v = c |> Seq.map digitalRoot |> Seq.sum
        Map.add k (if Map.containsKey k acc then max v (Map.find k acc) else v) acc
    Seq.fold accumulator Map.empty compoundNumbers

let digitalRootSum n =
    let digitalRoots = buildDigitalRootMap n
    digitalRoots |> Map.toSeq |> Seq.map snd |> Seq.sum

//generateCompoundNumbers 10 |> Seq.toList |> printfn "%A"
//printfn "digital root 24 - %d; digital root 8 - %d; digital root 139 - %d" (digitalRoot 24) (digitalRoot 8) (digitalRoot 139)
//buildDigitalRootMap 24 |> Seq.toList |> printfn "%A"
digitalRootSum 1000000 |> printfn "%A"
