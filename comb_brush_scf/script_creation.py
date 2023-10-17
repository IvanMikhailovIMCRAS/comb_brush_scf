

def script_creation(N: int, n: int, m: int, sigma: float) -> None:
    if N < 3:
        raise ValueError("N < 3")
    if n < 0:
        raise ValueError("n < 0")
    if m < 1 and m > N//2:
        raise ValueError("m < 1 and m > N//2")
    if N % m != 0:
        raise ValueError("N % m != 0")
    if sigma < 0:
        raise ValueError("sigma < 0")
    if sigma > (1 + n/m)**(-1):
        raise ValueError("sigma > (1 + n/m)**(-1)")

    theta = (1+N+(N//m-1)*n)*sigma

    with open('data/brush.in', 'w') as file1:
        file1.writelines(
            f"""
    lat : flat : n_layers : {N+n}
    lat : flat : geometry : flat
    lat : flat : lambda : 0.16666666666666666667
    lat : flat : lowerbound : surface
    lat : flat : upperbound : mirror1

    mon : solid : freedom : frozen
    mon : solid : frozen_range : lowerbound
    mon : W : freedom : free
    mon : X: freedom : pinned
    mon : X : pinned_range : 1
    mon : A : freedom : free
    
    mol : solvent : composition : (W)1
    mol : solvent : freedom : solvent

    mol : pol : composition : {mol_script(N, m, n)}
    mol : pol : freedom : restricted
    mol : pol : theta : {theta}

    output : filename.pro : type : profiles
    output : filename.pro : template : data/profile.template

    start
    
    """
        )


def mol_script(N: int, m: int, n: int) -> str:

    if N <= 0:
        raise Exception("N1 must be > 0")

    if m < 1:
        raise Exception("m must be >= 1")
    if n < 0:
        raise Exception("m must be >= 0")
    if n == 0:
        return f'(X)1(A){N}'
    else:
        return f'(X)1((A){m}[(A){n}]){N//m-1}(A){m}'
