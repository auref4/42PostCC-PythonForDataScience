from typing import Callable, Iterable, Iterator


def ft_filter(function: Callable[[any], bool], iterable: Iterable) -> Iterator:
    """Applies f to each iteration of i and return an iterator"""
    if function is None:
        return (element for element in iterable if element)
    return (element for element in iterable if function(element))
