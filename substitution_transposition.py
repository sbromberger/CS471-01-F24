def create_substitution_map(s1: str, s2: str) -> dict[str, str]:
    """ Create a map of plaintext characters to substituted characters. """
    if len(s1) != len(s2):
        raise ValueError("Alphabets s1 and s2 must be the same length")
    s1_uniq = list(set(s1))
    s2_uniq = list(set(s2))

    if len(s1_uniq) != len(s1) or len(s2_uniq) != len(s2):
        raise ValueError("s1 and s2 must each contain unique characters")
    
    return dict(zip(s1, s2))
    
    # A -> F 
    # B -> Z 
    # C -> Q 
    # D -> A

def substitute(message: str, input_alphabet: str, sub_alphabet: str) -> str:
    """ Apply a substitution map function to an input message, yielding ciphertext """
    ciphertext = ""
    if not set(message).issubset(input_alphabet):
        raise ValueError("Message has characters not in input alphabet")
    s_map = create_substitution_map(input_alphabet, sub_alphabet)
    for ch in message:
        ciphertext += s_map[ch]
    return ciphertext

# m = "helloworld"
# c = "abccdedfcg"
# i_a = "helowrd"
# s_a = "abcdefg"

# print(substitute(m, i_a, s_a))


import random

def make_key(m_len: int) -> list[int]:
    """ Given an integer, return a shuffled list of [0..n) """
    randvec = list(range(m_len))  # [0, 1, 2, 3, 4, ... m_len-1]
    random.shuffle(randvec)
    return randvec

def transpose(m: str, k: list[int]) -> str:
    """ Given a plaintext message and a key of shuffled integer indices,
    return the transposition of the plaintext by the key.
    """

    c = ""
    for index in k:
        c += m[index]
    return c

# m = "hello world"
# print(f"{m=}")
# k = make_key(len(m))
# print(f"{k=}")
# c = transpose(m, k)
# print(f"{c=}")




