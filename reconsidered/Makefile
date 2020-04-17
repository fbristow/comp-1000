SHELL   := /bin/bash
SCRIPTS := group-by-outcome.py colour.py

all: COMP1010.html COMP1010.pdf COMP1020.html COMP1500.html

%.html: %-struct.md $(SCRIPTS)
	pandoc $< -o $@ -F group-by-outcome.py -F colour.py --number-sections \
		--standalone --toc --toc-depth 1 

%.pdf: %-struct.md $(SCRIPTS)
	pandoc $< -o $@ -F group-by-outcome.py -F colour.py --number-sections \
		--standalone --toc --toc-depth 1 --pdf-engine=xelatex

%-struct.md: %.md tags-to-attr.py
	cat <(sed -n '/^---$$/,/^---$$/p' $<) \
		<(pandoc $< -f markdown-auto_identifiers --reference-links \
			     --reference-location=section -F tags-to-attr.py -t markdown) \
				 > $@

# the extra `echo ""` is there because if there's no newline in between
# files, pandoc gobbles up the header that's inserted
COMP1000.html: COMP1010-struct.md COMP1020-struct.md COMP1500-struct.md 
	cat <(pandoc COMP1010-struct.md -F yamltitletoheaders.py --shift-heading-level-by=1 -t markdown) \
		<(echo "") \
	    <(pandoc COMP1020-struct.md -F yamltitletoheaders.py --shift-heading-level-by=1 -t markdown) | \
	pandoc -f markdown -F colour.py -o $@ --standalone --toc --toc-depth 2 -M 'title=COMP 1000' \
		-M date=2020 -M author='Franklin Bristow'

clean:
	rm -f *.pdf *.html *-struct.md
