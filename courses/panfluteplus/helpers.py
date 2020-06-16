def find_by_id(identifier, elem):
    """
    Find an element below the specified element that has the specified ID.

    :param identifier: the ID that's being searched for
    :param elem: the "root" element to start searching from
    :rtype :class:`Element` | ``None``
    """
    with_id = None
    def _matches_id(e, doc):
        nonlocal with_id
        if hasattr(e, 'identifier') and e.identifier == identifier:
            with_id = e
    elem.walk(_matches_id)
    return with_id
