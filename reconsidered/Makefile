all: COMP1010.html COMP1010.pdf

COMP1010.html: COMP1010.md tag.py
	pandoc COMP1010.md -o COMP1010.html -F ./tag.py --number-sections --number-offset=1009 --standalone 

COMP1010.pdf: COMP1010.md tag.py
	pandoc COMP1010.md -o COMP1010.pdf -F ./tag.py --number-sections --pdf-engine=xelatex 

clean:
	rm COMP1010.pdf COMP1010.html
