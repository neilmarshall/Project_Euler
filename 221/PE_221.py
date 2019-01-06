#! /usr/bin/env python3.7
"""
We shall call a positive integer A an "Alexandrian integer", if there exist
integers p, q, r such that:

    A = p . q . r, and 1 / A = 1 / p + 1 / q + 1 / r

For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18). In fact,
630 is the 6th Alexandrian integer, the first 6 Alexandrian integers being:

    6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.

Solution: 1884161251122450
"""

function main(l)
  A = Array{Float64}(0)
  p = 0
  q = 0
  r = 0
  curMax = 0
  println("Initialising array...")
  while length(A) <= l
  	r += 1
  	p = -(r + 1)
  	while (p^2 + 2 * p * r - 1) < 0
  		q = (1 - p * r) / (p + r)
  		if floor(q) == q
  			push!(A, p * q * r)
      end
  		p -= 1
    end
  end
  A = sort(A)
  curMax = A[length(A)]
  println("Calculating further results...")
  while r * (r + 1) * (r + 2) < curMax
  	r += 1
  	p = -(r + 1)
  	while (p^2 + 2 * p * r - 1) < 0
  		q = (1 - p * r) / (p + r)
  		if floor(q) == q
        if p * q * r < curMax
          pop!(A)
    			push!(A, p * q * r)
          A = sort(A)
          curMax = A[l]
          println(Int64(curMax))
        end
      end
  		p -= 1
    end
  end
  println("Finished...")
  return A
end

l = 150000
A = [Int64(a) for a in main(l)]
println(A[l])
