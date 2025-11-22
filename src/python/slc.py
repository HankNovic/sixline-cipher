"""
SixLine Cipher - Python Encoder/Decoder
Spec: SLC-1.0
Author: HankNovic

This module implements the SixLine Cipher (SLC) as defined in:
docs/SLC-1.0-SPEC.md

- Uses 6 vertical-like symbols as base-6 digits:
  0 -> "i"
  1 -> "!"
  2 -> "l"
  3 -> "I"
  4 -> "|"
  5 -> "¦"

- Each encoded unit (letter / digit / some punctuation) is represented
  as a pair of symbols (Symbol Pair), i.e. length 2 string.

- Encoding/decoding rules follow the v1.0 specification.
"""

SYMBOLS = ["i", "!", "l", "I", "|", "¦"]

# Global encode map: char -> symbol pair
ENC_MAP = {}


def _build_tables():
    """
    Build the encoding table according to SLC-1.0 spec.

    Mapping summary:

    A–Z:
        A  (0)  -> 00 -> "ii"
        ...
        Z  (25) -> 41 -> "|!"

    0–9:
        0 (0)   -> 00 -> "ii"
        ...
        9 (9)   -> 13 -> "!I"

    Whitespace & punctuation:
        " " (space) -> 42 -> "|l"
        "."         -> 43 -> "|I"
        ","         -> 44 -> "||"
        "?"         -> 45 -> "|¦"
        "!"         -> 50 -> "¦i"
    """
    # Letters A–Z
    for i in range(26):
        # decimal i -> base-6 (a, b), where i = a*6 + b
        a, b = divmod(i, 6)
        pair = SYMBOLS[a] + SYMBOLS[b]
        ENC_MAP[chr(ord("A") + i)] = pair

    # Digits 0–9
    for i in range(10):
        a, b = divmod(i, 6)
        pair = SYMBOLS[a] + SYMBOLS[b]
        ENC_MAP[str(i)] = pair

    # Whitespace & punctuation (v1.0 recommended mapping)
    ENC_MAP[" "] = "|l"   # space
    ENC_MAP["."] = "|I"   # period
    ENC_MAP[","] = "||"   # comma
    ENC_MAP["?"] = "|¦"   # question mark
    ENC_MAP["!"] = "¦i"   # exclamation mark


_build_tables()

# Build reverse map: symbol pair -> char
DEC_MAP = {v: k for k, v in ENC_MAP.items()}


def encode(text: str, *, sep: str = " ") -> str:
    """
    Encode a plaintext string into SixLine Cipher.

    - All letters are converted to uppercase before encoding.
    - Only characters present in ENC_MAP are supported.
      Unsupported characters raise ValueError.

    Parameters
    ----------
    text : str
        Plaintext input (ASCII letters, digits, space, some punctuation).
    sep : str, optional
        Separator between encoded symbol pairs. Default is a single space.
        Use sep="" for a continuous stream.

    Returns
    -------
    str
        SixLine-encoded string.
    """
    result = []
    upper = text.upper()

    for ch in upper:
        if ch in ENC_MAP:
            result.append(ENC_MAP[ch])
        else:
            raise ValueError(f"Unsupported character for SixLine encoding: {repr(ch)}")

    return sep.join(result)


def _split_pairs(cipher: str) -> list[str]:
    """
    Split cipher text into symbol pairs.

    Supports:
    - Space-separated pairs, e.g. '!! i| !¦'
    - Continuous stream, e.g. '!!i|!¦'

    Returns list of 2-character strings.
    """
    s = cipher.strip()

    if not s:
        return []

    # If there is any whitespace, assume it's already pair-separated.
    tokens = s.split()
    if len(tokens) > 1:
        # All tokens MUST have length 2
        for t in tokens:
            if len(t) != 2:
                raise ValueError(f"Invalid token length (expected 2): {repr(t)}")
        return tokens

    # No whitespace or only one token.
    # Then treat as continuous stream.
    one = tokens[0]
    if len(one) % 2 != 0:
        raise ValueError("Cipher length must be even when using continuous mode.")

    pairs = [one[i:i+2] for i in range(0, len(one), 2)]
    return pairs


def decode(cipher: str) -> str:
    """
    Decode a SixLine Cipher string back to plaintext.

    Supports both:
    - Space-separated symbol pairs: '!! i| !¦ ll'
    - Continuous stream: '!!i|!¦ll'

    Parameters
    ----------
    cipher : str
        SixLine-encoded string.

    Returns
    -------
    str
        Decoded plaintext.

    Raises
    ------
    ValueError
        If an invalid symbol pair is encountered.
    """
    pairs = _split_pairs(cipher)
    out_chars = []

    for pair in pairs:
        if pair in DEC_MAP:
            out_chars.append(DEC_MAP[pair])
        else:
            raise ValueError(f"Invalid SixLine symbol pair: {repr(pair)}")

    return "".join(out_chars)


if __name__ == "__main__":
    # Quick self-test
    sample = "HELLO WORLD"
    enc = encode(sample)
    dec = decode(enc)

    print("Plain :", sample)
    print("Encoded:", enc)
    print("Decoded:", dec)
