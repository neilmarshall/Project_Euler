
using Primes

function pe_146(limit::Int64=150000000, remainder_limit::Int64=11)

  # establish some inital empty collections
  solutions = Array{Int64, 1}()
  remainders = []

  # define get_mods function
  function get_mods(p)
    mods = []
    for r in 0:p-1
      if all([(r^2 + a) % p != 0 for a in [1, 3, 7, 9, 13, 27]])
        push!(mods, r)
      end
    end
    return mods
  end

  # observe solutions mod product of initial primes must take certain values
  for r = 0:prod(primes(remainder_limit)) - 1
    if all([r % p in get_mods(p) for p in primes(remainder_limit)])
      push!(remainders, r)
    end
  end

  # define is_solution function
  function is_solution(n)
    mods = []
    for a = 1:27
      if isprime(n^2 + a)
        push!(mods, a)
      end
    end
    return mods == [1, 3, 7, 9, 13, 27]
  end

  # determine eligible candidates and check if they are solutions
  for n = 0:10:limit
    if n % (prod(primes(remainder_limit))) in remainders
      if is_solution(n)
        println(n)
        push!(solutions, n)
      end
    end
  end
  solutions = sum(solutions)
  println("Sum: $solutions")
end

@time pe_146(150000000, 13)

# note: solution for n = 150000000 is 676333270
# note: current fastest time if 253 seconds
