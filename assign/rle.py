def run_length_decoder(run_lengths):
    """
    Takes a list of tuples representing
    run-length and character and returns
    the expanded representation as a string.

    >>> run_length_decoder([(4, 's')])
    'ssss'

    >>> run_length_decoder([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
    'abbcccdddd'

    >>> run_length_decoder([])
    ''

    """
    expanded_string = ''

    for r in run_lengths:
        run_length, character = r
        expanded_run = run_length * character
        expanded_string = expanded_string + expanded_run

    return expanded_string

def run_length_encoder(s):
    """
    Takes a string and returns a run-length encoded
    representation of the string as a list of 
    2-tuples of run-length and character.

    Examples:

    >>> run_length_encoder('ssss')
    [(4, 's')]

    >>> run_length_encoder('sssbbb')
    [(3, 's'), (3, 'b')]

    >>> run_length_encoder('abbcccdddd')
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

    >>> run_length_encoder('')
    []

    """
    stash = []
    run_length = 0

    # deal with the case of an empty string
    if len(s) > 0:
        prev_char = s[0]
    else:
        return stash

    for idx, char in enumerate(s):

        if char != prev_char:
            stash.append( (run_length, prev_char) )
            prev_char = char
            run_length = 0

        run_length += 1

        if idx == len(s)-1:
            stash.append( (run_length, prev_char) )

    return stash

if __name__ == '__main__':
    
    # run the tests in the docstrings
    import doctest
    doctest.testmod(verbose=True)

