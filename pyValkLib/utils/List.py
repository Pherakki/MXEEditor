
def chunk_list(self, lst, chunksize):
    """
    Splits a 1D list into sub-lists of size 'chunksize', return returns those sub-lists inside a new 2D list.

    Inputs
    ------
    lst -- a 1D list
    chunksize -- the size of each sub-list of the result

    Returns
    ------
    THe 1D input 'lst' converted to a 2D list, where each sub-list has length 'chunksize'.
    """
    return [lst[i:i + chunksize] for i in range(0, len(lst), chunksize)]

def flatten_list(self, lst):
    return [subitem for item in lst for subitem in item]