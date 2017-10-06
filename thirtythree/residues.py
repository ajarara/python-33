

def least_residue_system(modulus, exponent):
    return {i: pow(i, exponent, modulus) for i in range(modulus)}


def is_injection(mapping):
    had = set()
    for key, value in mapping.items():
        if value in had:
            return False
        had.add(value)
    return True


def invert_dict(d):
    assert is_injection(d)
    return {value: key for key, value in d.items()}


