#!/usr/bin/python3

import panflute as pf
import sys
from collections import defaultdict 

colours = [('black', '#c8c3cc'), ('white', '#563f46'), ('white', '#8ca3a3'), ('white', '#484f4f'), ('black', '#e0e2e4'), ('black', '#c6bcb6'), ('white', '#96897f'), ('white', '#7efa35'), ('black', '#cab577'), ('black', '#dbceb0'), ('white', '#838060'), ('white', '#4f3222')]
colour_idx = 0

def __default_tuple():
    global colour_idx
    v = (colour_idx, [])
    colour_idx += 1
    return v

tags = defaultdict(__default_tuple)

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
            tag = tags[t]
            colour = colours[tag[0]]
            pf.debug(colour)
            wrapped = pf.Span(pf.SmallCaps(elem), attributes={'style': f"color:{colour[0]};background-color:{colour[1]};border:1px solid black;"})
            # The tags are written in `pf.Str` elements at the end of a learning
            # objective. The parent is a `pf.Plain` element, and *that* 
            # element's parent is the `pf.ListItem` that I want to append at
            # the end of the document.
            tags[t][1].append(elem.parent.parent)

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
        content.append(pf.OrderedList(*tags[k][1]))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
