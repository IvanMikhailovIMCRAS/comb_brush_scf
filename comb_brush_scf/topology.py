def mol_script_comb(N: int, m: int, n: int) -> str:

    if N <= 0:
        raise Exception("N must be > 0")

    if m < 1:
        raise Exception("m must be >= 1")
    if n < 0:
        raise Exception("m must be >= 0")
    if n == 0:
        return f'(X)1(A){N}'
    else:
        return f'(X)1((A){m}[(A){n}]){N//m-1}(A){m}'
    
def mol_script_linear(N: int) -> str:

    if N <= 1:
        raise Exception("N must be > 1")
    return f'(X)1(A){N-1}'