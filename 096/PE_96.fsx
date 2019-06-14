(*
A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in order
to eliminate options (there is much contested opinion over this). The complexity
of the search determines the difficulty of the puzzle.

The 6K text file, p096_sudoku.txt contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions.

By solving all fifty puzzles find the sum of the 3-digit numbers found in the
top left corner of each solution grid.

Solution: 24702
*)

type CellValue = | KnownValue of int | PotentialValues of int list

type Cell = { value : CellValue; row : int; column : int; grid : int } with

    member this.IsSolved =
        match this.value with
        | KnownValue _ -> true
        | PotentialValues _ -> false

    member this.ExtractKnownValue =
        match this.value with
        | KnownValue value -> value
        | _ -> failwith "cell value error"

    member this.ExtractPotentialValues =
        match this.value with
        | PotentialValues values -> values
        | _ -> failwith "cell value error"

let isSolved = fun (c : Cell) -> c.IsSolved
let extractKnownValue = fun (c : Cell) -> c.ExtractKnownValue
let extractPotentialValues = fun (c : Cell) -> c.ExtractPotentialValues

let (|Solved|Unsolved|Unsolvable|) grid =
    let checkCells cells =
        cells |> List.map extractKnownValue |> List.sort = [1..9]
    let checkSolution grouper =
        List.groupBy grouper >> List.map (fun (_, cells) -> cells) >> List.forall checkCells
    if List.forall isSolved grid then
        if (checkSolution (fun c -> c.row) grid) &&
           (checkSolution (fun c -> c.column) grid) &&
           (checkSolution (fun c -> c.grid) grid)
            then Solved
            else Unsolvable
    else
        if grid |> List.filter (isSolved >> not) |> List.map extractPotentialValues |> List.exists (fun v -> v = [])
            then Unsolvable
            else Unsolved
    
let rec solvePuzzle grid =
    let guessSolution grid =
        let firstUnknownCell = List.find (isSolved >> not) grid
        let newGrid testValue =
            grid
            |> List.map (fun cell ->
                if cell = firstUnknownCell then { cell with value = KnownValue testValue } else cell)
        let rec attempt testValues =
            match testValues with
            | [] -> None
            | head::tail ->
                match solvePuzzle (newGrid head) with
                | Some grid -> Some grid
                | None -> attempt tail
        firstUnknownCell.ExtractPotentialValues |> attempt
    let rec reduceGrid grid =
        let eliminateValuesFromCell grid cell =
            let convertValuesToCellValues values =
                match values with
                | head::[] -> KnownValue head
                | _ -> PotentialValues values
            let valuesToEliminate = 
                grid
                |> List.filter isSolved
                |> List.filter (fun c -> c.row = cell.row || c.column = cell.column || c.grid = cell.grid)
                |> List.map extractKnownValue
                |> Set.ofList
            let newPotentialValues =
                Set.difference (Set.ofList cell.ExtractPotentialValues) valuesToEliminate
                |> Set.toList
                |> List.sort
                |> convertValuesToCellValues
            { cell with value = newPotentialValues }
        let grid' =
            grid
            |> List.map (fun cell ->
                match cell.value with
                | KnownValue _ -> cell
                | PotentialValues _ -> eliminateValuesFromCell grid cell)
        if grid' = grid then grid' else reduceGrid grid'
    let grid' = reduceGrid grid
    match grid' with
    | Solved -> Some grid'
    | Unsolvable -> None
    | Unsolved -> guessSolution grid'


// read data, parse as puzzles, solve puzzles and combine answers into final solution to problem
let rec parseStringAsGrids (data : string []) =
    let parseString = Seq.map string >> Seq.map System.Int32.Parse >> Seq.toList
    seq {
        if Array.length data % 10 <> 0 then failwith "bad data input"
        if not (Array.isEmpty data) then
            yield data |> Array.skip 1 |> Array.take 9 |> Array.map parseString |> List.ofArray
            yield! Array.skip 10 data |> parseStringAsGrids
    }

let convertPuzzle puzzle =
    let getGrid row column =
        let rowIndex = (row * 3 + 1) / 9
        let columnIndex = (column * 3 + 1) / 9
        3 * rowIndex + columnIndex
    let convertColumn row column n =
        match n with
        | 0 -> { value = PotentialValues [1..9]; row = row; column = column; grid = getGrid row column }
        | n -> { value = KnownValue n; row = row; column = column; grid = getGrid row column }
    let convertRow row columns =
        columns |> List.mapi (fun column n -> convertColumn row column n)
    puzzle |> List.mapi convertRow |> List.concat

let parseSolution grid =
    List.take 3 grid
    |> List.map extractKnownValue
    |> List.map string
    |> List.reduce (+)
    |> System.Int32.Parse

System.IO.File.ReadAllLines("p096_sudoku.txt")
|> parseStringAsGrids
|> Seq.map convertPuzzle
|> Seq.choose solvePuzzle
|> Seq.map parseSolution
|> Seq.sum
|> printfn "%d"
