all: html json latex pdf

json: latex-ref-label.json example-lists.json attributes.json sections.json
html: latex-ref-label.html example-lists.html attributes.html sections.html
latex: latex-ref-label.tex example-lists.tex attributes.tex sections.tex
pdf: latex-ref-label.pdf example-lists.pdf attributes.pdf sections.pdf

latex-ref-label.html: latex-ref-label.md
	pandoc latex-ref-label.md -o latex-ref-label.html --standalone

latex-ref-label.json: latex-ref-label.md
	pandoc latex-ref-label.md -t json | python3 -mjson.tool > latex-ref-label.json

latex-ref-label.tex: latex-ref-label.md
	pandoc latex-ref-label.md -o latex-ref-label.tex --standalone

latex-ref-label.pdf: latex-ref-label.md
	pandoc latex-ref-label.md -o latex-ref-label.pdf --pdf-engine=xelatex

example-lists.html: example-lists.md
	pandoc example-lists.md -f markdown+example_lists -o example-lists.html --standalone

example-lists.json: example-lists.md
	pandoc example-lists.md -f markdown+example_lists -t json | python3 -mjson.tool > example-lists.json

example-lists.tex: example-lists.md
	pandoc example-lists.md -f markdown+example_lists -o example-lists.tex

example-lists.pdf: example-lists.md
	pandoc example-lists.md -o example-lists.pdf --pdf-engine=xelatex

attributes.html: attributes.md nameref.py list-span.py
	pandoc attributes.md -o attributes.html --standalone -F nameref.py -F list-span.py

attributes.json: attributes.md
	pandoc attributes.md -f markdown -t json | python3 -mjson.tool > attributes.json

attributes.tex: attributes.md nameref.py
	pandoc attributes.md -f markdown -o attributes.tex --standalone -F nameref.py

attributes.pdf: attributes.md nameref.py
	pandoc attributes.md -f markdown -o attributes.pdf --pdf-engine=xelatex -F nameref.py

sections.html: sections.md nameref.py
	pandoc sections.md -o sections.html --standalone --toc --number-sections --number-offset=1010 -F nameref.py

sections.json: sections.md
	pandoc sections.md --toc -t json | python3 -mjson.tool > sections.json

sections.tex: sections.md
	pandoc sections.md -o sections.tex --standalone --toc

sections.pdf: sections.md
	pandoc sections.md -o sections.pdf --pdf-engine=xelatex --toc

clean:
	rm -f *.html *.json *.tex *.pdf
