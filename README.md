# Application of Extended Euclidean Algorithm to find Multiplicative Inverse Modulo N

Given two integers 'a' and 'n'

Can we find an 'x' such that **x** \* **a** is congruent to **1** MODULO **n**?

So, 'x' is actually the multiplicative inverse of 'a' modulo 'n' i.e.

```
x = (inverse a) MODULO n
```

Now, we can apply Extended Euclidean Algorithm to calculate: `(inverse a) MODULO n`

**NOTE**:
We can find such an 'x' only when both 'a' and 'n' are co-prime to each other i.e. `gcd(a, n) = 1`

