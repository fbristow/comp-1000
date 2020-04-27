#!/usr/bin/python3

import panflute as pf
from collections import defaultdict

referenced_ids = set()
all_ids = dict()

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
    
def finalize(doc):
    unused_ids = all_ids.keys() - referenced_ids

    unused = defaultdict(lambda: defaultdict(list))
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
        unused[course][ancestor].append(all_ids[unused_id])

    for course in sorted(unused):
        pf.debug(f"# {course}")
        for header in unused[course]:
            pf.debug(f"## {pf.stringify(header)}")
            for objective in unused[course][header]:
                pf.debug(f"* {pf.stringify(objective)}")
            pf.debug("")
        pf.debug("")

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
