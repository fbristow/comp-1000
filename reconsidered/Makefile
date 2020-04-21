SHELL   := /bin/bash
SCRIPTS := group-by-outcome.py colour.py

all: COMP1010.html COMP1010.pdf COMP1020.html COMP1500.html COMP1000.pdf COMP1000.html

%.html: %-struct.md $(SCRIPTS)
	pandoc $< -o $@ -F group-by-outcome.py -F colour.py --number-sections \
		--standalone --toc --toc-depth 1 

%.pdf: %-struct.md $(SCRIPTS)
	pandoc $< -o $@ -F group-by-outcome.py -F colour.py --number-sections \
		--standalone --toc --toc-depth 1 --pdf-engine=xelatex

%-struct.md: %.md tags-to-attr.py group-by-outcome.py
	cat <(sed -n '/^---$$/,/^---$$/p' $<) \
		<(pandoc $< -f markdown-auto_identifiers --reference-links \
			     --reference-location=section -F tags-to-attr.py \
				 -F group-by-outcome.py -t markdown+raw_tex) \
				 > $@

# the extra `echo ""` is there because if there's no newline in between
# files, pandoc gobbles up the header that's inserted
COMP-all-struct.md: COMP1010-struct.md COMP1020-struct.md COMP1500-struct.md yamltitletoheaders.py
	cat <(pandoc COMP1010-struct.md -F yamltitletoheaders.py --shift-heading-level-by=1 -t markdown) \
		<(echo "") \
	    <(pandoc COMP1020-struct.md -F yamltitletoheaders.py --shift-heading-level-by=1 -t markdown) \
		<(echo "") \
	    <(pandoc COMP1500-struct.md -F yamltitletoheaders.py --shift-heading-level-by=1 -t markdown) > \
		COMP-all-struct.md

COMP1000.html: COMP-all-struct.md COMP1000.md colour.py nameref.py
	pandoc COMP1000.md COMP-all-struct.md -F nameref.py -F colour.py -o $@ --standalone --toc --toc-depth 2 

COMP1000.pdf: COMP1000.md COMP-all-struct.md colour.py nameref.py
	pandoc COMP1000.md COMP-all-struct.md -F nameref.py -F colour.py -o $@ --standalone --toc --toc-depth 2 \
		   --pdf-engine=xelatex

clean:
	rm -f *.pdf *.html *-struct.md
