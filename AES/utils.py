def bytes2matrix(b: bytes) -> list[list[int]]:
    return [[b[4 * row + col] for col in range(4)] for row in range(4)]

def matrix2bytes(m: list[list[int]]) -> bytes:
    return bytes([b for row in m for b in row])
