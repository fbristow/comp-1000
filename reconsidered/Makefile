%.html: %.md tag.py
	pandoc $< -o $@ -F ./tag.py --number-sections --standalone --section-divs

%.pdf: %.md tag.py
	pandoc $< -o $@ -F ./tag.py --number-sections --pdf-engine=xelatex --section-divs

all: COMP1010.html COMP1010.pdf COMP1020.html COMP1020.pdf

clean:
	rm *.pdf *.html
