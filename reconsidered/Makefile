%.html: %.md tag.py 
	pandoc $< -o $@ -F ./tag.py --number-sections --standalone --toc --toc-depth 1 

%.pdf: %.md tag.py
	pandoc $< -o $@ -F ./tag.py --number-sections --pdf-engine=xelatex --toc --toc-depth 1

all: COMP1010.html COMP1010.pdf COMP1020.html COMP1020.pdf

clean:
	rm *.pdf *.html
