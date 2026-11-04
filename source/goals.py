# Goal -> list of (item id, note). Notes: "partial: ...", "", ""
W5, W6, W7, W9, EX = "Week 5", "Week 6", "Week 7", "Week 9", "Lectures 15–16 (not on goals sheet)"
G = []
def g(n, week, text, star, items, gtitle=None): G.append(dict(n=n, week=week, text=text, star=star, items=items))

g(1,W5,"State the definitions of upper bound, lower bound, bounded set, supremum, infimum, maximum, and minimum.",True,
 [("L9.D21",""),("L9.R1",""),("L9.D22",""),("L9.P21",""),("L9.D23",""),("HW6.2",""),("P8.1",""),("P8.2",""),("ET9.2","partial: what inf A = sup A forces"),("PA.1e",""),("PB.1b",""),("PB.1c","")])
g(2,W5,"Determine whether a set is bounded above or below, and whether it has a supremum, infimum, maximum, or minimum.",True,
 [("L9.E21",""),("L9.E22",""),("L9.R2",""),("L9.R3",""),("L10.E11",""),("L10.R1",""),("HW5.3",""),("HW6.3",""),("P9.3",""),("ET9.1",""),("ET9.2",""),("PA.2","")])
g(3,W5,"Distinguish between supremum and maximum, and between infimum and minimum.",True,
 [("L9.R2",""),("L9.R3",""),("L9.D23",""),("L10.R1",""),("HW6.2",""),("HW5.3","partial: max vs sup for each set"),("P8.2",""),("P9.3",""),("ET9.1",""),("ET10.2",""),("PA.1e",""),("PB.1b",""),("PB.1c","")])
g(4,W5,"Prove that a given number is the supremum or infimum of a set using the definitions.",True,
 [("L9.E21",""),("L9.E22",""),("L10.P11",""),("L10.E11",""),("HW5.3",""),("HW6.2",""),("HW6.3",""),("ET10.1",""),("ET9.1","partial"),("PA.2","")])
g(5,W5,"State and apply the completeness axiom of R.",True,
 [("L9.D24",""),("L9.D25",""),("L9.R4",""),("L9.R5",""),("L9.T23",""),("L9.CA",""),("L9.T24",""),("L9.R8",""),("L10.T31","partial: applies completeness"),("HW6.4b",""),("HW6.4c",""),("ET9.3",""),("PA.1a",""),("PA.1b","")])
g(6,W5,"Explain why Q is not complete and understand what this means in terms of existence of suprema.",True,
 [("L9.T21",""),("L9.R6",""),("L9.T22",""),("L9.R8",""),("HW5.3b","partial: rational set, irrational sup"),("P8.4",""),("PA.1b",""),("PB.3a","partial: uses irrationality of √2")])
g(7,W5,"Recognize R as the unique complete ordered field up to isomorphism.",False,
 [("L9.T23",""),("L9.R7","")])
g(8,W5,"State and prove properties of suprema and infima, including their behavior under set inclusion and unions.",True,
 [("HW5.1a",""),("HW5.1c",""),("HW5.2a",""),("HW5.2b",""),("PB.2a",""),("PA.3a","partial: comparing sups"),("PA.3b","partial: comparing sups")])
g(9,W6,"State, prove, and apply the ε-characterization of the supremum and infimum. Interpret and use statements involving nested quantifiers.",True,
 [("L10.P21",""),("L10.GM",""),("L10.R1",""),("L10.R2",""),("L10.R3",""),("L10.T32","partial: 'write it with quantifiers'"),("HW5.1b",""),("HW8.5",""),("HW9.6b","partial: quantifier order"),("P9.1",""),("P9.2",""),("P9.4",""),("P10.1",""),("ET10.3",""),("ET10.2","partial: sup approximated by elements"),("PA.1c",""),("PA.3a",""),("PB.1a","compare with 2A 1(c): quantifiers swapped"),("PB.2b","")])
g(10,W6,"Prove statements involving inequalities that hold for every ε > 0.",True,
 [("L10.P41",""),("L10.X41",""),("L14.T41","partial: uses this fact"),("HW6.1",""),("PA.1c",""),("PA.3b",""),("PB.1a",""),("PB.2b","")])
