all: COMP1010.html COMP1010.pdf

COMP1010.html: COMP1010.md
	pandoc COMP1010.md -o COMP1010.html --number-sections --number-offset=1009 --standalone

COMP1010.pdf: COMP1010.md
	pandoc COMP1010.md -o COMP1010.pdf --number-sections --pdf-engine=xelatex 

clean:
	rm COMP1010.pdf COMP1010.html
