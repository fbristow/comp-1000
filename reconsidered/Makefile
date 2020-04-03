%.html: %.md tag.py 
	pandoc $< -o $@ -F ./tag.py --number-sections --standalone --toc --toc-depth 1 

%.pdf: %.md tag.py
	pandoc $< -o $@ -F ./tag.py --number-sections --pdf-engine=xelatex --toc --toc-depth 1

all: COMP1010.html COMP1010.pdf COMP1020.html COMP1020.pdf COMP1500.html COMP1500.pdf COMP1000.html

COMP1000.html: COMP1010.md COMP1020.md COMP1500.md
	pandoc COMP1010.md -o COMP1010.html -F tag.py -F ./yamltitletoheaders.py --shift-heading-level-by=1
	pandoc COMP1020.md -o COMP1020.html -F tag.py -F ./yamltitletoheaders.py --shift-heading-level-by=1
	pandoc COMP1500.md -o COMP1500.html -F tag.py -F ./yamltitletoheaders.py --shift-heading-level-by=1
	pandoc COMP1010.html COMP1020.html COMP1500.html --standalone --toc --toc-depth 2 -o COMP1000.html -M 'title=COMP 1000' -M 'date=2020' -M 'author=Franklin Bristow'

COMP1000.pdf: COMP1000.html
	pandoc COMP1000.html -o COMP1000.pdf --pdf-engine=xelatex

clean:
	rm *.pdf *.html
