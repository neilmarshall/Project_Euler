#! /usr/bin/env fsharpi
(*
In the game of darts a player throws three darts at a target board which is split
into twenty equal sized sections numbered one to twenty.

The score of a dart is determined by the number of the region that the dart lands
in. A dart landing outside the red/green outer ring scores zero. The black and
cream regions inside this ring represent single scores. However, the red/green
outer ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region, or
bulls-eye. The outer bull is worth 25 points and the inner bull is a double,
worth 50 points.

There are many variations of rules but in the most popular game the players will
begin with a score 301 or 501 and the first player to reduce their running total
to zero is a winner. However, it is normal to play a "doubles out" system, which
means that the player must land a double (including the double bulls-eye at the
centre of the board) on their final dart to win; any other dart that would reduce
their running total to one or lower means the score for that set of three darts
is "bust".

When a player is able to finish on their current score it is called a "checkout"
and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

    D3
    D1 D2
    S2 D2
    D2 D1
    S4 D1
    S1 S1 D2
    S1 T1 D1
    S1 S3 D1
    D1 D1 D1
    D1 S2 D1
    S2 S2 D1 

Note that D1 D2 is considered different to D2 D1 as they finish on different
doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for
example, D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?

Solution: 38182
*)
type Multiplier = Single | Double | Triple
type Value = Value of int
type Dart = Dart of Multiplier * Value
type Checkout = SingleCheckout of Dart | DoubleCheckout of Dart * Dart | TripleCheckout of Dart * Dart * Dart

let count_checkouts =

    let darts =
        let singles = [for n in 1..20 do yield Dart (Single, Value n)]
        let doubles = [for n in 1..20 do yield Dart (Double, Value n)]
        let trebles = [for n in 1..20 do yield Dart (Triple, Value n)]
        let bullseyes = [Dart (Single, Value 25); Dart (Double, Value 25)]
        singles @ doubles @ trebles @ bullseyes

    let checkouts =

        let doubles = darts |> List.filter (fun (Dart (d, _)) -> d = Double)

        let pairs =
            seq {
                for d1 in darts do
                    let darts' = List.filter (fun d2 -> d2 >= d1) darts
                    for d2 in darts' do
                        yield DoubleCheckout (d1, d2) }
            |> List.ofSeq

        let singleCheckouts = [for d in doubles do yield SingleCheckout d]

        let doubleCheckouts = seq { for dart in darts do
                                        for double in doubles do
                                            yield DoubleCheckout (dart, double) } |> List.ofSeq

        let tripleCheckouts = seq { for pair in pairs do
                                        match pair with
                                        | DoubleCheckout (c1, c2) ->
                                            for double in doubles do
                                                yield TripleCheckout (c1, c2, double)
                                        | _ -> failwith "invalid parameter" } |> List.ofSeq

        singleCheckouts @ doubleCheckouts @ tripleCheckouts

    let scoreCheckout (checkout : Checkout) =
        let scoreDart = function
            | Dart (Single, Value v) -> 1 * v
            | Dart (Double, Value v) -> 2 * v
            | Dart (Triple, Value v) -> 3 * v
        match checkout with
        | SingleCheckout d1 -> scoreDart d1
        | DoubleCheckout (d1, d2) -> scoreDart d1 + scoreDart d2
        | TripleCheckout (d1, d2, d3) -> scoreDart d1 + scoreDart d2 + scoreDart d3

    checkouts
    |> List.map scoreCheckout
    |> List.filter (fun score -> score < 100)
    |> List.length


count_checkouts |> printfn "%d"
