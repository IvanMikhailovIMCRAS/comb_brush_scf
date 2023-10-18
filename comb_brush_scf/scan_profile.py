import numpy as np

def read_profile():
    profile = np.loadtxt("data/brush.pro", skiprows=1)
    return profile.T

def first_moment(col: int):
    pass