g(11,W6,"State and prove that N is unbounded above in R, and state and apply the Archimedean property and its consequences.",True,
 [("L10.T31",""),("L10.T32",""),("L10.T33",""),("L14.E21","partial: applied"),("HW6.3","partial: via density"),("HW8.2","partial: applied when choosing n₀"),("P9.2",""),("PA.7a","partial: applied"),("PB.7a","partial: applied")])
g(12,W6,"State the integer-part property and use it to prove the density of Q in R.",True,
 [("L10.T41",""),("L10.D41",""),("L10.E41",""),("L10.T42",""),("L10.Q",""),("HW6.3",""),("ET10.4",""),("PB.3a",""),("PB.3b","")])
g(13,W6,"Use completeness to prove the existence of infima for nonempty lower bounded sets.",True,
 [("L9.R5",""),("HW6.4a",""),("HW6.4b",""),("HW6.4c",""),("PA.1a","partial")])
g(14,W6,"Prove properties of suprema and infima under addition and scalar multiplication, including multiplication by negative scalars.",False,
 [("HW6.4d",""),("HW6.4e",""),("HW6.4a","partial: t = −1 case"),("PA.3b","partial: sup B + c")])
g(15,W6,"Define complex numbers as ordered pairs of real numbers, state their field operations, and perform arithmetic operations, including division, writing answers in the form x + iy.",True,
 [("L11.S1",""),("L11.D41",""),("L11.T41",""),("L11.R1",""),("L11.D42",""),("L11.P41",""),("L11.R2",""),("L11.D43",""),("L11.E41",""),("L11.R4",""),("L11.EX",""),("HW6.5",""),("P10.2",""),("P10.4",""),("ET11.1",""),("ET11.2",""),("ET11.3",""),("ET12.1","partial: √ rules fail in C"),("PA.4a","")])
g(16,W6,"Explain what it means that C is an algebraically closed field.",False,
 [("L11.S2",""),("HW7.6a","partial: roots of real polynomials")])
g(17,W6,"Explain why C cannot be made into an ordered field.",False,
 [("L11.P42",""),("P10.3","")])
g(18,W6,"Define complex conjugation and modulus and interpret them geometrically.",True,
 [("L11.D51",""),("L11.D52",""),("L11.R3",""),("L11.R4",""),("HW6.5c",""),("ET12.2","partial: modulus as length"),("PA.1g",""),("PA.1h",""),("PB.4a","")])
g(19,W7,"State and prove the basic properties of complex conjugation and modulus, including their behavior under field operations.",True,
 [("L11.PR",""),("L12.PR",""),("L12.P11",""),("HW7.4b",""),("HW7.6a",""),("HW7.6bc",""),("ET12.2",""),("PA.1g",""),("PA.1h",""),("PB.4a",""),("PB.4b",""),("PB.4c",""),("PB.7d","partial: Re of a limit")])
g(20,W7,"State, prove, and apply the triangle inequality.",True,
 [("L11.PR","partial: (xii) stated"),("L12.PX",""),("L12.TRI",""),("L12.QEQ",""),("L14.E31","partial: applied"),("L14.T41","partial: applied"),("L15.R31",""),("HW7.4a",""),("HW7.4c",""),("HW7.5",""),("P11.3",""),("PB.1g",""),("PB.4b","")])
g(21,W7,"Find the modulus and argument of a complex number and express it in polar form.",True,
 [("L12.D21",""),("L12.R1",""),("L12.R2",""),("L12.E21",""),("L12.X21",""),("L12.E22",""),("HW7.1ab",""),("P11.1","partial"),("ET12.2","partial: z/|z| = cos θ + i sin θ"),("PA.4b",""),("PA.5a","")])
g(22,W7,"Interpret operations with complex numbers geometrically in the complex plane, including addition by the parallelogram rule and multiplication by multiplying moduli and adding arguments.",True,
 [("L12.ADD",""),("L12.TRI",""),("L12.MUL",""),("L12.QI",""),("L12.X31",""),("HW7.1ab","partial: (b)"),("HW7.1c",""),("P11.1",""),("P11.4",""),("ET12.3",""),("PA.4d","")])
g(23,W7,"State and apply De Moivre's formula to compute powers of complex numbers. (Listed twice on the goals sheet.)",True,
 [("L12.DM",""),("L12.E31",""),("L12.X31",""),("HW7.2",""),("HW7.3a",""),("P11.1","partial: product, not powers"),("PA.4c",""),("PA.5b",""),("PB.4d","")])
