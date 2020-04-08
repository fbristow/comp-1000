#!/usr/bin/python3

import panflute as pf
import sys
import copy
from collections import defaultdict

labels = set()
tags = defaultdict(list)

def prepare(doc):
    pass

def action(elem, doc):
    if isinstance(elem, pf.ListItem):
        pf.debug(f">>>{elem.content}<<<")
        for item in elem.content:
            pf.debug(f"---{item}---")


def _action(elem, doc):
    wrapped = elem
    if isinstance(elem, pf.Str):
        t = elem.text
        tn = len(t)
        # if it's not an empty string and the text is surrounded by colons
        # (e.g., :likethis:), then it's a tag that we should capture
        if tn > 1 and t[::tn-1] == '::':
            ref = ""
            if "#" in t:
                # if the tag contains an identifier (e.g., :like#this:),
                # then we should extract the identifier (including the #)
                ref = t[t.index("#"):-1]
                # and turn the tag back into a regular tag (:likethis:)
                t = t[:t.index("#")] + ":"

                # The tags are written in `pf.Str` elements at the end of a learning
                # objective. The parent is a `pf.Plain` element, and *that* 
                # element's parent is the `pf.ListItem` that I want to append at
                # the end of the document.
                c = copy.copy(elem.ancestor(2))
                c.replace_keyword(elem.text, pf.Str(''))
                pf.debug(f"[[[{elem.text}]]]")
                pf.debug(f">>>{pf.stringify(c)}<<<")
                tags[t].append(c)

                if ref in labels:
                    raise ValueError(f"Labels must be unique, {ref} has already been used.")
                else:
                    labels.add(ref)

    return wrapped

def finalize(doc):
    content = doc.content
    title = doc.get_metadata('title').lower().replace(" ", "") + "-"

    content.append(pf.Header(pf.Str(text="Objectives organized by course outcome"), level=2, classes=['unnumbered'], identifier=title+'organized'))
    for k in tags:
        # turn ":program:" into "Program"
        outcome = k[1:-1].capitalize()
        content.append(pf.Header(pf.Str(text=outcome), level=3, classes=['unnumbered'], identifier=title+outcome))
        # the list in the dict is already a bunch of `pf.ListItem`, so just add
        # them in a new `pf.OrderedList`
        content.append(pf.OrderedList(*tags[k]))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
