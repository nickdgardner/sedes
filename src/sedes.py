import re

def assign(scansion):
    """From a metrical scansion (sequence of (character cluster, preliminary
    metrical analysis, final metrical analysis) tuples as output by
    hexameter.scan.analyze_line_metrical), produce a sequence of (word, sedes)
    tuples."""
    # Output list of tuples.
    result = []
    # List of character cluster making up the current word.
    word = []
    # Sedes of the current word -- the first sedes seen after a word break.
    word_sedes = None
    # Buffer of words seen up until a sedes after a word break. This is needed
    # for sequences like "δ’ ἐτελείετο", where the "δ’" inherits the sedes of
    # the following word.
    words = []
    sedes = 0.0

    # Append a dummy word break at the end of the line, as a sentinel to output
    # the final group of words sharing a sedes.
    if len(scansion) < 1 or " " not in scansion[-1][0]:
        scansion += ((" ", "", ""),)

    for c, _, value in scansion:
        word.append(c)
        if " " in c:
            assert value == "", value
            assert word, word
            # Trim punctuation and spaces from the current word and append it to
            # the list of words that share the current sedes.
            word = "".join(word)
            word = re.sub("^[^\\w\u0313\u0314\u0301\u0342\u0300\u0308\u0345\u0323\u2019]*", "", word)
            word = re.sub("[^\\w\u0313\u0314\u0301\u0342\u0300\u0308\u0345\u0323\u2019]*$", "", word)
            words.append(word)
            if word_sedes is not None:
                # Once we know the sedes, output all the words seen since the
                # last time we saw a sedes.
                for w in words:
                    result.append((w, "{:g}".format(word_sedes)))
                words = []
            word = []
            word_sedes = None

        # If it's a vowel with a sedes value, advance the sedes counter.
        if value == "-":
            sedes += 0.5
        elif value == "+":
            sedes += 1.0
        if (value == "-" or value == "+") and word_sedes is None:
            # The first vowel in a word, remember the sedes for the whole word.
            word_sedes = sedes
    assert sedes == 12.0, sedes
    assert not word, word
    assert not words, words
    assert word_sedes is None, word_sedes
    return tuple(result)
