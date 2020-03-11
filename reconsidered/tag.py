#!/usr/bin/python3

import panflute as pf
import sys
from collections import Counter

tags = Counter()

def prepare(doc):
    pass

def action(elem, doc):
    wrapped = elem
    if isinstance(elem, pf.Str):
        t = elem.text
        tn = len(t)
        if tn > 1 and t[::tn-1] == '::':
            wrapped = pf.Emph(pf.SmallCaps(elem))
            tags[t] += 1

    return wrapped

def finalize(doc):
    tags_list = pf.OrderedList(*[pf.ListItem(pf.Plain(pf.Str(text=f"{k}: {tags[k]}"))) for k in tags])
    doc.content.insert(0, tags_list)
    total_tags = sum(tags.values())
    doc.content.insert(0, pf.Plain(pf.Str(text=str(total_tags))))
    pf.debug(tags.keys())

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
