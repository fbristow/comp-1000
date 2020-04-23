#!/usr/bin/python3

import re
import panflute as pf

# e.g., [*link] or [=link-id]
ref_pattern = re.compile("\[[\*=][\w-]+\]")

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
                elems.append(pf.Span(pf.Str(pf.stringify(section)), pf.Space(),
                        pf.Link(pf.Str(f"({course})"),
                            url=f"#{section_id}"), attributes={"outcomes": outcomes}))
            elif ref_type == '=':
                # Equivalent to, just put a link back to the original.
                elems.append(pf.Space())
                elems.append(pf.Link(pf.Str(f"(equiv {course}#{section_id})"), url=f"#{section_id}"))

        return pf.Plain(*elems)
    
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
