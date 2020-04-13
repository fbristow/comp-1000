---
title: Testing `\label` and `\ref` from \LaTeX with pandoc.
---

Making lists with labels
------------------------

### Section 1

Here's a list with some labels:

1. First item \label{first-item}
2. \label{second-item} Second item
3. Third item \label{third-item}

### Section 2

1. Fourth item \label{fourth-item}
    1. Sub item in four \label{four-point-one}
2. Fifth item.

Making references to labels
---------------------------

The \ref{first-item} that we looked at had \ref{second-item} underneath it. Then
came \ref{third-item}. Does HTML render anything?

What about the \ref{fourth-item}? Or \ref{four-point-one}?
