# Calculus Cheat Sheet

Generated from the Math domain of the Tech & Life Reference. Every formula also
lives on the site as a flashcard and quiz question.

## Rules — Derivatives

| Rule | Formula |
|---|---|
| Definition | f′(x) = lim_h→0 [f(x+h) − f(x)] / h |
| Power | d/dx xⁿ = n·x^(n−1) |
| Product | (fg)′ = f′g + fg′ |
| Quotient | (f/g)′ = (f′g − fg′) / g² — "low d-high minus high d-low, over low squared" |
| Chain | d/dx f(g(x)) = f′(g(x)) · g′(x) |
| Implicit | Differentiate both sides in x, write dy/dx whenever you differentiate a y, then solve for dy/dx |

## The ones to know cold — Derivatives

| f(x) | f′(x) | f(x) | f′(x) |
|---|---|---|---|
| sin x | cos x | eˣ | eˣ |
| cos x | −sin x | aˣ | aˣ · ln a |
| tan x | sec²x | ln x | 1/x |
| sec x | sec x · tan x | log_a x | 1 / (x · ln a) |
| csc x | −csc x · cot x | arcsin x | 1 / √(1 − x²) |
| cot x | −csc²x | arctan x | 1 / (1 + x²) |

Pattern worth noticing: every co-function derivative (cos, csc, cot) carries a minus sign. That one observation halves what you have to memorise.

## Antiderivatives — every one gets + C — Integrals

| ∫ f(x) dx | Result |
|---|---|
| ∫ xⁿ dx | x^(n+1)/(n+1) + C, for n ≠ −1 |
| ∫ (1/x) dx | ln|x| + C — the absolute value matters |
| ∫ eˣ dx | eˣ + C |
| ∫ aˣ dx | aˣ/ln a + C |
| ∫ sin x dx | −cos x + C |
| ∫ cos x dx | sin x + C |
| ∫ sec²x dx | tan x + C |
| ∫ sec x tan x dx | sec x + C |
| ∫ tan x dx | ln|sec x| + C |
| ∫ sec x dx | ln|sec x + tan x| + C |
| ∫ 1/(1 + x²) dx | arctan x + C |
| ∫ 1/√(1 − x²) dx | arcsin x + C |

## The Fundamental Theorem, and the three techniques — Integrals

| Name | Statement / method |
|---|---|
| FTC Part 1 | d/dx ∫_a^(x) f(t) dt = f(x) — differentiation undoes integration |
| FTC Part 2 | ∫_a^(b) f(x) dx = F(b) − F(a), where F′ = f |
| u-substitution | Reverse chain rule. Pick u = the inside function; you need its derivative present (up to a constant). Change the limits when the integral is definite, or convert back before evaluating |
| By parts | ∫ u dv = uv − ∫ v du. Choose u by LIATE: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential — earliest in the list becomes u |
| Partial fractions | For a rational function with the degree of the numerator lower than the denominator: factor the denominator, split into simpler fractions, integrate each. If the degree is not lower, do polynomial long division first |

## Area, volume, length, average — Applications

| Quantity | Formula |
|---|---|
| Area between curves | ∫_a^(b) (top − bottom) dx |
| Volume — disk | V = π ∫_a^(b) [R(x)]² dx |
| Volume — washer | V = π ∫_a^(b) ([R(x)]² − [r(x)]²) dx — outer squared minus inner squared, not the difference squared |
| Volume — shell | V = 2π ∫_a^(b) x · h(x) dx |
| Arc length | L = ∫_a^(b) √(1 + [f′(x)]²) dx |
| Average value | f_avg = 1/(b−a) · ∫_a^(b) f(x) dx |

## Convergence tests and the four Maclaurin series — Series

| Test | Verdict |
|---|---|
| nth-term (divergence) | If lim a_n ≠ 0, it diverges. If the limit is 0, this test says nothing |
| Geometric Σ a·rⁿ | Converges iff |r| < 1, to a/(1 − r) |
| p-series Σ 1/n^(p) | Converges iff p > 1. So Σ1/n diverges, Σ1/n² converges |
| Ratio test | L = lim |a_n+1/a_n|. L < 1 converges, L > 1 diverges, L = 1 inconclusive |
| Alternating series | Converges if terms decrease in magnitude and tend to 0 |

| Series | Expansion |
|---|---|
| eˣ | Σ xⁿ/n! = 1 + x + x²/2! + x³/3! + … |
| sin x | x − x³/3! + x⁵/5! − … (odd powers) |
| cos x | 1 − x²/2! + x⁴/4! − … (even powers) |
| 1/(1 − x) | 1 + x + x² + x³ + … for |x| < 1 |

Taylor series about a: f(x) = Σ f^((n))(a)·(x − a)ⁿ / n!. A Maclaurin series is just the case a = 0.

## Trig identities and limits you will keep needing — Foundations

| Identity |  |
|---|---|
| Pythagorean | sin²θ + cos²θ = 1 | 1 + tan²θ = sec²θ | 1 + cot²θ = csc²θ |
| Double angle | sin 2θ = 2 sinθ cosθ | cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ |
| Special limits | lim_x→0 (sin x)/x = 1 | lim_x→0 (1 − cos x)/x = 0 |
| L'Hôpital (L'Hopital) | Only for 0/0 or ∞/∞: then lim f/g = lim f′/g′. Check the form every time before applying it |
| Continuity at a | All three: f(a) exists, lim_x→a f(x) exists, and the two are equal |

