def bytes2matrix(b: bytes) -> list[list[int]]:
    return [[b[4 * row + col] for col in range(4)] for row in range(4)]

def matrix2bytes(m: list[list[int]]) -> bytes:
    return bytes([b for row in m for b in row])

def bytes2word(b: bytes) -> list[int]:
    return [b[i] for i in range(4)]

def xor_words(w1: list[int], w2: list[int]) -> list[int]:
    return [w1[i] ^ w2[i] for i in range(4)]

def GF_mult(a: int, b: int) -> int:
    res = 0
    for _ in range(8):
        if b & 1:
            res ^= a
        overflow = a & 0x80
        a <<= 1
        if overflow:
            a ^= 0x1B
        b >>= 1
    return res
