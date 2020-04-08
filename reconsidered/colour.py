#!/usr/bin/python3

import panflute as pf
import sys
from collections import defaultdict 

colours = [('black', 'cyan'), ('white', 'brown'), ('white', 'darkgray'),
        ('black', 'green'), ('white', 'magenta'), ('white', 'olive'), 
        ('white', 'purple'), ('black', 'teal'), ('white', 'violet'), 
        ('black', 'yellow'), ('white', 'black'), ('white', 'gray')]
labels = set()
colour_idx = 0

def __default_tuple():
    global colour_idx
    v = (colour_idx, [])
    colour_idx += 1
    return v

tags = defaultdict(__default_tuple)
tag_sequence = []

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
            ref = ""
            if "#" in t:
                # if the tag contains an identifier (e.g., :like#this:),
                # then we should extract the identifier (including the #)
                ref = t[t.index("#"):-1]
                # and turn the tag back into a regular tag (:likethis:)
                t = t[:t.index("#")] + ":"

                # a tag should only be added to the sequence and to the end of the file 
                # when it's actually a learning objective
                tag_sequence.append(t)
                # The tags are written in `pf.Str` elements at the end of a learning
                # objective. The parent is a `pf.Plain` element, and *that* 
                # element's parent is the `pf.ListItem` that I want to append at
                # the end of the document.
                tags[t][1].append(elem.ancestor(2))

                if ref in labels:
                    raise ValueError(f"Labels must be unique, {ref} has already been used.")
                else:
                    labels.add(ref)
            tag = tags[t]
            colour = colours[tag[0]%len(colours)]
            if doc.format in ('html', 'html5'):
                wrapped = pf.Span(pf.Span(pf.SmallCaps(pf.Str(t)), attributes={'style': f"color:{colour[0]};background-color:{colour[1]};border:1px solid black;"}))
                wrapped.content.append(pf.Span(pf.Space,pf.Str(ref), attributes={'style': "color:lightgray"}))
            elif doc.format == 'latex':
                wrapped = pf.Span(pf.Span(pf.RawInline(f"\\colorbox{{{colour[1]}}}{{\\color{{{colour[0]}}}{t}}}", format='latex')))
                wrapped.content.append(pf.Span(pf.Space, pf.RawInline("{\\color{gray}", format='latex'), pf.Str(ref), pf.RawInline("}", format='latex')))

    return wrapped

def html_colour_block():
    pass

def latex_colour_block():
    pass

def finalize(doc):
    content = doc.content
    title = doc.get_metadata('title').lower().replace(" ", "") + "-"

    colour_boxes = []
    count = 0
    for t in tag_sequence:
        tag = tags[t]
        #colour = colours[tag[0]]
        colour = colours[tag[0]%len(colours)]
        if doc.format in ('html', 'html5'):
            div = pf.Span(attributes={'style': f"width:4px;height:4px;background-color:{colour[1]};float:left"})
        elif doc.format == 'latex':
            div = pf.RawInline(f"\\colorbox{{{colour[1]}}}{{\makebox[1pt]{{~}}}}", format='latex')
            if count % 60 == 0:
                colour_boxes.append(pf.LineBreak)
            count += 1
        colour_boxes.append(div)

    colour_block = pf.Para(*colour_boxes)
    content.insert(0, colour_block)

    content.append(pf.Header(pf.Str(text="Objectives organized by course outcome"), level=2, classes=['unnumbered'], identifier=title+'organized'))
    for k in tags:
        # turn ":program:" into "Program"
        outcome = k[1:-1].capitalize()
        content.append(pf.Header(pf.Str(text=outcome), level=3, classes=['unnumbered'], identifier=title+outcome))
        # the list in the dict is already a bunch of `pf.ListItem`, so just add
        # them in a new `pf.OrderedList`
        content.append(pf.OrderedList(*tags[k][1]))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
