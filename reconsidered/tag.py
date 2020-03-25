#!/usr/bin/python3

import panflute as pf
import sys
from collections import defaultdict 

tags = defaultdict(lambda: [])

def prepare(doc):
    pass

def action(elem, doc):
    wrapped = elem
    if isinstance(elem, pf.Str):
        t = elem.text
        tn = len(t)
        # if it's not an empty string and the text is surrounded by colons
        # (e.g., :likethis:), then it's a tag that we should capture
        if tn > 1 and t[::tn-1] == '::':
            wrapped = pf.Emph(pf.SmallCaps(elem))
            # The tags are written in `pf.Str` elements at the end of a learning
            # objective. The parent is a `pf.Plain` element, and *that* 
            # element's parent is the `pf.ListItem` that I want to append at
            # the end of the document.
            tags[t].append(elem.parent.parent)

    return wrapped

def finalize(doc):
    content = doc.content
    content.append(pf.Header(pf.Str(text="Objectives organized by course outcome"), level=1, classes=['unnumbered'], identifier='organized'))
    for k in tags:
        # turn ":program:" into "Program"
        outcome = k[1:-1].capitalize()
        content.append(pf.Header(pf.Str(text=outcome), level=2, classes=['unnumbered'], identifier=outcome))
        # the list in the dict is already a bunch of `pf.ListItem`, so just add
        # them in a new `pf.OrderedList`
        content.append(pf.OrderedList(*tags[k]))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
