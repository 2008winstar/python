def gcd(p, q):
    """求最大公约数"""

    return p if q == 0 else gcd(q, p % q)


print(gcd(120, 20))
