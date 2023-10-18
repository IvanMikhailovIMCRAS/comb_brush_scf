from .topology import mol_script_linear

def create_charge_brush(N: int, 
                        sigma: float,
                        alpha: float,
                        phibulk: float,
                        n_layers: int) -> None:
    if N < 2:
        raise ValueError("N < 3")
    if sigma < 0:
        raise ValueError("sigma < 0")
    if sigma >= 1.0:
        raise ValueError("sigma >= 1")

    theta = N * sigma

    with open('data/brush.in', 'w') as file1:
        file1.writelines(
            f"""
    lat : flat : n_layers : {n_layers}
    lat : flat : geometry : flat
    lat : flat : lambda : 0.16666666666666666667
    lat : flat : lowerbound : surface
    lat : flat : upperbound : mirror1
    lat : flat : bondlength : 6e-10
    
    sys : ivan : temperature : 300

    mon : solid : freedom : frozen
    mon : solid : frozen_range : lowerbound
    
    mon : W : freedom : free
    
    mon : X: freedom : pinned
    mon : X : pinned_range : 1
    mon : X : valence : {alpha}
    
    mon : A : freedom : free
    mon : A : valence : {alpha}
    
    mon : M : freedom : free
    mon : M : valence : -1
    
    mon : P : freedom : free
    mon : P : valence : 1
    
    mol : ionm : composition : (M)1
    mol : ionm : freedom : neutralizer
    
    mol : ionp : composition : (P)1
    mol : ionp : freedom : free
    mol : ionp : phibulk : {phibulk}
    
    mol : solvent : composition : (W)1
    mol : solvent : freedom : solvent

    mol : pol : composition : {mol_script_linear(N)}
    mol : pol : freedom : restricted
    mol : pol : theta : {theta}

    output : filename.pro : type : profiles
    output : filename.pro : template : data/profile.template
    
    newton : mynew : tolerance : 1e-7

    start    
    """
        )


