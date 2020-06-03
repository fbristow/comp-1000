SHELL    = /bin/bash
EXISTING = COMP1010 COMP1020 COMP1500
COURSES  = $(EXISTING) COMP1000
SCRIPTS  = tags-to-attr.py nameref.py colour.py missing.py
SHIFTED_EXISTING = $(addsuffix -shifted.md, $(EXISTING))
TOCDEPTH = 3

# Even though the -shifted.md are listed explicitly as dependencies, they
# should be deleted after the makefile completes.
.INTERMEDIATE: $(SHIFTED_EXISTING)

all: html pdfs 

pdfs: $(addsuffix .pdf, $(COURSES))
html: $(addsuffix .html, $(COURSES))

%.html: %-struct.md colour.py
	pandoc $< -o $@ -F colour.py --number-sections --standalone --toc \
		--toc-depth $(TOCDEPTH) --number-offset=$(@:COMP%.html=%)

%.pdf: %-struct.md colour.py
	pandoc $< -o $@ -F colour.py --number-sections --standalone --toc \
		--toc-depth $(TOCDEPTH) --pdf-engine=xelatex \
		-V header-includes="\usepackage{tocstyle}" \
		-V header-includes="\settocstylefeature{spaceafternumber}{0.5em}" \
		-V header-includes="\usepackage{fullpage}" \
		-V header-includes="\usepackage{tcolorbox}" \
		-V header-includes="\setcounter{section}{$(@:COMP%.pdf=%)}" \
		-V toccolor="blue"

%-struct.md: %.md tags-to-attr.py group-by-outcome.py
	cat <(sed -n '/^---$$/,/^---$$/p' $<) \
		<(pandoc $< -f markdown-auto_identifiers --reference-links \
			     --reference-location=section -F tags-to-attr.py \
				 -F group-by-outcome.py -t markdown) \
		> $@

%-shifted.md: %-struct.md yamltitletoheaders.py
	pandoc $< -F yamltitletoheaders.py --shift-heading-level-by=2 -t markdown \
			  -o $@

COMP1000.html: COMP1000.md $(SHIFTED_EXISTING) $(SCRIPTS)
	pandoc COMP1000.md $(SHIFTED_EXISTING) $(addprefix -F , $(SCRIPTS)) -o $@ \
			--number-sections --standalone --toc --toc-depth $(TOCDEPTH) \
			--number-offset=1000

COMP1000.pdf: COMP1000.md $(SHIFTED_EXISTING) $(SCRIPTS)
	pandoc COMP1000.md $(SHIFTED_EXISTING) $(addprefix -F , $(SCRIPTS)) -o $@ \
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
