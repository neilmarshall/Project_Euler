(* function that returns prime factors of a given number *)
let rec factorise n =
    let rec check_factor n known_factors factor_to_check =
        if factor_to_check = n then
            known_factors @ [n]
        else
            if n % factor_to_check = 0UL then
                check_factor (n / factor_to_check) (known_factors @ [factor_to_check]) 2UL
            else
                check_factor n known_factors (factor_to_check + 1UL)
    check_factor n [] 2UL

printfn "Factors of %d: %A" 600851475143UL (factorise 600851475143UL)
