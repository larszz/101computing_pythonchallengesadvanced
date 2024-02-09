# Poem Decoding Challenge - www.101computing.net/poem-decoding-challenge

codebook = {1: "a",
            2: "and",
            3: "as",
            4: "beauty",
            5: "blanketing",
            6: "can't",
            7: "crystal",
            8: "each",
            9: "earth",
            10: "embrace",
            11: "erase",
            12: "falling",
            13: "flake",
            14: "footprints",
            15: "goes",
            16: "it",
            17: "leaving",
            18: "momentary",
            19: "of",
            20: "secrets",
            21: "snow",
            22: "so",
            23: "soft",
            24: "still",
            25: "the",
            26: "thrill",
            27: "time",
            28: "tranquil",
            29: "whispering",
            30: "with",
            31: [12, 21],
            32: [31, 31],
            33: [29, 20, 3, 16, 15],
            34: [32, 33],
            35: [8, 7, 13],
            }

poem = [[29, 21],
        [34],
        [35, 22, 23, 2, 24],
        [5, 25, 9, 30, 1, 28, 26],
        [34],
        [35, 1, 18, 10],
        [17, 14, 19, 4, 27, 6, 11]]


# Complete this code by implementing a recursive function to replace all keys within each verse of the poem with their matching values from the codebook


def get_text_from_codebook(code: int):
    if code not in codebook:
        raise ValueError(f"Code '{code}' not found in codebook!")

    result = codebook[code]
    if isinstance(result, str):
        return result
    if isinstance(result, list):
        return ' '.join([get_text_from_codebook(subcode) for subcode in result])
    raise TypeError(f"Value in codebook has an invalid type: {type(result)}")


def get_poem_as_text(encoded_poem: list[list]) -> str:
    return '\n'.join([' '.join([get_text_from_codebook(word) for word in line]) for line in encoded_poem])


if __name__ == '__main__':
    print(get_poem_as_text(poem))

