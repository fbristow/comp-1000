#!/usr/bin/python3

import re
import copy
import panflute as pf
from collections import defaultdict

# e.g., [*link], [=link-id], [~id]
ref_pattern = re.compile("\[[\*=~][\w-]+\]")
ref_types = {
        "~": {
            "latex" : pf.RawInline("$\\approx$", format='tex'),
            "html"  : pf.RawInline("&asymp;")
        },
        "=": defaultdict(lambda: pf.Str("="))
}

def prepare(doc):
    pass

def action(elem, doc):
    if isinstance(elem, pf.ListItem):
        stringy = pf.stringify(elem)
        matches = ref_pattern.findall(stringy)
        if not matches:
            return elem

        elems = []
        referenced_ids = []
        copied_elem = None
        enclosed_span = None

        for match in matches:
            # get the ref out of the text (turns "[*header]" into "header"):
            referenced_id = match[2:-1]
            ref_type = match[1]
            referenced_elem = None
            referenced_ids.append(referenced_id)

            def matches_id(elem, doc):
                nonlocal referenced_elem
                if hasattr(elem, 'identifier') and elem.identifier == referenced_id:
                    referenced_elem = elem
            doc.walk(matches_id)

            if not referenced_elem:
                raise NameError(f"Element with ID {referenced_id} not found in document.")

            course = referenced_elem.attributes['course']
            outcomes = referenced_elem.attributes['outcomes']

            if ref_type == '*':
                # Dereferencing type: fill in the learning objective with a link
                # back to the original.
                assert copied_elem is None
                copied_elem = copy.deepcopy(referenced_elem.ancestor(2))
                referenced_elem = None
                # find the enclosed span with the ID. You know it's already in there,
                # so this should be pretty fast.
                copied_elem.walk(matches_id)
                # referenced_elem should now be the `pf.Span` with the ID
                assert referenced_elem is not None
                enclosed_span = referenced_elem
                referenced_elem.identifier = ""
                referenced_elem.content.append(pf.Space())
                referenced_elem.content.append(pf.Link(pf.Str(f"({course})"), url=f"#{referenced_id}"))
            elif ref_type in ('=', '~'):
                # We **must** already have a `copied_elem`
                assert enclosed_span is not None
                # Equivalent to or approximates, just put a link back to the original.
                ref_type = ref_types[ref_type][doc.format]
                enclosed_span.content.append(pf.Space())
                enclosed_span.content.append(pf.Link(pf.Str("("), ref_type, pf.Str(f"{course})"), url=f"#{referenced_id}",
                        title=pf.stringify(enclosed_span)))

        assert enclosed_span is not None
        enclosed_span.attributes["referenced-ids"] = " ".join(referenced_ids)
        return copied_elem

def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
