def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list (matrix-like structure) and display its shape
    before and after slicing.

    This function validates that the input `family` is a well-formed 2D list
    (all rows must be lists of equal length). It then slices the rows from
    index `start` up to, but not including, index `end`, prints the original
    and new shapes, and returns the sliced sublist.

    Parameters
    ----------
    family : list of list
        A 2D list (matrix). Each element must be a list of equal length.
    start : int
        The starting row index (inclusive).
    end : int
        The ending row index (exclusive).

    Returns
    -------
    list of list
        A new 2D list containing the rows of `family` from `start` to `end`.

    Raises
    ------
    TypeError
        If `family` is not a list of lists, or
        if `start`/`end` are not integers.
    ValueError
        If rows in `family` have inconsistent lengths.

    Examples
    --------
    >>> slice_me([[1, 2], [3, 4], [5, 6]], 0, 2)
    My shape is : (3, 2)
    My new shape is : (2, 2)
    [[1, 2], [3, 4]]
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list of lists")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    row = len(family)
    col = 0
    if row > 0:
        if type(family[0]) is not list:
            raise TypeError("family must be a list of lists")
        col = len(family[0])

        for i, r in enumerate(family):
            if type(r) is not list:
                raise TypeError(f"row {i} is not a list")
            if len(r) != col:
                raise ValueError(f"row {i} has length {len(r)} != {col}")

    print(f"My shape is : ({row}, {col})")

    new_family = family[start:end]
    new_row = len(new_family)
    new_col = new_col = col if new_row > 0 else 0
    print(f"My new shape is : ({new_row}, {new_col})")

    return new_family
