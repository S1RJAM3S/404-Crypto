def bytes2matrix(b: bytes) -> list[list[int]]:
    return [[b[4 * row + col] for col in range(4)] for row in range(4)]

def matrix2bytes(m: list[list[int]]) -> bytes:
    return bytes([b for row in m for b in row])

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
