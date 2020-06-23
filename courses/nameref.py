#!/usr/bin/python3

import re
import copy
import pickle
import panflute as pf
import panfluteplus as pfp
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
        copied_span = None

        while matches:
            # remove the first element from the list
            match = matches[0]
            matches = matches[1:]
            # get the ref out of the text (turns "[*header]" into "header"):
            referenced_id = match[2:-1]
            ref_type = match[1]
            referenced_ids.append(referenced_id)

            referenced_elem = pfp.find_by_id(referenced_id, doc)

            if not referenced_elem:
                raise NameError(f"Element with ID {referenced_id} not found in document.")

            course = referenced_elem.attributes['course']
            outcomes = referenced_elem.attributes['outcomes']

            if ref_type == '*':
                # Dereferencing type: fill in the learning objective with a link
                # back to the original.
                assert copied_elem is None
                copied_elem = pfp.copy_listitem(referenced_elem.ancestor(2))
                # find the enclosed span with the ID. You know it's already in there,
                # so this should be pretty fast.
                copied_span = pfp.find_by_id(referenced_id, copied_elem)
                # We need to clear out the ID and add a link back to the original
                copied_span.identifier = ""
                copied_span.content.append(pf.Space())
                copied_span.content.append(pf.Link(pf.Str(f"({course})"), url=f"#{referenced_id}"))
                # "recursively" find references in the copied element.
                copied_matches = ref_pattern.findall(pf.stringify(copied_elem))
                matches.extend(copied_matches)
            elif ref_type in ('=', '~'):
                if copied_elem:
                    # if we copied an element, and the copied element has references
                    # in it, we need to remove the reference from the copied element
                    copied_elem.replace_keyword(match, pf.Str(""))
                else:
                    # we're just adding adding equivalencies to a hard-coded
                    # objective, so we have to find the nearest child pf.Span
                    # of the currently inspected pf.ListItem
                    copied_span = pfp.find_by_type(pf.Span, elem)
                    # we need to get rid of the reference if we're doing hard-coded
                    # equivalencies, since we're not replacing an entire element.
                    elem.replace_keyword(match, pf.Str(""))
                
                # Equivalent to or approximates, just put a link back to the original.
                ref_type = ref_types[ref_type][doc.format]
                copied_span.content.append(pf.Space())
                link = pf.Link(pf.Str("("), ref_type, pf.Str(f"{course})"), url=f"#{referenced_id}",
                        title=pf.stringify(referenced_elem))
                copied_span.content.append(link)

        assert copied_span is not None
        copied_span.attributes["referenced-ids"] = " ".join(referenced_ids)
        return copied_elem

def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
