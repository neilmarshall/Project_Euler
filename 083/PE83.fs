// ===============
// Problem outline
// ===============

    // Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K
    // text file containing a 80 by 80 matrix, from the top left to the bottom right by moving
    // left, right, up, and down.

// SOLUTION: 425185

// ====================
// Djikstra's Algorithm
// ====================

    // Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

    // Assign to every node a tentative distance value: set it to zero for our initial node and to
    // infinity for all other nodes. Set the initial node as current.

    // For the current node, consider all of its unvisited neighbors and calculate their tentative
    // distances through the current node. Compare the newly calculated tentative distance to the
    // current assigned value and assign the smaller one. For example, if the current node A is
    // marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then
    // the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance
    // greater than 8 then change it to 8. Otherwise, keep the current value.

    // When we are done considering all of the unvisited neighbors of the current node, mark the
    // current node as visited and remove it from the unvisited set. A visited node will never be
    // checked again.

    // If the destination node has been marked visited (when planning a route between two specific
    // nodes) or if the smallest tentative distance among the nodes in the unvisited set is
    // infinity (when planning a complete traversal; occurs when there is no connection between
    // the initial node and remaining unvisited nodes), then stop. The algorithm has finished.

    // Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
    // set it as the new "current node", and go back to step 3.

module Djikstra =

    type Node = Node of int * int

    /// convert list of distances (indexed by position) to map of
    /// distances indexed by Node
    let graphAsMap =
        List.mapi (fun i x -> List.mapi (fun j y -> (Node(i + 1, j + 1), float y)) x)
        >> List.concat
        >> Map.ofList

    /// return map of <Node, distance>, where distance is infinity for all
    /// nodes except startNode, where distance is taken from graph
    let generateInitialDistances startNode n graph =
        [for x in [1..n] -> [for y in [1..n] -> (Node(x, y), infinity)]]
        |> List.concat
        |> Map.ofList
        |> Map.add startNode (Map.find startNode graph)

    /// return set of unvisited nodes, which will initially be all
    /// nodes except startNode
    let generateInitialUnvisitedNodes startNode n =
        [for i in [1..n] -> [for j in [1..n] -> Node(i, j)]]
        |> List.concat
        |> Set.ofList
        |> Set.remove startNode

    /// return set of unvisited neighbours for a given node, which
    /// will be all nodes that lie above, below, to the left or to
    /// the right of the given node
    let getUnvisitedNeighbours unvisitedNodes (Node (x, y)) =
        let isNeighbour (Node(i, j)) =
            (abs(x - i) = 1 && y = j) || (abs(y - j) = 1 && x = i)
        Set.filter isNeighbour unvisitedNodes

    /// update the <Node, distance> map to add the distance betwen
    /// the current node and all of its (unvisited) neighbours
    let updateDistances graph currentNode distances nodesToUpdate =
        let updateDistance distances node =
            let currentDistance = Map.find node distances
            let tentativeDistance = Map.find currentNode distances + Map.find node graph
            let newDistance = List.min [currentDistance; tentativeDistance]
            distances |> Map.add node newDistance
        nodesToUpdate |> Set.fold updateDistance distances

    /// identify next node to visit as unvisited node with minimum distance
    let getNextNode unvisitedNodes distances =
        unvisitedNodes
        |> Set.toList
        |> List.minBy (fun node -> Map.find node distances)

    /// recursive function to solve problem
    let rec recursiveSolve graph currentNode endNode distances unvisitedNodes =
        if unvisitedNodes |> Set.contains endNode then
            let unvisitedNeighbours =
                getUnvisitedNeighbours unvisitedNodes currentNode
            let distances = updateDistances graph currentNode distances unvisitedNeighbours
            let nextNode = getNextNode unvisitedNodes distances
            let unvisitedNodes = Set.remove nextNode unvisitedNodes
            recursiveSolve graph nextNode endNode distances unvisitedNodes
        else
            Map.find endNode distances |> int

    /// entry function to set up bindings and call recursive solution
    let solve graph =
        let n = List.length graph
        let startNode, endNode = Node(1, 1), Node(n, n)
        let graph = graphAsMap graph
        let distances = generateInitialDistances startNode n graph
        let unvisitedNodes = generateInitialUnvisitedNodes startNode n
        recursiveSolve graph startNode endNode distances unvisitedNodes


module PE83 =

    [<EntryPoint>]
    let Main args =

        let graph = [[131; 673; 234; 103; 18];
                     [201; 96; 342; 965; 150];
                     [630; 803; 746; 422; 111];
                     [537; 699; 497; 121; 956];
                     [805; 732; 524; 37; 331]]

        printfn "%d" (Djikstra.solve graph)  // should return 2297
        0  // return code