g(24,W7,"Determine the nth roots of unity and explain their geometric arrangement on the unit circle.",True,
 [("L12.D41",""),("L12.RU",""),("L12.GI",""),("L12.E41",""),("L12.X41",""),("HW7.3bc",""),("P11.2",""),("PA.5b",""),("PA.5c",""),("PB.4d","partial: roots of w, same method")])
g(25,W7,"Define a distance and an open ball.",True,
 [("L13.D21",""),("L13.E21",""),("L13.E22",""),("L13.D22",""),("L13.R21",""),("L13.D23",""),("L13.E24",""),("L13.P21",""),("L13.P22",""),("L13.R22",""),("L13.D24",""),("L13.E25",""),("L13.D25",""),("L13.P23",""),("L13.X21",""),("L13.R23",""),("HW7.5",""),("HW8.1",""),("P12.1",""),("P12.2",""),("P12.3",""),("P12.4",""),("P12.5",""),("ET13.1",""),("ET13.2",""),("ET13.3",""),("PA.6c",""),("PB.1d",""),("PB.1e",""),("PB.1f",""),("PB.5b",""),("PB.5c","")])
g(26,W7,"Interpret open balls geometrically in the complex plane C.",True,
 [("L13.E22",""),("L13.E23",""),("L13.D23","partial: figure"),("L13.E24","partial: (iv) closed disc"),("L13.P23",""),("L13.MAN",""),("L14.R3",""),("HW7.4c","partial: a circle in C"),("HW8.1b",""),("P12.5","partial"),("ET13.2","partial: a ball in R, not C"),("PA.6a",""),("PA.6b",""),("PA.6c",""),("PB.5a","")])
g(27,W7,"Define a norm on a field and verify whether a given function satisfies the norm axioms.",True,
 [("L13.D31",""),("L13.E31",""),("L13.E32",""),("PB.1h","")])
g(28,W7,"Prove that a norm on a field induces a distance.",True,
 [("L13.P31",""),("PA.6c","partial: ρ = 2|z − w|")])
g(29,W7,"Recognize the complex modulus and the real absolute value as examples of norms.",True,
 [("L13.E31",""),("L13.E32",""),("L11.R3",""),("PB.1h","")])
g(30,W7,"State, prove, and apply the basic properties of absolute value, including the triangle inequality.",True,
 [("L13.D11",""),("L13.R11",""),("L13.PR",""),("L13.T11",""),("L15.R31",""),("HW8.4","partial: applied"),("ET13.1","partial: |x − y| as a distance"),("PB.1h",""),("PB.2b","partial: applied")])
g(31,W9,"Define a sequence and construct examples of sequences.",False,
 [("L14.D11",""),("L14.EX",""),("L14.R1",""),("HW8.3","partial: piecewise c_n")])
g(32,W9,"Distinguish a sequence from its range by constructing different sequences with the same range.",False,
 [("L14.D14",""),("L14.R2",""),("HW8.6","partial: uses the range set")])
g(33,W9,"Define the sum, difference, product, and quotient of two sequences, and compute their terms.",False,
 [("L14.D12",""),("L14.D13","")])
g(34,W9,"Define the tail of a sequence and identify tails of given sequences.",False,
 [("L14.D15",""),("L14.R6",""),("ET14.3","partial: removing terms leaves a tail")])
g(35,W9,"State the rigorous definition of convergence using ε and n₀(ε), and illustrate its geometric meaning using balls centered at the limit.",True,
 [("L14.D21",""),("L14.R3",""),("L14.R4",""),("HW8.2",""),("P14.6","partial: instructor's reply explains the ε-ball"),("ET14.1","partial"),("PA.7a",""),("PB.7a","")])
g(36,W9,"Identify the correct order of quantifiers in the definition, explain how n₀(ε) depends on ε, and distinguish the definition from statements obtained by changing the quantifiers.",True,
 [("L14.R3",""),("L14.R4",""),("L10.R3",""),("HW9.6b",""),("PA.1c","partial: compare with 2B 1(a)"),("PB.1a","partial: quantifiers swapped")])
