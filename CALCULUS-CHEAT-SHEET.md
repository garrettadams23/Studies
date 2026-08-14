# Calculus Cheat Sheet

> **Generated** from `data/math.html` by `tools/gen_cheatsheet.py`.
> Do not edit by hand — run the generator after changing the Math domain.

Every formula here also lives on the site as a flashcard and quiz question. 16 topics, 65 sections.

## Contents

- [Calculus Cheat Sheet — Everything on One Page](#calculus-cheat-sheet-everything-on-one-page) — MATH • Cheat Sheet
- [Unit 1 — Foundations: Functions, Continuity, Vectors & Trig](#unit-1-foundations-functions-continuity-vectors-trig) — MATH • Ch 1–5
- [Unit 2 — Derivatives: Limits, Rules, Graphing & Applications](#unit-2-derivatives-limits-rules-graphing-applications) — MATH • Ch 6–10
- [Unit 3 — Integrals: Series, Area, Techniques & Differential Equations](#unit-3-integrals-series-area-techniques-differential-equations) — MATH • Ch 11–15
- [Chapter Tests & the Final — Where the Marks Actually Go](#chapter-tests-the-final-where-the-marks-actually-go) — MATH • Exam Strategy
- [Logarithms & Exponents — Rules and How to Solve](#logarithms-exponents-rules-and-how-to-solve) — MATH • Formulas
- [Trigonometry — The Unit Circle, Identities & Inverses](#trigonometry-the-unit-circle-identities-inverses) — MATH • Formulas
- [The Two Pictures — Derivative as Slope, Integral as Area](#the-two-pictures-derivative-as-slope-integral-as-area) — MATH • Diagrams
- [Algebra & Geometry Formulas — The Prerequisites](#algebra-geometry-formulas-the-prerequisites) — MATH • Formulas
- [Shape Formulas — Labelled Diagrams](#shape-formulas-labelled-diagrams) — MATH • Formulas
- [TI-84 Plus CE — The Keys That Matter for Calculus](#ti-84-plus-ce-the-keys-that-matter-for-calculus) — MATH • Ch 5 Calculator
- [The Named Theorems — Rolle, MVT, IVT, EVT & Squeeze](#the-named-theorems-rolle-mvt-ivt-evt-squeeze) — MATH • Theorems
- [sin, cos, tan & sec — What They Actually Are](#sin-cos-tan-sec-what-they-actually-are) — MATH • Trig Foundations
- [Implicit Differentiation & Choosing Which Rule First](#implicit-differentiation-choosing-which-rule-first) — MATH • Ch 8 Technique
- [Numerical Integration — Trapezoidal Rule, Midpoint & Simpson's](#numerical-integration-trapezoidal-rule-midpoint-simpsons) — MATH • Ch 12 Approximation
- [Series — Choosing a Test, and Radius of Convergence](#series-choosing-a-test-and-radius-of-convergence) — MATH • Ch 11 Deep

---

## Calculus Cheat Sheet — Everything on One Page

### Rules — Derivatives

| Rule | Formula |
|---|---|
| Definition | f′(x) = lim_h→0 [f(x+h) − f(x)] / h |
| Power | d/dx xⁿ = n·x^(n−1) |
| Product | (fg)′ = f′g + fg′ |
| Quotient | (f/g)′ = (f′g − fg′) / g² — "low d-high minus high d-low, over low squared" |
| Chain | d/dx f(g(x)) = f′(g(x)) · g′(x) |
| Implicit | Differentiate both sides in x, write dy/dx whenever you differentiate a y, then solve for dy/dx |

### The ones to know cold — Derivatives

| f(x) | f′(x) | f(x) | f′(x) |
|---|---|---|---|
| sin x | cos x | eˣ | eˣ |
| cos x | −sin x | aˣ | aˣ · ln a |
| tan x | sec²x | ln x | 1/x |
| sec x | sec x · tan x | log_a x | 1 / (x · ln a) |
| csc x | −csc x · cot x | arcsin x | 1 / √(1 − x²) |
| cot x | −csc²x | arctan x | 1 / (1 + x²) |

Pattern worth noticing: every co-function derivative (cos, csc, cot) carries a minus sign. That one observation halves what you have to memorise.

### Antiderivatives — every one gets + C — Integrals

| ∫ f(x) dx | Result |
|---|---|
| ∫ xⁿ dx | x^(n+1)/(n+1) + C, for n ≠ −1 |
| ∫ (1/x) dx | ln\|x\| + C — the absolute value matters |
| ∫ eˣ dx | eˣ + C |
| ∫ aˣ dx | aˣ/ln a + C |
| ∫ sin x dx | −cos x + C |
| ∫ cos x dx | sin x + C |
| ∫ sec²x dx | tan x + C |
| ∫ sec x tan x dx | sec x + C |
| ∫ tan x dx | ln\|sec x\| + C |
| ∫ sec x dx | ln\|sec x + tan x\| + C |
| ∫ 1/(1 + x²) dx | arctan x + C |
| ∫ 1/√(1 − x²) dx | arcsin x + C |

### The Fundamental Theorem, and the three techniques — Integrals

| Name | Statement / method |
|---|---|
| FTC Part 1 | d/dx ∫_a^(x) f(t) dt = f(x) — differentiation undoes integration |
| FTC Part 2 | ∫_a^(b) f(x) dx = F(b) − F(a), where F′ = f |
| u-substitution | Reverse chain rule. Pick u = the inside function; you need its derivative present (up to a constant). Change the limits when the integral is definite, or convert back before evaluating |
| By parts | ∫ u dv = uv − ∫ v du. Choose u by LIATE: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential — earliest in the list becomes u |
| Partial fractions | For a rational function with the degree of the numerator lower than the denominator: factor the denominator, split into simpler fractions, integrate each. If the degree is not lower, do polynomial long division first |

### Area, volume, length, average — Applications

| Quantity | Formula |
|---|---|
| Area between curves | ∫_a^(b) (top − bottom) dx |
| Volume — disk | V = π ∫_a^(b) [R(x)]² dx |
| Volume — washer | V = π ∫_a^(b) ([R(x)]² − [r(x)]²) dx — outer squared minus inner squared, not the difference squared |
| Volume — shell | V = 2π ∫_a^(b) x · h(x) dx |
| Arc length | L = ∫_a^(b) √(1 + [f′(x)]²) dx |
| Average value | f_avg = 1/(b−a) · ∫_a^(b) f(x) dx |

### Convergence tests and the four Maclaurin series — Series

| Test | Verdict |
|---|---|
| nth-term (divergence) | If lim a_n ≠ 0, it diverges. If the limit is 0, this test says nothing |
| Geometric Σ a·rⁿ | Converges iff \|r\| < 1, to a/(1 − r) |
| p-series Σ 1/n^(p) | Converges iff p > 1. So Σ1/n diverges, Σ1/n² converges |
| Ratio test | L = lim \|a_n+1/a_n\|. L < 1 converges, L > 1 diverges, L = 1 inconclusive |
| Alternating series | Converges if terms decrease in magnitude and tend to 0 |

| Series | Expansion |
|---|---|
| eˣ | Σ xⁿ/n! = 1 + x + x²/2! + x³/3! + … |
| sin x | x − x³/3! + x⁵/5! − … (odd powers) |
| cos x | 1 − x²/2! + x⁴/4! − … (even powers) |
| 1/(1 − x) | 1 + x + x² + x³ + … for \|x\| < 1 |

Taylor series about a: f(x) = Σ f^((n))(a)·(x − a)ⁿ / n!. A Maclaurin series is just the case a = 0.

### Trig identities and limits you will keep needing — Foundations

| Identity |  |
|---|---|
| Pythagorean | sin²θ + cos²θ = 1 \| 1 + tan²θ = sec²θ \| 1 + cot²θ = csc²θ |
| Double angle | sin 2θ = 2 sinθ cosθ \| cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ |
| Special limits | lim_x→0 (sin x)/x = 1 \| lim_x→0 (1 − cos x)/x = 0 |
| L'Hôpital (L'Hopital) | Only for 0/0 or ∞/∞: then lim f/g = lim f′/g′. Check the form every time before applying it |
| Continuity at a | All three: f(a) exists, lim_x→a f(x) exists, and the two are equal |

---

## Unit 1 — Foundations: Functions, Continuity, Vectors & Trig

### Functions, graphs and continuity — Ch 1–2

| Idea | What to hold onto |
|---|---|
| Transformations of f(x) | f(x) + k up · f(x + k) left · a·f(x) vertical stretch · f(ax) horizontal compression by 1/a. Inside the parentheses does the opposite of what it looks like |
| Domain killers | Division by zero, even roots of negatives, logs of non-positives. Almost every "find the domain" question is one of those three |
| Continuity | Value exists, limit exists, they match. A removable discontinuity is a hole; a jump is one-sided limits disagreeing; an infinite one is a vertical asymptote |
| Asymptotes | Vertical where the denominator is 0 and the numerator is not. Horizontal from comparing degrees: bottom-heavy → y = 0, equal → ratio of leading coefficients, top-heavy → none (slant instead) |

### Vectors — Ch 3

| Operation | Formula |
|---|---|
| Magnitude | \|v\| = √(v₁² + v₂² + v₃²) |
| Unit vector | v̂ = v / \|v\| |
| Dot product | a·b = a₁b₁ + a₂b₂ + a₃b₃ = \|a\|\|b\| cos θ — a scalar. Zero means perpendicular |
| Angle between | cos θ = (a·b) / (\|a\|\|b\|) |
| Cross product | a × b — a vector, perpendicular to both. \|a × b\| = \|a\|\|b\| sin θ. Zero means parallel |

The one that gets missed on tests: dot gives a number, cross gives a vector. If your answer has the wrong type, you used the wrong product.

### Trig values, and the calculator trap — Ch 4–5

| θ | 0 | π/6 (30°) | π/4 (45°) | π/3 (60°) | π/2 (90°) |
|---|---|---|---|---|---|
| sin | 0 | 1/2 | √2/2 | √3/2 | 1 |
| cos | 1 | √3/2 | √2/2 | 1/2 | 0 |
| tan | 0 | √3/3 | 1 | √3 | undefined |

Degrees versus radians is the single most common avoidable error in a calculus course. Calculus is done in radians. If your calculator is in degree mode, sin(π) returns about 0.0548 instead of 0. Check the mode indicator before every test — this costs one second and has ended many otherwise-correct attempts.

Two more calculator habits worth building: parenthesise the whole denominator (1/(2+3), never 1/2+3), and remember that −2² is −4 while (−2)² is 4 — the minus sign is not part of the base unless you make it so.

---

## Unit 2 — Derivatives: Limits, Rules, Graphing & Applications

### Evaluating a limit — try these in order — Ch 6

| # | Try | When |
|---|---|---|
| 1 | Substitute. If you get a number, you are done | Always first. Most limits are this easy |
| 2 | Factor and cancel | Substitution gave 0/0 and it is a polynomial or a simple rational |
| 3 | Multiply by the conjugate | 0/0 with a square root in it |
| 4 | Divide by the highest power of x in the denominator | x → ±∞ on a rational function |
| 5 | L'Hôpital / L'Hopital | Confirmed 0/0 or ∞/∞ and the above did not help |

A nonzero number over zero is not indeterminate — it is infinite (check the sign from each side). Only the seven forms 0/0, ∞/∞, 0·∞, ∞−∞, 1^(∞), 0^(0), ∞^(0) are indeterminate.

### What a derivative means, before what it computes — Ch 7–8

A derivative is a rate of change and, geometrically, the slope of the tangent line. Everything in this unit is one of those two readings: f′(a) is the instantaneous rate at a, and the tangent line there is y − f(a) = f′(a)(x − a).

Position → velocity → acceleration is the same fact applied twice: v = s′, a = v′ = s″. Speed is |v|, which is why an object can have negative velocity and increasing speed at the same time.

### Reading a graph off the derivatives — Ch 9

| If… | Then f is… |
|---|---|
| f′ > 0 | increasing |
| f′ < 0 | decreasing |
| f′ = 0 or undefined | at a critical point — a candidate for a max or min, not a guarantee |
| f″ > 0 | concave up (holds water) |
| f″ < 0 | concave down |
| f″ changes sign | inflection point — the sign must actually change, not merely reach zero |

Second derivative test: at a critical point, f″ > 0 means local minimum, f″ < 0 means local maximum, and f″ = 0 tells you nothing — fall back to the first derivative sign chart.

### Optimisation and related rates — the same four steps — Ch 10

```
# OPTIMISATION
1. Draw it. Label what varies with letters.
2. Write the quantity to optimise as an equation.
3. Use a CONSTRAINT to reduce it to ONE variable.
4. Differentiate, set = 0, solve, then test the critical
   points AND the endpoints of the domain.

# RELATED RATES - the difference is step 3
1. Draw it. Label what varies with letters, not numbers.
2. Write an equation relating the quantities.
3. Differentiate BOTH SIDES with respect to TIME (implicitly).
   Every variable produces a d/dt term via the chain rule.
4. NOW substitute the numbers for the instant asked about,
   and solve for the rate you want.

# The classic mistake in related rates is substituting the
# numbers at step 2. Do that and the varying quantity becomes
# a constant, whose derivative is zero, and the problem
# collapses. Numbers go in LAST.
```

---

## Unit 3 — Integrals: Series, Area, Techniques & Differential Equations

### Picking a convergence test — Ch 11

| If the series has… | Reach for |
|---|---|
| Terms that clearly do not go to 0 | nth-term test — done, it diverges |
| The form Σ a·rⁿ | Geometric: converges iff \|r\| < 1 |
| The form Σ 1/n^(p) | p-series: converges iff p > 1 |
| Factorials or n-th powers | Ratio test — factorials cancel beautifully in a ratio |
| (−1)ⁿ | Alternating series test |

Always run the nth-term test first. It is one line, and when it applies it ends the problem immediately. Remember it can only prove divergence — a limit of 0 does not prove convergence, which is exactly why Σ1/n diverges.

### Choosing an integration technique — Ch 12–13

| The integrand looks like… | Try |
|---|---|
| A function and (a multiple of) its own derivative | u-substitution |
| A product of two unrelated types — x·eˣ, x·sin x, ln x | By parts, choosing u by LIATE |
| A rational function with a factorable denominator | Partial fractions |
| √(a² − x²), √(a² + x²), √(x² − a²) | Trig substitution |
| Nothing obvious | Algebra first — expand, split the fraction, or use an identity. Many "hard" integrals are easy once rewritten |

Two habits that catch most errors: after any indefinite integral, differentiate your answer and check you get the integrand back — it takes ten seconds and is a complete verification. And when you substitute in a definite integral, either change the limits to u-values or convert back to x before evaluating. Mixing the two is the most common wrong answer in this chapter.

### Differential equations — Ch 15

| Type | Method |
|---|---|
| Separable dy/dx = g(x)·h(y) | Separate: dy/h(y) = g(x) dx, integrate both sides, + C on one side only, then solve for y |
| Initial value problem | Find the general solution first, then use the initial condition to pin down C. Not the other way round |
| Exponential growth / decay dy/dt = k·y | y = y₀·e^(kt). Positive k grows, negative k decays. Half-life and doubling-time questions are this equation |
| Slope fields | At each point, the segment's slope is dy/dx evaluated there. A solution curve follows the segments — you are reading a picture, not computing |

Verification works here too, and is even easier: substitute your solution back into the original equation. If both sides match, you are right, regardless of how you got there.

---

## Chapter Tests & the Final — Where the Marks Actually Go

### Most lost marks are not conceptual — The trap

| Error | Guard |
|---|---|
| Calculator in degree mode | Check before question 1. sin(π) should read 0 |
| Dropping + C | Write it as you write the integral sign, not afterwards |
| Forgetting the chain rule's inner derivative | Underline the inside function before differentiating |
| Sign slips on cos, csc, cot derivatives | Co-functions are negative. Say it once per test |
| u-sub limits not changed | Decide up front: change the limits, or convert back. Never half of each |
| Substituting numbers too early in related rates | Differentiate first, numbers last |
| Answering the wrong question | The question asks for the value, the rate, or the x where it happens. Re-read the last line before submitting |

### Using this site on this course — In practice

Every card here is a flashcard and a quiz option automatically. Pick the 📐 Math deck rather than All domains, and star (★) the cards for the chapter whose test is next so they land in your study list.

The techniques in the Productivity domain apply directly: The Memory Palace is well suited to the derivative and integral tables, which are exactly the ordered arbitrary lists it is for. Hansei after each practice set — what broke, what would have caught it — turns a wrong answer into a countermeasure rather than a bad mood. And Sleep matters more here than for most subjects, because a calculation error rate is one of the first things sleep loss moves.

A note on the scores so far: an honest way to read a 73% is that roughly one question in four is going wrong, and the error table above is where those usually live. It is worth spending one practice set doing nothing but checking your own work — differentiate every antiderivative, substitute every solution back — before assuming the gap is conceptual.

---

## Logarithms & Exponents — Rules and How to Solve

### A log is an exponent — that is the whole idea — Core Concept

log_b(x) = y means exactly b^(y) = x. "What power do I raise b to, to get x?" Every log rule below is an exponent rule wearing a different hat, which is why the two columns mirror each other line for line.

### The mirror — Reference

| Exponent rule | Log rule |
|---|---|
| b^(m) · b^(n) = b^(m+n) | log(MN) = log M + log N |
| b^(m) / b^(n) = b^(m−n) | log(M/N) = log M − log N |
| (b^(m))^(n) = b^(mn) | log(M^(p)) = p · log M |
| b^(0) = 1 | log_b(1) = 0 |
| b^(1) = b | log_b(b) = 1 |
| b^(−n) = 1/b^(n) | log(1/M) = −log M |
| b^(1/n) = ^(n)√b | log(^(n)√M) = (1/n) · log M |

Change of base: log_b(x) = ln x / ln b = log x / log b. This is how you compute log_7(200) on a calculator that only offers ln and log.

ln is log_e, and log with no base written usually means log_10. In calculus assume natural log unless told otherwise — e is the base that makes the derivative clean.

### The three rules that do not exist — The trap

| Wrong | Right |
|---|---|
| log(M + N) = log M + log N | No such rule. A log of a sum does not split. log M + log N = log(MN) — the sum is on the outside |
| log M / log N = log(M − N) | No. log M − log N = log(M/N). A quotient of logs is a change of base, not a subtraction |
| (log M)^(p) = p · log M | Only log(M^(p)) = p · log M. The exponent must be inside the log |

And the one that costs marks quietly: a log of a negative number or of zero is undefined, so after solving any log equation you must check every solution in the original. Extraneous roots are normal here, not evidence you made a mistake.

### The two shapes, and how each is solved — Hands-on

```
# VARIABLE IN THE EXPONENT -> take a log of both sides
   3^(2x) = 50
   ln(3^(2x)) = ln 50
   2x · ln 3 = ln 50          # the power rule pulls it down
   x = ln 50 / (2 · ln 3) ≈ 1.78

# VARIABLE INSIDE A LOG -> condense to ONE log, then exponentiate
   log(x) + log(x − 3) = 1
   log(x(x − 3)) = 1          # product rule condenses
   x(x − 3) = 10^1            # base 10 implied by "log"
   x² − 3x − 10 = 0
   (x − 5)(x + 2) = 0  ->  x = 5 or x = −2

   CHECK: x = −2 would need log(−2). Undefined. Reject.
   Answer: x = 5 only.
```

---

## Trigonometry — The Unit Circle, Identities & Inverses

### The unit circle — every value you are asked to know — Diagram

*(diagram — see this card on the site)*

Each point is (cos θ, sin θ). Reading it beats recalling a table: the x-coordinate is the cosine, the y-coordinate is the sine, and the tangent is their ratio. Where the x-coordinate is 0 — at π/2 and 3π/2 — the tangent is undefined, which is exactly where tan has its vertical asymptotes.

Only the first quadrant needs memorising. Everything else is those values with signs from ASTC: All positive in QI, only Sine in QII, only Tangent in QIII, only Cosine in QIV.

### Identities worth knowing by heart — Reference

| Family | Identities |
|---|---|
| Reciprocal | csc θ = 1/sin θ \| sec θ = 1/cos θ \| cot θ = cos θ/sin θ |
| Pythagorean | sin²θ + cos²θ = 1 \| 1 + tan²θ = sec²θ \| 1 + cot²θ = csc²θ |
| Even / odd | cos(−θ) = cos θ (even) \| sin(−θ) = −sin θ and tan(−θ) = −tan θ (odd) |
| Sum | sin(A ± B) = sinA cosB ± cosA sinB; cos(A ± B) = cosA cosB ∓ sinA sinB — the sign flips |
| Double angle | sin 2θ = 2 sinθ cosθ; cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ |
| Power reduction | sin²θ = (1 − cos 2θ)/2 \| cos²θ = (1 + cos 2θ)/2 — the ones that make ∫ sin²x dx doable |

The second and third Pythagorean identities are just the first divided through by cos²θ and by sin²θ. Derive them in ten seconds instead of memorising three separate facts.

And the first one is the Pythagorean theorem itself. On the unit circle the legs are cos θ and sin θ and the hypotenuse is 1, so a² + b² = c² becomes cos²θ + sin²θ = 1. That is why the family is named after him — it is one theorem in trigonometric clothing.

### Inverse trig, and the two laws — Reference

| Inverse | Range — the principal values |
|---|---|
| arcsin x | [−π/2, π/2] — QIV and QI |
| arccos x | [0, π] — QI and QII |
| arctan x | (−π/2, π/2) — QIV and QI, never reaching the ends |

Those ranges are why arcsin(sin(3π/4)) is π/4, not 3π/4 — the answer has to land inside the range. It is a favourite exam question precisely because the obvious answer is wrong.

| Law | Formula | Use when |
|---|---|---|
| Sines — the law of sines | a/sin A = b/sin B = c/sin C | You have an angle paired with the side opposite it |
| Cosines — the law of cosines | c² = a² + b² − 2ab·cos C | Three sides, or two sides and the angle between them |

---

## The Two Pictures — Derivative as Slope, Integral as Area

### The derivative is a limit of slopes — Diagram

*(diagram — see this card on the site)*

Take two points on the curve. The line through them — the secant — has slope Δy/Δx = [f(x+h) − f(x)] / h, the average rate of change across that interval. Now slide the second point toward the first. The secant pivots, and in the limit as h → 0 it becomes the tangent, whose slope is f′(x) — the instantaneous rate.

That is the whole definition, and it is worth being able to sketch, because it turns several memorised rules into obvious consequences: f′ = 0 at a peak because the tangent is flat there; a corner has no derivative because the secants approach different slopes from each side; and a vertical tangent means f′ is undefined rather than zero.

### The integral is a limit of sums — Diagram

*(diagram — see this card on the site)*

Slice the region under the curve into rectangles and add their areas — that is a Riemann sum, and it is an approximation. More, thinner rectangles give a better one; the definite integral is what those sums converge to. The elongated S of ∫ is literally an S, for "sum".

Which is what makes the Fundamental Theorem surprising rather than merely true. These two pictures — slopes of tangents, areas under curves — look unrelated, and the theorem says each undoes the other. Area is found by reversing slope. That is the biggest single idea in the course; almost everything in Units 2 and 3 follows from it.

One consequence to carry into the tests: a definite integral is a signed area. Region below the axis counts as negative, which is why ∫_0^(2π) sin x dx = 0 even though the curve plainly encloses area. If a question asks for total area rather than for the integral, split at the zeros and take absolute values.

---

## Algebra & Geometry Formulas — The Prerequisites

### Algebra — Reference

| Name | Formula |
|---|---|
| Quadratic formula | x = (−b ± √(b² − 4ac)) / 2a, for ax² + bx + c = 0 |
| Discriminant | b² − 4ac — positive gives two real roots, zero gives one, negative gives none real |
| Pythagorean theorem | a² + b² = c² — legs a, b, hypotenuse c. Only for right triangles; otherwise use the law of cosines, which is its generalisation |
| Difference of squares | a² − b² = (a + b)(a − b) |
| Perfect square | (a ± b)² = a² ± 2ab + b² |
| Sum / difference of cubes | a³ ± b³ = (a ± b)(a² ∓ ab + b²) |
| Slope | m = (y₂ − y₁)/(x₂ − x₁) |
| Point-slope form | y − y₁ = m(x − x₁) — the form every tangent-line answer takes |
| Distance | d = √((x₂ − x₁)² + (y₂ − y₁)²) |
| Midpoint | ((x₁ + x₂)/2, (y₁ + y₂)/2) |
| Circle (centre h,k) | (x − h)² + (y − k)² = r²; the unit circle is x² + y² = 1 |
| Ellipse ("oval") | (x − h)²/a² + (y − k)²/b² = 1 — a circle stretched by a and b |

### Geometry — the ones optimisation keeps asking for — Reference

| Shape | Area / Volume | Perimeter / Surface |
|---|---|---|
| Circle | A = πr² | C = 2πr |
| Triangle | A = ½bh | — |
| Trapezoid | A = ½(b₁ + b₂)h | — |
| Rectangular box | V = lwh | SA = 2(lw + lh + wh) |
| Cylinder | V = πr²h | SA = 2πr² + 2πrh |
| Cone | V = ⅓πr²h | SA = πr² + πrl |
| Sphere | V = ⁴⁄₃πr³ | SA = 4πr² |

Optimisation and related-rates questions nearly always hand you one of these plus a constraint. "A cylindrical can holds 355 cm³ — minimise the material" is the volume formula as the constraint and the surface-area formula as the thing to minimise. Working out which is which is most of the problem.

Worth noticing the pattern in the last rows: differentiating a sphere's volume with respect to r gives 4πr² — its surface area. Same for a circle, where d/dr(πr²) = 2πr is the circumference. Growing a shape outward adds a shell of exactly its surface, which is both a sanity check and a reminder that these formulas are related rather than arbitrary.

---

## Shape Formulas — Labelled Diagrams

### What each letter refers to — Diagram

*(diagram — see this card on the site)*

Amber marks the dimension the letter names. The single most common geometry error is not forgetting a formula — it is using the diameter where the formula wants the radius. If a problem gives you "a circle 10 cm across", r is 5, not 10.

### Flat shapes — Reference

| Shape | Area | Perimeter |
|---|---|---|
| Rectangle | A = lw | P = 2l + 2w |
| Square | A = s² | P = 4s |
| Triangle | A = ½bh | Sum of the three sides |
| Trapezoid | A = ½(b₁ + b₂)h | Sum of the four sides |
| Circle | A = πr² | C = 2πr = πd |
| Circle sector | A = ½r²θ (θ in radians) | Arc length s = rθ |

In a triangle, h is the perpendicular height — the right-angle mark in the diagram is doing real work. For an obtuse triangle that height falls outside the shape, which surprises people the first time.

### Solids — Reference

| Solid | Volume | Surface area |
|---|---|---|
| Rectangular box | V = lwh | SA = 2(lw + lh + wh) |
| Cube | V = s³ | SA = 6s² |
| Cylinder | V = πr²h | SA = 2πr² + 2πrh |
| Cone | V = ⅓πr²h | SA = πr² + πrl, slant l = √(r² + h²) |
| Sphere | V = ⁴⁄₃πr³ | SA = 4πr² |
| Hemisphere | V = ⅔πr³ | SA = 3πr² (curved + flat face) |
| Pyramid | V = ⅓ · (base area) · h | Base + the triangular faces |

The cone's surface area uses the slant height l (green in the diagram), not the vertical height h. They are different lengths related by Pythagoras, and mixing them is the classic cone mistake.

Notice the pattern: cone and pyramid both carry a ⅓ against the prism or cylinder with the same base and height. A cone is exactly a third of its surrounding cylinder — worth remembering as one fact rather than two formulas.

### How these show up in calculus — In practice

| Question type | What the shape formula is doing |
|---|---|
| Optimisation | One formula is the constraint (fixed volume), the other is the objective (minimise material). "A can holds 355 cm³ — least aluminium" is V = πr²h fixed, SA minimised |
| Related rates | Differentiate the formula with respect to time. A cone draining gives dV/dt in terms of dh/dt — and usually needs similar triangles first to write r in terms of h |
| Volumes of revolution | Disk, washer and shell are just πr² and the cylinder's side, integrated. That is why the formulas look familiar |

A sanity check that catches unit and setup errors: areas come out in square units, volumes in cubic. If a volume answer has an r² and no third length, something is missing.

---

## TI-84 Plus CE — The Keys That Matter for Calculus

### Set the mode before anything else — Do this first

```
# Press MODE. On the screen you want:
   RADIAN      # NOT DEGREE. Calculus is radians.
   FUNCTION    # not PARAMETRIC/POLAR/SEQ
   MATHPRINT   # shows fractions and integrals the way
               # they are written; CLASSIC is one line

# Verify with one keystroke, every single test:
   sin(π)  ->  should read 0 (or a tiny number like -3E-13)
   If it reads 0.0548, you are in DEGREE mode. Fix it now.

# Press 2nd then MODE to QUIT back to the home screen.
```

The tiny number is not an error — sin(π) can come back as something like −3E−13 because π is stored to finite precision. Read that as zero.

### The keys you will actually use — Reference

| Want | Press |
|---|---|
| π | 2nd then ^ |
| e (the number) | 2nd then ÷ |
| e^( | 2nd then LN |
| Previous answer | 2nd then (−) — this is ANS |
| Quit any menu | 2nd then MODE |
| Store to a variable | STO▶ then ALPHA and a letter |
| Decimal → fraction | MATH → 1: ▶Frac |
| Table of values | 2nd then GRAPH. Set it up with 2nd then WINDOW |

### Negative is not minus — The trap

The TI-84 has two different keys and they are not interchangeable. (−), next to ENTER, makes a number negative. −, above +, subtracts. Using the wrong one gives ERR: SYNTAX at best and a wrong answer at worst. If you get a syntax error you cannot explain, this is the first thing to check.

Two more that bite: −2² evaluates as −4 because the square binds tighter than the negation — type (−2)² if you mean 4. And always parenthesise a whole denominator: 1/(2+3) is 0.2, while 1/2+3 is 3.5.

### Derivatives and integrals numerically — Hands-on

```
# DERIVATIVE at a point:  MATH -> 8: nDeriv(
   nDeriv(expression, variable, value)
   nDeriv(X²,X,3)            -> 6        # d/dx x² at x=3
   nDeriv(sin(X),X,0)        -> 1

# DEFINITE INTEGRAL:  MATH -> 9: fnInt(
   fnInt(expression, variable, lower, upper)
   fnInt(X²,X,0,2)           -> 2.6666…  # = 8/3
   fnInt(sin(X),X,0,π)       -> 2

# SUMMATION (partial sums for series):  MATH -> 0: Σ(
   Σ(expression, variable, start, end)
   Σ(1/N²,N,1,100)           -> 1.6349…  # approaching π²/6

# LOG TO ANY BASE:  MATH -> A: logBASE(
   logBASE(200,7)            -> 2.7227…
   # or do it by hand: ln(200)/ln(7) - same answer

# Type X with the X,T,θ,n key. Other letters need ALPHA.
```

### From the graph — the CALC menu — Hands-on

```
# Enter the function in Y= first, then GRAPH.
# ZOOM 6 = ZStandard is the usual starting window.
# ZOOM 0 = ZoomFit fits the y-range to the x-range.

# Press 2nd then TRACE to open CALC:
   1: value        f(x) at an x you type
   2: zero         a root - you give a Left and Right bound
   3: minimum      local min in a bracket you give
   4: maximum      local max
   5: intersect    where two curves meet (solve f(x)=g(x))
   6: dy/dx        the derivative at a point, off the graph
   7: ∫f(x)dx      the definite integral, and it shades it

# "Left Bound? / Right Bound? / Guess?" means: move the
# cursor to one side, ENTER, the other side, ENTER, then
# ENTER again. It only searches inside the bracket you give.

# LIMITS have no dedicated key. Use the TABLE:
#   2nd WINDOW -> TblStart just below the value,
#   ΔTbl = 0.001, then 2nd GRAPH and read what it approaches.
```

### What the calculator will confidently get wrong — The trap

| Situation | What happens |
|---|---|
| nDeriv at a corner or cusp | It returns a number anyway. nDeriv(abs(X),X,0) gives 0, but the derivative does not exist there. The routine estimates with a symmetric difference and cannot tell the difference |
| Vertical asymptotes | The graph draws a near-vertical line through the asymptote and it looks like part of the curve. It is not — it is the plotter joining points |
| Improper integrals | fnInt across an infinite discontinuity returns something, or errors, and neither means "converges" |
| ERR: INVALID DIM | Usually a stat plot left switched on. 2nd then Y=, turn all Plots off |
| ERR: WINDOW RANGE | Xmin ≥ Xmax or Ymin ≥ Ymax. Press ZOOM 6 to reset |
| A blank graph | Nothing is wrong with the function — the window is wrong. ZOOM 6, then ZOOM 0 |

There is a drill for this card in the repo: python tools/ti84_trainer.py asks for the key sequences and checks your answers, and every number it quotes back is computed by Python at run time rather than typed in, so the drill cannot be wrong about the arithmetic. Pass a flag to drill one area:

| Flag | Covers | Drills |
|---|---|---|
| --area mode | Mode setup | 4 |
| --area numeric | Numeric functions (nDeriv, fnInt, Σ, logBASE) | 9 |
| --area calc | The CALC menu and graphing | 7 |
| --area errors | Errors, traps, and where the calculator lies | 7 |

The most important limitation to understand for a calculus course: the TI-84 has no computer algebra system. nDeriv and fnInt return numbers, never expressions — it cannot tell you that the derivative of x² is 2x, only that it is 6 at x = 3. Symbolic work is the TI-89 and Nspire CAS. So the calculator is a checking tool: do the algebra by hand, then confirm the number.

---

## The Named Theorems — Rolle, MVT, IVT, EVT & Squeeze

### The hypotheses are the answer — Core Concept

Theorem questions are almost never about what the theorem concludes — they are about the conditions it needs. "Which of the following describes Rolle's Theorem?" is really "can you list the hypotheses?" So learn each one as a checklist plus a conclusion, and notice a pattern that runs through all of them: continuity is required on the closed interval [a,b], differentiability only on the open interval (a,b).

That asymmetry is deliberate, not a typo. The endpoints need the function to exist and connect; they do not need a two-sided derivative, which could not exist at an endpoint anyway.

### Rolle is the flat case of the Mean Value Theorem — Diagram

*(diagram — see this card on the site)*

Same picture twice. On the left the endpoints sit at equal height, so the secant joining them is horizontal and the parallel tangent is flat — f′(c) = 0. On the right the endpoints differ, the secant is tilted, and the guaranteed tangent is parallel to it. Rolle is the Mean Value Theorem with the extra condition f(a) = f(b), which is exactly what makes the slope zero.

### The five, stated properly — Reference

| Theorem | Requires | Guarantees |
|---|---|---|
| Rolle's | 1. f continuous on [a,b]; 2. f differentiable on (a,b); 3. f(a) = f(b) | At least one c in (a,b) with f′(c) = 0 |
| Mean Value (MVT) | 1. continuous on [a,b]; 2. differentiable on (a,b) | At least one c in (a,b) with f′(c) = [f(b) − f(a)]/(b − a) — instantaneous rate equals average rate somewhere |
| Intermediate Value (IVT) | continuous on [a,b] only — no differentiability needed | For any N between f(a) and f(b), some c with f(c) = N. This is how you prove a root exists: opposite signs at the ends |
| Extreme Value (EVT) | continuous on a closed, bounded [a,b] | f attains an absolute maximum and an absolute minimum on the interval |
| Squeeze | g(x) ≤ f(x) ≤ h(x) near a, and lim g = lim h = L | lim f = L. The tool for lim_x→0 x²sin(1/x) = 0, and for proving lim_x→0 (sin x)/x = 1 |

### Existence, not location — and drop a hypothesis, lose the theorem — The trap

Every one of these is an existence statement. It says some c is there; it does not tell you where, how many, or how to find it. "Find all values of c guaranteed by the MVT" is a separate calculation — set f′(x) equal to the secant slope and solve.

| Drop this | And it breaks |
|---|---|
| Differentiability, from Rolle / MVT | f(x) = \|x\| on [−1, 1]: continuous, endpoints equal, but the corner at 0 means no c with f′(c) = 0 exists |
| Continuity, from IVT | A step function jumps straight past every value in between without ever equalling one |
| Closed interval, from EVT | f(x) = x on the open (0,1) gets arbitrarily close to 1 and never reaches a maximum |
| Bounded interval, from EVT | f(x) = x on [0, ∞) has no maximum at all |

Worth knowing as its own fact, because it is asked directly: differentiable ⇒ continuous, but continuous ⇏ differentiable. The absolute value function at 0 is the standard counterexample. Contrapositive form is the useful one — if a function is not continuous at a point, it cannot be differentiable there.

### Two different theorems both get called "average value" — The trap

| Name | Which one |
|---|---|
| Mean Value Theorem; sometimes written "average value theorem" | The derivative one above: instantaneous rate equals average rate at some c. Rolle is its special case |
| Mean Value Theorem for Integrals | The integral one: if f is continuous on [a,b], some c has f(c) = 1/(b−a) · ∫_a^(b) f(x) dx — the average value is actually attained by the function |

Courses and textbooks are not consistent about this naming, so read from context: if the statement involves f′, it is the derivative version; if it involves an integral, it is the integral version. Both say "somewhere the function matches its average" — just average rate versus average value.

### The three ways these get examined — Hands-on

```
# 1. "Does the theorem APPLY?" -> check hypotheses one by one
   f(x) = x^(2/3) on [−1, 1], Rolle?
   continuous on [−1,1]?      yes
   f(−1) = f(1) = 1?           yes
   differentiable on (−1,1)?   NO - cusp at x = 0
   -> Rolle does not apply. (And indeed f′ is never 0 here.)

# 2. "FIND the c" -> apply the conclusion as an equation
   f(x) = x² on [0, 4], MVT:
   secant slope = (16 − 0)/(4 − 0) = 4
   f′(x) = 2x = 4  ->  x = 2       # c = 2, inside (0,4) ✓

# 3. "PROVE a root exists" -> that is IVT, via a sign change
   Show x³ + x − 1 = 0 has a root in [0, 1]:
   f is a polynomial, so continuous on [0,1]
   f(0) = −1  0
   -> 0 lies between them, so some c in (0,1) has f(c) = 0

# Note what step 3 does NOT do: it never finds the root.
# IVT proves existence. Finding it is a different job.
```

---

## sin, cos, tan & sec — What They Actually Are

### They are ratios, not operations — Core Concept

sin is not something you do to an angle the way squaring is something you do to a number. Each of the six is a ratio of two sides of a right triangle, and which two is the whole definition. Once the angle is fixed, that ratio is fixed too — a triangle twice the size has both sides twice as long and the ratio is unchanged. That scale-independence is exactly why the functions are useful.

### The right-triangle definition — Diagram

*(diagram — see this card on the site)*

Adjacent and opposite are named relative to θ — they swap if you measure from the other acute angle. The hypotenuse never changes: it is always the side across from the right angle, and always the longest. So the first thing to do in any triangle problem is label the sides from the angle you were given.

SOH-CAH-TOA is the standard mnemonic: Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse, Tangent = Opposite/Adjacent.

### All six, and how they pair up — Reference

| Function | Ratio | Reciprocal of | Read it as |
|---|---|---|---|
| sin θ | opposite / hypotenuse | csc | How high, per unit of distance travelled |
| cos θ | adjacent / hypotenuse | sec | How far across, per unit travelled |
| tan θ | opposite / adjacent | cot | Slope. Rise over run — this is why tan shows up in every tangent-line question |
| csc θ | hypotenuse / opposite | sin | — |
| sec θ | hypotenuse / adjacent | cos | — |
| cot θ | adjacent / opposite | tan | — |

The reciprocal pairing is the part that trips people, because the names do not match the pairs. Secant pairs with cosine and cosecant pairs with sine — the "co" is on opposite sides. The reliable trick: look at the third letter. sec → cosine, csc → sine, cot → tangent.

### Two definitions, one function — and why courses use both — Concept

A right triangle only has acute angles, so the triangle definition cannot explain sin(120°) or a negative cosine. The unit circle fixes that: put the angle at the origin, and the point where its ray meets the circle of radius 1 has coordinates (cos θ, sin θ).

|  | Right triangle | Unit circle |
|---|---|---|
| Works for | Acute angles only, 0 to 90° | Every angle, including negative and beyond 360° |
| sin θ | opp/hyp | The y-coordinate |
| cos θ | adj/hyp | The x-coordinate |
| Best for | Solving actual triangles — surveying, ladders, ramps | Calculus, periodicity, anything with a sign |

They agree wherever both apply, because on a unit circle the hypotenuse is 1 — so opp/hyp becomes just opp, which is the height, which is y. Same function, described from two directions. See Trigonometry — The Unit Circle, Identities & Inverses for the circle side.

### Where sec quietly matters, and where it all goes wrong — The trap

sec looks like the least useful of the six until calculus, where it appears constantly for one reason: d/dx tan x = sec²x, and 1 + tan²θ = sec²θ. Those two facts are why trig substitution reaches for sec whenever an integrand contains √(x² − a²). It is not arbitrary — it is the identity that turns the radical into something without a root.

| Mistake | What is actually true |
|---|---|
| sin⁻¹x means 1/sin x | No. sin⁻¹ is the inverse function, arcsin. The reciprocal is csc x. This notation is genuinely bad and catches everyone once |
| sin²x means sin(x²) | No — sin²x is (sin x)². The exponent sits after the function name but applies to the output |
| Any angle works in any function | tan and sec are undefined wherever cos θ = 0 — at π/2, 3π/2 and so on, because those are division by zero. cot and csc break where sin θ = 0 |
| Degrees are fine | Only in geometry. Every calculus formula on this site — every derivative, every limit — assumes radians |

Ranges are worth knowing as a sanity check on an answer: sin and cos always land in [−1, 1], so a sine of 1.4 is an arithmetic error. sec and csc are the opposite — they never fall between −1 and 1, because they are 1 over something no bigger than 1.

---

## Implicit Differentiation & Choosing Which Rule First

### Choosing the rule: look at the outermost operation — Core Concept

Before you differentiate anything, ask what is the last thing that happens if you evaluated this at a number. That operation names the rule.

| Outermost operation | Rule | Example |
|---|---|---|
| Addition / subtraction | Differentiate term by term | x³ + sin x |
| A product of two functions | Product rule | x²·sin x |
| A quotient | Quotient rule | (x+1)/(x²−3) |
| A function wrapped around another | Chain rule | sin(x²) — the sine happens last |
| A constant times something | Pull the constant out | 5·tan x |

sin(x²) and sin²x look similar and need different first moves. In sin(x²) the sine is outermost, so chain rule with inner x². In sin²x = (sin x)² the squaring is outermost, so chain rule with inner sin x. Getting the order right is most of the work.

### The chain rule, said once, properly — Concept

d/dx f(g(x)) = f′(g(x)) · g′(x) — differentiate the outer function leaving the inner one untouched, then multiply by the derivative of the inner. The universal mistake is stopping before that multiplication.

```
# Underline the inside before you start. It is the whole trick.
   d/dx sin(3x²)  ->  cos(3x²) · 6x        # not just cos(3x²)
   d/dx (x³+1)⁵   ->  5(x³+1)⁴ · 3x²
   d/dx e^(2x)    ->  e^(2x) · 2
   d/dx ln(5x)    ->  (1/5x) · 5  =  1/x

# Nested twice? Peel one layer at a time, outside in.
   d/dx sin(cos(x²))
     = cos(cos(x²)) · d/dx[cos(x²)]
     = cos(cos(x²)) · (−sin(x²)) · 2x
```

### Implicit differentiation — the mechanical version — Hands-on

When y is not solved for, differentiate both sides with respect to x and write dy/dx every time you differentiate a y. That is the chain rule doing its job: y is a function of x, so d/dx[y³] = 3y²·dy/dx.

```
# x² + y² = 25
   2x + 2y·(dy/dx) = 0
   dy/dx = −x/y

# THE FOUR STEPS, every time:
#   1. d/dx both sides
#   2. every y gives a dy/dx  (chain rule)
#   3. get all dy/dx terms on ONE side, everything else on the other
#   4. factor out dy/dx and divide
```

### The hard case: product rule and chain rule together — Hands-on

```
# x·sin(y) = 5y + 2x        

# LEFT side is a PRODUCT of x and sin(y):
   d/dx[x·sin(y)] = (1)·sin(y) + x·cos(y)·(dy/dx)
                     ^^^^^^^^^^   ^^^^^^^^^^^^^^^^
                     d/dx[x]·sin(y)   x·d/dx[sin(y)], chain rule
                                      because y depends on x

# RIGHT side:
   d/dx[5y + 2x] = 5·(dy/dx) + 2

# Set them equal and GROUP the dy/dx terms:
   sin(y) + x·cos(y)·(dy/dx) = 5·(dy/dx) + 2

   x·cos(y)·(dy/dx) − 5·(dy/dx) = 2 − sin(y)      # step 3
   (dy/dx)·[x·cos(y) − 5]       = 2 − sin(y)      # step 4: factor

   dy/dx = (2 − sin(y)) / (x·cos(y) − 5)

# The answer contains BOTH x and y. That is normal and correct
# for implicit differentiation - do not try to eliminate y.
```

### Inverse trig derivatives — all six — Reference

| f(x) | f′(x) | f(x) | f′(x) |
|---|---|---|---|
| arcsin x | 1/√(1 − x²) | arccos x | −1/√(1 − x²) |
| arctan x | 1/(1 + x²) | arccot x | −1/(1 + x²) |
| arcsec x | 1/(\|x\|·√(x² − 1)) | arccsc x | −1/(\|x\|·√(x² − 1)) |

Learn the left column and negate for the right — each co-inverse is the negative of its partner, so three facts cover six. Note the absolute value in the arcsec pair; it is not decoration, it is what keeps the derivative positive on both branches.

These almost always arrive wrapped in a chain rule: d/dx arctan(3x) = 1/(1 + (3x)²) · 3 = 3/(1 + 9x²).

### Higher-order derivatives, and going backwards — Reference

| Notation | Meaning |
|---|---|
| f″(x), d²y/dx² | Rate of change of the rate of change — concavity, and acceleration from position |
| f‴, f⁽⁴⁾ | Keep differentiating. Beyond the third, the superscript goes in parentheses |
| Antiderivative | The power rule in reverse: add one to the exponent, divide by the new exponent. x³ → x⁴/4. Always + C |

A quick check that costs nothing: differentiate your antiderivative. If it does not return the original, you have made an error, and you will know immediately rather than at the end of a three-step problem.

---

## Numerical Integration — Trapezoidal Rule, Midpoint & Simpson's

### Why trapezoids beat rectangles — Diagram

*(diagram — see this card on the site)*

A rectangle's flat top is wrong almost everywhere — it matches the curve at one point and misses either side. A trapezoid's slanted top joins two points on the curve, so it tracks the function instead of approximating it with a step. Same number of slices, much less error, and it is why the Trapezoidal Rule exists.

### The three formulas — Reference

| Rule | Formula, with Δx = (b − a)/n |
|---|---|
| Trapezoidal | (Δx/2)·[f(x₀) + 2f(x₁) + 2f(x₂) + … + 2f(x_n−1) + f(x_n)] |
| Midpoint | Δx·[f(m₁) + f(m₂) + … + f(m_n)], where each m is the centre of its slice |
| Simpson's | (Δx/3)·[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + … + 4f(x_n−1) + f(x_n)] |

The coefficient pattern is the thing to memorise, and each is different. Trapezoid: 1, 2, 2, …, 2, 1. Simpson's: 1, 4, 2, 4, 2, …, 4, 1 — ends are 1, then alternate 4 and 2, always ending on a 4 before the final 1.

Simpson's requires n to be even. It fits a parabola through each pair of slices, so an odd number leaves one stranded. If a problem gives you n = 5 and asks for Simpson's, re-read it — something is wrong.

### Which way each one is wrong — The trap

| Curve is… | Trapezoid | Midpoint |
|---|---|---|
| Concave up | Overestimates — the chord sits above the curve | Underestimates |
| Concave down | Underestimates | Overestimates |

Derive it rather than memorise it: on a concave-up curve the straight chord joining two points lies above the arc between them, so trapezoids include area that is not there. Midpoint errs the other way for the mirror-image reason. Questions asking "is this an over- or under-estimate?" are asking about concavity, which means they are asking about f″.

Simpson's is exact for any polynomial of degree 3 or lower. That surprises people — it fits parabolas, yet handles cubics perfectly, because the cubic error terms cancel between the pairs. If a problem asks you to approximate ∫x³dx by Simpson's and compare with the exact value, the answer is that they match.

### When you actually use these — In practice

Numerical rules are not a fallback for weak algebra — they are the only option when there is no elementary antiderivative. ∫e^(−x²)dx is the standard example: it is central to statistics and has no answer in elementary functions, so every value of it anyone has ever used was computed numerically.

They are also how you integrate data rather than a formula. Given a table of speed readings every 10 seconds, the distance travelled is a trapezoidal sum — there is no function to antidifferentiate. That is the form these questions usually take on a test.

On a TI-84, fnInt( does this for you numerically, so it is a good check on a hand computation — see TI-84 Plus CE. But the exam wants the hand version with the coefficient pattern shown.

---

## Series — Choosing a Test, and Radius of Convergence

### Sequence versus series — the distinction everything rests on — Core Concept

|  | Sequence {a_n} | Series Σa_n |
|---|---|---|
| Is | A list of terms | The sum of that list |
| Converges when | The terms approach a limit | The partial sums approach a limit |
| Example | 1/n → 0, converges | Σ1/n diverges — the harmonic series |

That last row is the single most important fact in the chapter. Terms going to zero is necessary but not sufficient — the harmonic series has terms shrinking to nothing and still sums to infinity. Every test below exists because that one check is not enough.

### The full battery, in the order to try them — Reference

| # | Test | Statement | Reach for it when |
|---|---|---|---|
| 1 | nth-term | If lim a_n ≠ 0, diverges. Limit 0 proves nothing | Always first — it is one line |
| 2 | Geometric | Σar^(n) converges iff \|r\| < 1, to a/(1−r) | A constant ratio between terms |
| 3 | p-series | Σ1/n^(p) converges iff p > 1 | A plain power of n on the bottom |
| 4 | Integral | If f is positive, continuous and decreasing with a_n = f(n), then Σa_n and ∫_1^(∞)f do the same thing | The term is something you can actually integrate |
| 5 | Direct comparison | 0 ≤ a_n ≤ b_n and Σb_n converges ⇒ Σa_n converges. Bigger diverges ⇒ smaller may still converge, so pick the direction carefully | The term is almost a p-series or geometric |
| 6 | Limit comparison | lim a_n/b_n = L with 0 < L < ∞ ⇒ both do the same thing | Comparison is obviously right but the inequality is awkward. Usually easier than #5 |
| 7 | Ratio | L = lim\|a_n+1/a_n\|. <1 converges, >1 diverges, =1 inconclusive | Factorials or n in an exponent — they cancel beautifully |
| 8 | Root | L = lim ^(n)√\|a_n\|, same verdicts | The whole term is raised to the n |
| 9 | Alternating | Converges if terms decrease in magnitude and → 0 | (−1)^(n) present |

Tests 7 and 8 both return "inconclusive" at L = 1, and that is a real answer, not a failure — it means try another test. The ratio test is inconclusive on every p-series, which is why #3 exists separately.

### Absolute versus conditional convergence — Concept

| Term | Means | Example |
|---|---|---|
| Absolutely convergent | Σ\|a_n\| converges. This is the strong kind — it implies Σa_n converges too | Σ(−1)^(n)/n² |
| Conditionally convergent | Σa_n converges but Σ\|a_n\| does not | Σ(−1)^(n)/n — the alternating harmonic series |

The standard exam move: given an alternating series, test the absolute version first. If Σ|a_n| converges you are finished and the answer is "absolutely". Only if it diverges do you run the alternating series test to decide between conditional and divergent.

Useful bonus for alternating series: the error from stopping after n terms is no bigger than the first term you left out. That single fact answers every "how many terms for accuracy 0.01?" question.

### Radius and interval of convergence — Hands-on

```
# A power series Σ cₙ(x − a)ⁿ converges on an interval centred
# at a. Find it with the RATIO TEST on the whole term.

# Example: Σ (x − 2)ⁿ / (n · 3ⁿ)

   |aₙ₊₁/aₙ| = |(x−2)ⁿ⁺¹ / ((n+1)·3ⁿ⁺¹)| · |(n·3ⁿ) / (x−2)ⁿ|
             = |x−2|/3 · n/(n+1)
   limit      = |x−2| / 3

   Converges when  |x−2|/3 < 1   ->   |x − 2| < 3
   RADIUS  R = 3
   so far: 2 − 3 < x < 2 + 3   ->   (−1, 5)

# NOW CHECK BOTH ENDPOINTS SEPARATELY. The ratio test says
# nothing at |x−2| = 3, so substitute each one back in.

   x = 5:  Σ 3ⁿ/(n·3ⁿ) = Σ 1/n        -> harmonic, DIVERGES
   x = −1: Σ (−3)ⁿ/(n·3ⁿ) = Σ (−1)ⁿ/n -> alternating harmonic,
                                          CONVERGES

   INTERVAL of convergence:  [−1, 5)

# Endpoints are where the marks are. The radius is one line of
# algebra; forgetting to test the two ends is the usual error.
```
