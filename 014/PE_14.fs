module PE14 =
    let collatz n =
        let collatz_generator s =
            match s with
            | 1 -> None
            | s when s % 2 = 0 -> Some(s, s / 2)
            | _ -> Some(s, 3 * s + 1)
        Seq.unfold collatz_generator n |> Seq.length |> (+) 1
    
    [<EntryPoint>]
    let mains args =
        [1..100] |> Seq.maxBy collatz |> printfn "%d"  // 97
        [1..1_000] |> Seq.maxBy collatz |> printfn "%d"  // 871
        [1..1_000_000] |> Seq.maxBy collatz |> printfn "%d"  // 837799
        0 // return code
