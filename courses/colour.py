#!/usr/bin/python3

import panflute as pf
from collections import deque

colours = deque([('black', 'cyan'), ('white', 'brown'), ('white', 'darkgray'),
        ('black', 'green'), ('white', 'magenta'), ('white', 'olive'), 
        ('white', 'purple'), ('black', 'teal'), ('white', 'violet'), 
        ('black', 'yellow'), ('white', 'black'), ('white', 'gray'),
        ('white', 'blue'), ('blue', 'orange'), ('black', 'red')])

collect_tags = False
tag_sequence = []
outcome_colours = dict()
barcodes = []

def prepare(doc):
    pass

def build_course_barcode(doc):
    content = doc.content
    colour_boxes = []
    count = 0
    for t in tag_sequence:
        colour = outcome_colours[t]
        if doc.format in ('html', 'html5'):
            div = pf.Span(attributes={'style': f"width:4px;height:40px;background-color:{colour[1]};float:left"})
        elif doc.format == 'latex':
            div = pf.RawInline(f"\\tcbox[tcbox width=forced center,boxrule=0mm,before=,after=,left=0mm,right=0mm,width=1mm,height=4em,arc=0mm,colframe={colour[1]},colback={colour[1]}]{{}}", format='latex')
        colour_boxes.append(div)

    colour_block = pf.Div(pf.Plain(*colour_boxes), attributes={'style': 'height:45px'})
    barcodes.append((collect_tags, colour_block))

def action(elem, doc):
    global collect_tags, tag_sequence
    if isinstance(elem, pf.Header) and "course-title" in elem.classes and collect_tags:
        # this is a course separator, we should reset state
        build_course_barcode(doc)
        collect_tags = False
        tag_sequence = []
    if isinstance(elem, pf.Header) and pf.stringify(elem) == "Learning objectives":
        collect_tags = elem.index + 1
    if isinstance(elem, pf.Span) and "used-in" in elem.attributes:
        courses = ", ".join(elem.attributes['used-in'].split())
        used_in = pf.Span(pf.Str(f"(Depended on by {courses})"))
        elem.content.append(pf.Space())
        elem.content.append(used_in)
    if isinstance(elem, pf.Span) and "outcomes" in elem.attributes:
        outcomes = elem.attributes["outcomes"].split()
        outcome_spans = []
        for outcome in outcomes:
            # only include outcomes in the sequence if there's an ID
            if collect_tags:
                tag_sequence.append(outcome)

            outcome_spans.append(pf.Space())

            if outcome not in outcome_colours:
                outcome_colours[outcome] = colours.popleft()

            colour = outcome_colours[outcome]
            if doc.format in ('html', 'html5'):
                outcome_spans.append(pf.Span(pf.Str(outcome),
                    attributes={'style': 
                        f"color:{colour[0]};background-color:{colour[1]};border:1px solid black;"}))
            elif doc.format == 'latex':
                outcome_spans.append(pf.Span(
                    pf.RawInline(f"""
                    \\tcbox[on line,arc=0pt, outer arc=0pt,boxsep=0pt,boxrule=1pt,top=2pt,bottom=2pt,left=1pt,right=1pt,colback={colour[1]}]{{
                        \\color{{{colour[0]}}}{outcome}
                    }}
                    """, format='latex')))

        elem.content.extend(outcome_spans)


def finalize(doc):
    content = doc.content

    colour_boxes = []
    count = 0
    for t in tag_sequence:
        colour = outcome_colours[t]
        if doc.format in ('html', 'html5'):
            div = pf.Span(attributes={'style': f"width:4px;height:40px;background-color:{colour[1]};float:left"})
        elif doc.format == 'latex':
            div = pf.RawInline(f"\\tcbox[tcbox width=forced center,boxrule=0mm,before=,after=,left=0mm,right=0mm,width=1mm,height=4em,arc=0mm,colframe={colour[1]},colback={colour[1]}]{{}}", format='latex')
        colour_boxes.append(div)

    colour_block = pf.Div(pf.Plain(*colour_boxes), attributes={'style': 'height:45px'})
    barcodes.append((collect_tags, colour_block))
    
    # Now insert them in reverse order (biggest insertion point first) so that 
    # when we insert things into the document, stuff below doesn't get shifted
    # down.
    barcodes.reverse()
    for (spot, block) in barcodes:
        content.insert(spot, block)

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
