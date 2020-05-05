#!/usr/bin/python3

import panflute as pf
import copy
from collections import defaultdict

objectives = defaultdict(list)
collect_objectives = False

def prepare(doc):
    pass

def action(elem, doc):
    global collect_objectives

    if isinstance(elem, pf.Header) and pf.stringify(elem) == "Learning objectives":
        collect_objectives = True
    # we're explicitly expecting learning objectives to be `pf.Span` that
    # appear after the "Learning objectives" header.
    if isinstance(elem, pf.Span) and collect_objectives:
        # We're interested in collecting the `pf.ListItem` so that we can
        # stuff them into a `pf.OrderedList` later. When we write them out
        # in the collection at the end, we **do not** want them to have any
        # of the metadata, so make a deep copy of the `pf.ListItem` and its
        # children, then strip any metadata from that copy
        listitem = copy.deepcopy(elem.ancestor(2))
        def delete_span_meta(elem, doc):
            if isinstance(elem, pf.Span) and "outcomes" in elem.attributes:
                elem.identifier = ""
                del elem.attributes["outcomes"]
        listitem.walk(delete_span_meta)

        # Learning objectives that have an ID should also have an "outcomes"
        # attribute, we'll use that to put the learning objective into a dict
        outcomes = elem.attributes["outcomes"].split()
        for outcome in outcomes:
            objectives[outcome].append(listitem)

def finalize(doc):
    content = doc.content
    title = doc.get_metadata('title').lower().replace(" ", "") + "-"

    content.append(pf.Header(pf.Str(text="Objectives organized by course outcome"), level=1, classes=['unnumbered'], identifier=title+'organized'))
    for outcome in objectives:
        # turn ":program:" into "Program"
        header = outcome[1:-1].capitalize()
        content.append(pf.Header(pf.Str(text=header), level=2, classes=['unlisted', 'unnumbered'], identifier=title+header))
        # the list in the dict is already a bunch of `pf.ListItem`, so just add
        # them in a new `pf.OrderedList`
        content.append(pf.OrderedList(*objectives[outcome]))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
