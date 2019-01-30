#! /usr/bin/env fsharpi

// A common security method used for online banking is to ask the user for
// three random characters from a passcode. For example, if the passcode was 
// 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
// reply would be: 317.
//
// The text file, keylog.txt, contains fifty successful login attempts.
//
// Given that the three characters are always asked for in order, analyse the 
// file so as to determine the shortest possible secret passcode of unknown 
// length.
//
// Solution: 73162890


open System
open System.IO

// read in data
let data = Array.toList(File.ReadAllLines("p079_keylog.txt"))


let getFirstCharacter (data : string list) =

    // count occurrences of indexes where characters appear
    let distinctChars = data |> String.Concat |> Seq.distinct |> Seq.sort |> Seq.toList
    let countIndexes ch =
        List.countBy (Seq.tryFindIndex (fun x -> x = ch))
        >> List.filter (fun x -> Option.isSome(fst x))
    let indexCounts = distinctChars |> List.map (fun ch -> ch, countIndexes ch data)

    // determine first character in data, given index counts
    let firstCharacter =
        let isFirstCharacter indexCount =
            let counts = snd indexCount
            if List.length counts = 1
                then Option.get(fst counts.[0]) = 0
                else false
        indexCounts |> List.find isFirstCharacter |> fst

    // remove first character and subsequently empty strings from the data
    let removeCharacter ch =
        List.map (fun (str : string) -> str.Replace(string ch, ""))
        >> List.filter (fun str -> str <> "")
    let data = removeCharacter firstCharacter data

    // return first character and updated data, so that problem can be
    // solved recusively
    firstCharacter, data


let rec solve data knownCharacters = 
    match data with
    | [] -> int(String.Concat(List.map string knownCharacters))
    | data ->
        let firstCharacter, data = getFirstCharacter data
        let knownCharacters = knownCharacters @ [firstCharacter]
        solve data knownCharacters


printfn "%A" (solve data [])
