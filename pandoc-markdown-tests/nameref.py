#!/usr/bin/python3

import panflute as pf

def prepare(doc):
    pass


section = None

def action(elem, doc):

    global section

    nameref = "\\nameref{"
    if isinstance(elem, pf.RawInline) and elem.format == 'tex' and elem.text.startswith(nameref):
        # get the ref out of the text (turns "\nameref{header}" into "header"):
        section_id = elem.text[len(nameref):-1]

        # find *any* element that has an ID that matches the one we just extracted
        def matches_id(elem, doc):
            global section
            if hasattr(elem, 'identifier') and elem.identifier == section_id:
                section = elem
        doc.walk(matches_id)

        # Make a link to that section
        link = pf.Link(pf.Str(pf.stringify(section)), url=f"#{section_id}")
        section = None
        return link
    
def finalize(doc):
    pass

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
