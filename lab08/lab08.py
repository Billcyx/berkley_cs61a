def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    generator_list = []
    index = 0
    g = g()

    element = next(g, None)

    while element != None:
        if index == 0:
            generator_list.append([element])
        else:
            generator_list.append(generator_list[index-1] + [element])
        index = index + 1

        element = next(g, None)

    generator_list = [iter(x) for x in generator_list]

    return generator_list
