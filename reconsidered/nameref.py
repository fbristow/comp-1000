#!/usr/bin/python3

import re
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

section = None

def action(elem, doc):

    if isinstance(elem, pf.Plain):
        stringy = pf.stringify(elem)
        matches = ref_pattern.findall(stringy)
        if not matches:
            return elem

        elems = []
        for match in matches:
            # get the ref out of the text (turns "[*header]" into "header"):
            section_id = match[2:-1]
            ref_type = match[1]
            section = None

            # find *any* element that has an ID that matches the one we just extracted
            def matches_id(elem, doc):
                nonlocal section
                if hasattr(elem, 'identifier') and elem.identifier == section_id:
                    section = elem
            doc.walk(matches_id)

            if not section:
                raise NameError(f"Element with ID {section_id} not found in document.")

            course = section.attributes['course']
            outcomes = section.attributes['outcomes']

            if ref_type == '*':
                # Dereferencing type: fill in the learning objective with a link
                # back to the original.
                elems.append(pf.Span(section, pf.Space(),
                        pf.Link(pf.Str(f"({course})"), url=f"#{section_id}"), attributes={
                                 "source-id": section_id}))
            elif ref_type in ('=', '~'):
                # Equivalent to or approximates, just put a link back to the original.
                ref_type = ref_types[ref_type][doc.format]
                elems.append(pf.Space())
                elems.append(pf.Link(pf.Str("("), ref_type, pf.Str(f"{course})"), url=f"#{section_id}",
                        title=f"{course}#{section_id}"))

        return pf.Plain(*elems)
    
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
