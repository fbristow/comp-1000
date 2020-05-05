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

def prepare(doc):
    pass

def action(elem, doc):
    global collect_tags
    if isinstance(elem, pf.Header) and pf.stringify(elem) == "Learning objectives":
        collect_tags = True
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
                    pf.RawInline(f"\\colorbox{{{colour[1]}}}{{\\color{{{colour[0]}}}{outcome}}}", format='latex')))

        elem.content.extend(outcome_spans)


def finalize(doc):
    content = doc.content
    title = doc.get_metadata('title').lower().replace(" ", "") + "-"

    colour_boxes = []
    count = 0
    for t in tag_sequence:
        colour = outcome_colours[t]
        if doc.format in ('html', 'html5'):
            div = pf.Span(attributes={'style': f"width:4px;height:40px;background-color:{colour[1]};float:left"})
        elif doc.format == 'latex':
            div = pf.RawInline(f"\\colorbox{{{colour[1]}}}{{\\color{{{colour[0]}}}.}}", format='latex')
            # The LaTeX boxes don't wrap automatically. I'm sure there's a nicer way
            # do to this with LaTeX, but I can't be bothered to find out
            if count % 54 == 0:
                colour_boxes.append(pf.LineBreak)
            count += 1
        colour_boxes.append(div)

    colour_block = pf.Div(pf.Plain(*colour_boxes), attributes={'style': 'height:45px'})
    content.insert(0, colour_block)

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)

if __name__ == "__main__":
    main()