g(37,W9,"Show that aₙ → a is equivalent to having at most finitely many terms outside B(a, ε) for every ε > 0, or equivalently, to having a tail entirely contained in B(a, ε) for every ε > 0.",True,
 [("L14.R5",""),("L14.R6",""),("L14.X31",""),("HW8.4","partial: applied"),("HW8.6","partial: applied"),("P14.1",""),("ET14.1",""),("PA.1f","partial")])
g(38,W9,"Explain why changing finitely many initial terms does not affect convergence or the limit.",False,
 [("L14.R5","partial: implicit"),("L15.T22","partial: discussion after the theorem"),("ET14.3","")])
g(39,W9,"Apply the ε–n₀(ε) proof template to establish convergence of given sequences.",True,
 [("L14.TPL",""),("L14.E21",""),("L14.R7",""),("L14.E22",""),("L14.X21",""),("HW8.2",""),("HW8.3",""),("PA.7a",""),("PB.7a","")])
g(40,W9,"Prove that 1/n → 0 by choosing an appropriate n₀(ε) and verifying the required inequality.",False,
 [("L14.E21",""),("L14.R7",""),("HW8.2a","partial: 1/n³, same method")])
g(41,W9,"Negate the definition of convergence to a given number a by reversing its quantifiers, and state the rigorous definition of divergence.",True,
 [("L14.NEG",""),("L14.D31",""),("L14.X31",""),("ET14.2","partial: counterexample"),("PA.1d","partial"),("PA.7c","partial")])
g(42,W9,"Explain why (−1)ⁿ diverges, without being required to reproduce its full proof.",True,
 [("L14.E31",""),("L14.R8",""),("L15.R13",""),("L16.EX",""),("HW9.1a","partial: (−i)ⁿ"),("P14.2","partial: the counterexample"),("ET14.2",""),("PA.7c","")])
g(43,W9,"Prove that a convergent sequence has a unique limit using the triangle inequality.",False,
 [("L14.T41","")])
g(44,W9,"Given aₙ → a, determine whether sets of indices of the form … (cut off on the goals sheet)",False,
 [("L14.R5",""),("L14.X31",""),("HW8.4","partial"),("P14.1",""),("P14.6",""),("ET14.1","partial")])
# Extras
g("A",EX,"Bounded sequences; convergent ⇒ bounded.",True,
 [("L15.D11",""),("L15.R11",""),("L15.T11",""),("L15.R13",""),("HW9.6a",""),("P14.2",""),("P14.3",""),("P14.4",""),("PA.1d",""),("PB.7c","")])
g("B",EX,"Comparison and Squeeze Theorems; bounded × null sequence → 0.",True,
 [("L15.T21",""),("L15.R21",""),("L15.T22",""),("L15.EX",""),("L15.P21",""),("L15.R22",""),("HW9.1bcd",""),("P14.5",""),("P14.6",""),("ET15.1",""),("ET15.3",""),("PA.1d",""),("PA.7b","")])
g("C",EX,"Algebra of limits.",True,
 [("L15.P3X",""),("L15.R31",""),("L15.E31",""),("HW9.1bcd","partial: (d)"),("P14.4",""),("ET15.2",""),("PA.7c",""),("PB.7b",""),("PB.7d","")])
g("D",EX,"Divergence to ±∞.",True,
 [("L15.D41",""),("L15.T41",""),("L15.E41",""),("L16.R12","partial: Remark 1.3"),("HW9.2","partial: (b), (d)"),("PB.6","")])
g("E",EX,"Geometric sequences αⁿ and Bernoulli's inequality.",False,
 [("L16.R11",""),("L16.T11",""),("L16.R12",""),("L16.EX",""),("L16.XR",""),("HW9.1a",""),("HW9.1bcd","partial: (c)")])
g("F",EX,"Basic limits, ratio and root criteria.",False,
 [("L16.P21",""),("L16.P31",""),("L16.R3X",""),("L16.P32",""),("L16.X1",""),("L16.AP",""),("HW9.2",""),("HW9.3","partial: (c)"),("PB.7b","partial: conjugate trick")])
g("G",EX,"Monotone Convergence Theorem and Cauchy sequences (not in Lectures 9–16).",False,
 [("HW9.3",""),("HW9.45",""),("HW9.6a",""),("HW9.6b","")])

RECHECK = {}
