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

def find_by_type(elem_type, elem):
    """
    Find an element below the specified element that has the specified type.

    :param elem_type: the type of element that's being searched for
    :param elem: the "root" element to start searching from
    :rtype :class:`Element` | ``None``
    """
    with_type = None
    def _matches_type(e, doc):
        nonlocal with_type
        if isinstance(e, elem_type):
            with_type = e
    elem.walk(_matches_type)
    return with_type

def find_closest_ancestor_by_type(elem_type, elem):
    """
    Find the closest ancestor of the specified element with the type provided.

    :param elem_type: the type of ancestor we should find.
    :param elem: the "root" element to start searching from
    :rtype :class:`Element` | ``None``
    """
    doc = elem.doc
    found = None

    while not found and elem is not doc:
        elem = elem.parent
        found = isinstance(elem, elem_type)

    if elem is doc:
        return None
    else:
        return elem

def copy_listitem(elem):
    """
    Do a "deep copy" of the pf.ListItem so that we can freely modify this one
    without affecting the original.

    :param elem: the pf.ListItem to copy.
    :rtype :class:`pf.ListItem`
    """
    import panflute as pf
    import json
    assert isinstance(elem, pf.ListItem)
    json_copy = json.dumps(elem, default=lambda e: e.to_json(),
                           check_circular=False, separators=(',', ':'),
                           ensure_ascii=False)
    copy = json.loads(json_copy, object_pairs_hook=pf.elements.from_json)
    copy = pf.ListItem(*copy)
    copy.parent = elem.parent
    return copy
