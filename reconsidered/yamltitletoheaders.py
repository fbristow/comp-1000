#!/usr/bin/python3

import panflute as pf


def prepare(doc):
    pass

def action(elem, doc):
    # The title of each document is "COMP XXXX", change it to compxxxx- to use
    # as a prefix for identifiers.
    title = doc.get_metadata('title').lower().replace(" ", "") + "-"
    if hasattr(elem, 'identifier') and elem.identifier:
        elem.identifier = title + elem.identifier

def finalize(doc):
    header = pf.Header(pf.Str(doc.get_metadata('title')), level=2)
    doc.content.insert(0, header)

def main(doc=None):
    return pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc) 


if __name__ == '__main__':
    main()
