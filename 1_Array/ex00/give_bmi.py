def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    """
    Calculate Body Mass Index (BMI) values for given heights and weights.

    Each BMI is computed as:

    BMI = weight / (height * height)

    where `height` is expected in meters and `weight` in kilograms.

    Parameters
    ----------
    height : list of int or float
    A list of heights in meters. Each element must be an `int` or `float`.
    weight : list of int or float
    A list of weights in kilograms. Each element must be an `int` or `float`.

    Returns
    -------
    list of float
    A list of BMI values, corresponding to each (weight, height) pair.

    Raises
    ------
    ValueError
    If `height` and `weight` have different lengths, or if either is empty.
    TypeError
    If any element in `height` or `weight` is not an `int` or `float`.

    Examples
    --------
    >>> give_bmi([1.7, 1.8], [65, 80])
    [22.49134948096886, 24.691358024691358]
    """
    if len(height) != len(weight):
        raise ValueError
    if not height or not weight:
        raise ValueError
    if not all(type(h) is int or type(h) is float for h in height):
        raise TypeError
    if not all(type(w) is int or type(w) is float for w in weight):
        raise TypeError
    return [w / (h * h) for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare BMI values against a given limit and return boolean results.

    Each element in the result indicates whether the corresponding BMI
    value is greater than the specified limit.

    Parameters
    ----------
    bmi : list of int or float
        A list of BMI values. Each element must be an `int` or `float`.
    limit : int
        The threshold BMI value to compare against.

    Returns
    -------
    list of bool
        A list of boolean values, where each element is `True` if the
        corresponding BMI is greater than `limit`, otherwise `False`.

    Raises
    ------
    ValueError
        If `bmi` is an empty list.
    TypeError
        If any element in `bmi` is not an `int` or `float`,
        or if `limit` is not an `int`.

    Examples
    --------
    >>> apply_limit([18.5, 22.0, 27.3], 23)
    [False, False, True]

    >>> apply_limit([20, 30, 25], 25)
    [False, True, False]
    """
    if not bmi:
        raise ValueError
    if not all(type(h) is int or type(h) is float for h in bmi):
        raise TypeError
    if not type(limit) is int:
        raise TypeError
    return [b > limit for b in bmi]
