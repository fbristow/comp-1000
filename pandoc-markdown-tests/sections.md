---
title: Testing sections with pandoc
toccolor: blue
---

Learning Objectives {-}
===================

Making lists with labels
------------------------

By the end of this unit, students should be able to:

### Make a list with some tags {#list-with-tags}

* First item :first:
* Second item :second:
* Third item :third:

### Make another section

* Fourth item

#### Have nested sections

* More deeply detailed sections

Making references to labels
---------------------------

The [Make a list with some tags] that we looked at had (@second-item) underneath it. Then
came (@third-item). Does HTML render anything? Yes, it does!

What about the (@fourth-item)? Can we see that? How about (@fifth-item) and its
child (@sub-item-five)?

What about this neat looking section: \nameref{have-nested-sections}
