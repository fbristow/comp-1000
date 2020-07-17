SHELL    = /bin/bash
EXISTING = COMP1010 COMP1020 COMP1500
COURSES  = $(EXISTING) COMP1000
SCRIPTS  = ./scripts/tags-to-attr.py ./scripts/nameref.py ./scripts/colour.py 
SHIFTED_EXISTING = $(addsuffix -shifted.md, $(EXISTING))
TOCDEPTH = 3

# Even though the -shifted.md are listed explicitly as dependencies, they
# should be deleted after the makefile completes.
.INTERMEDIATE: $(SHIFTED_EXISTING)

all: html pdfs 

pdfs: $(addsuffix .pdf, $(COURSES))
html: $(addsuffix .html, $(COURSES))

%.html: %-struct.md ./scripts/colour.py
	pandoc $< -o $@ -F ./scripts/colour.py --number-sections --standalone --toc \
		--toc-depth $(TOCDEPTH) --number-offset=$(@:COMP%.html=%)

%.pdf: %-struct.md ./scripts/colour.py
	pandoc $< -o $@ -F ./scripts/colour.py --number-sections --standalone --toc \
		--toc-depth $(TOCDEPTH) --pdf-engine=xelatex \
		-V header-includes="\usepackage{tocstyle}" \
		-V header-includes="\settocstylefeature{spaceafternumber}{0.5em}" \
		-V header-includes="\usepackage{fullpage}" \
		-V header-includes="\usepackage{tcolorbox}" \
		-V header-includes="\setcounter{section}{$(@:COMP%.pdf=%)}" \
		-V toccolor="blue"

%-struct.md: %.md ./scripts/tags-to-attr.py ./scripts/group-by-outcome.py
	cat <(sed -n '/^---$$/,/^---$$/p' $<) \
		<(pandoc $< -f markdown-auto_identifiers --reference-links \
			     --reference-location=section -F ./scripts/tags-to-attr.py \
				 -F ./scripts/group-by-outcome.py -t markdown) \
		> $@

%-shifted.md: %-struct.md ./scripts/yamltitletoheaders.py
	pandoc $< -F ./scripts/yamltitletoheaders.py --shift-heading-level-by=2 -t markdown \
			  -o $@

COMP1000.html: COMP1000.md appendix.md $(SHIFTED_EXISTING) $(SCRIPTS)
	pandoc COMP1000.md appendix.md $(SHIFTED_EXISTING) $(addprefix -F , $(SCRIPTS)) -o $@ \
			-F ./scripts/missing.py \
			--number-sections --standalone --toc --toc-depth $(TOCDEPTH) \
			--number-offset=1000

COMP1000.pdf: COMP1000.md appendix.tex $(SHIFTED_EXISTING) $(SCRIPTS)
	pandoc COMP1000.md appendix.tex $(SHIFTED_EXISTING) $(addprefix -F , $(SCRIPTS)) -o $@ \
			-F ./scripts/missing.py \
			--standalone --toc --toc-depth $(TOCDEPTH) --pdf-engine=xelatex \
			-V header-includes="\usepackage{tocstyle}" \
			-V header-includes="\settocstylefeature{spaceafternumber}{0.5em}" \
			-V header-includes="\usepackage{fullpage}" \
			-V header-includes="\usepackage{tcolorbox}" \
			-V header-includes="\usepackage{appendix}" \
			-V header-includes="\setcounter{section}{$(@:COMP%.pdf=%)}" \
			-V toccolor="blue" --number-sections

COMP1020.html: COMP1020.md appendix.md COMP1010-shifted.md $(SCRIPTS)
	pandoc COMP1020.md appendix.md COMP1010-shifted.md $(addprefix -F , $(SCRIPTS)) \
		--number-sections --standalone --toc --toc-depth $(TOCDEPTH) \
		--number-offset=1020 -o $@

COMP1020.pdf: COMP1020.md appendix.tex COMP1010-shifted.md $(SCRIPTS)
	pandoc COMP1020.md appendix.tex COMP1010-shifted.md $(addprefix -F , $(SCRIPTS)) -o $@ \
			--standalone --toc --toc-depth $(TOCDEPTH) --pdf-engine=xelatex \
			-V header-includes="\usepackage{tocstyle}" \
			-V header-includes="\settocstylefeature{spaceafternumber}{0.5em}" \
			-V header-includes="\usepackage{fullpage}" \
			-V header-includes="\usepackage{tcolorbox}" \
			-V header-includes="\usepackage{appendix}" \
			-V header-includes="\setcounter{section}{$(@:COMP%.pdf=%)}" \
			-V toccolor="blue" --number-sections

clean:
	rm -f *.pdf *.html 
