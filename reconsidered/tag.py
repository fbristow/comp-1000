#!/usr/bin/python3

import panflute as pf
import sys

def action(elem, doc):
    wrapped = elem
    if isinstance(elem, pf.Str):
        t = elem.text
        tn = len(t)
        if tn > 1 and t[::tn-1] == '::':
            wrapped = pf.Emph(pf.SmallCaps(elem))

    return wrapped

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
