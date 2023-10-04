import collections
from typing import Union

NUCLEOTIDES = ["A", "C", "G", "T"]

def validate_seq(seq: str) -> Union[str, bool]:
    """
    Checks that a sequence is valid

    Parameters
    ----------
    seq : str
        The DNA sequence

    Returns
    -------
    str | bool
        Returns the sequence in upper case if it is valid, False otherwise
    """
    seq = seq.upper()
    for nuc in seq:
        if nuc not in NUCLEOTIDES:
            return False
    return seq


def count_freq(seq):
    if validate_seq(seq) is False:
        raise ValueError("The sequence provided is not a valid dna sequence!")
    freq_dict = dict(collections.Counter(seq))
    return f"{freq_dict['A']} {freq_dict['C']} {freq_dict['G']} {freq_dict['T']}"

def dna_to_rna(seq: str):
    if validate_seq(seq) is False:
        raise ValueError("The sequence provided is not a valid dna sequence!")
    return seq.upper().replace("T", "U")