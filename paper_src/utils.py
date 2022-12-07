
def flatten(dictionary, level=[]):
    """ Flattens a dictionary by placing '.' between levels.
    This function flattens a hierarchical dictionary by placing '.' 
    between keys at various levels to create a single key for each 
    value. It is used internally for converting the configuration 
    dictionary to more convenient formats. Implementation was 
    inspired by `this StackOverflow post
    <https://stackoverflow.com/questions/6037503/python-unflatten-dict>`_.
    Parameters
    ----------
    dictionary : dict
        The hierarchical dictionary to be flattened.
    level : str, optional
        The string to append to the beginning of this dictionary, 
        enabling recursive calls. By default, an empty string.
    Returns
    -------
    dict
        The flattened dictionary.
    See Also
    --------
    lfads_tf2.utils.unflatten : Performs the opposite of this operation.
    """

    tmp_dict = {}
    for key, val in dictionary.items():
        if type(val) == dict:
            tmp_dict.update(flatten(val, level + [key]))
        else:
            tmp_dict['.'.join(level + [key])] = val
    return tmp_dict
