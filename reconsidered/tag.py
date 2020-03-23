#!/usr/bin/python3

import panflute as pf
import sys
from collections import Counter

tags = Counter()
objective_section = 0
objective_number = 0


### What am I trying to do right now?
#
# I'm trying to figure out how to do two separate things:
#
# 1. How do I collect learning objectives into a `dict` that's keyed on the
#    main learning objective's tag?
#
#    This one I think is actually fairly easy, given the script that I've got
#    written below -- instead of using a counter, just use a plain `dict` with
#    values being `list`s of learning objectives.
# 
#    The problem with this is that you lose context of where the objective came
#    from.
# 2. How do I automate numbering learning objectives so that I can refer to 
#    them across documents?
# 
#    When I generate the learning objectives and outcomes for the new course(s)
#    I want to be able to say "this objective came from this course", and 
#    basically be able to do set arithmetic on the objectives to answer
#    questions like "Which learning objectives *aren't* being covered?"

def prepare(doc):
    pass

def action(elem, doc):
    global objective_section, objective_number
    if isinstance(elem, pf.Header) and elem.level > 1:
        objective_section += 1
        objective_number = 0
        pf.debug(f"Section {objective_section}")
    if objective_section and isinstance(elem, pf.ListItem):
        objective_number += 1
        pf.debug(f"Objective {objective_number}")
    return elem

def _action(elem, doc):
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

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
