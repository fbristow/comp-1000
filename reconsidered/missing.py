#!/usr/bin/python3

import panflute as pf
import itertools
from collections import OrderedDict, defaultdict

referenced_ids = set()
all_ids = OrderedDict()

def prepare(doc):
    pass

def action(elem, doc):
    if isinstance(elem, pf.Span):
        # a span with `referenced-ids` is a *copy*
        if "referenced-ids" in elem.attributes:
            references = elem.attributes["referenced-ids"].split()
            referenced_ids.update(references)

        # a span with an ID is *probably* a learning objective. For
        # capturing all of the identifiers, though, I want to use the
        # **actual** element with the ID, not its copy, so make sure 
        # that this isn't a `pf.Span` that's wrapped in another `pf.Span` 
        # (indicating that it's a copy).
        if elem.identifier and not hasattr(elem.parent, "attributes"):
            all_ids[elem.identifier] = elem

def materialize_unused(doc, unused_ids):
    unused = defaultdict(OrderedDict)
    for unused_id in unused_ids:
        # find the nearest header for that element.
        ancestor = all_ids[unused_id]
        course = ancestor.attributes["course"]
        #### Go to the top of the enclosing list of the pf.ListItem 
        while ancestor.parent is not doc:
            ancestor = ancestor.parent
        #### Spin backwards until you find a header
        while not isinstance(ancestor, pf.Header):
            ancestor = ancestor.prev
        unused[course].setdefault(ancestor, list()).append(all_ids[unused_id])
    return unused

def find_by_id(identifier, doc):
    with_id = None
    def matches_id(elem, doc):
        nonlocal with_id
        if hasattr(elem, 'identifier') and elem.identifier == identifier:
            with_id = elem
    doc.walk(matches_id)
    return with_id
    
def finalize(doc):
    objectives = materialize_unused(doc, all_ids)
    unused_section = find_by_id('missing-objectives', doc)

    spot = itertools.count(start=unused_section.index + 1)

    for course in sorted(objectives):
        doc.content.insert(next(spot), pf.Header(pf.Str(course), level=2))
        for header in objectives[course]:
            unit_list = pf.OrderedList()
            for objective in objectives[course][header]:
                if objective.identifier not in referenced_ids:
                    # we've got a handle on the original `pf.Span`, so ask
                    # for its grandparent to get the `pf.ListItem`.
                    unit_list.content.append(objective.ancestor(2))

            # Only put the header into the document *if* the unit actually
            # has learning objectives that were not referenced.
            if len(unit_list.content):
                doc.content.insert(next(spot), header)
                doc.content.insert(next(spot), unit_list)

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
