from typing import Callable, Iterable, Iterator, Any


def ft_filter(function: Callable[[Any], bool], iterable: Iterable) -> Iterator:
    """Applies f to each iteration of i and return an iterator"""

    if function is None:
        # Return iterator of the original list
        return (element for element in iterable if element)

    # Return iterator after the function was applied
    return (element for element in iterable if function(element))
