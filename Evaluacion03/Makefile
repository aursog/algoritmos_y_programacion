######################
#      Makefile      #
######################

filename=eva03

pdf: 
	xelatex -shell-escape ${filename}
	xelatex -shell-escape ${filename}

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

view:
	while inotifywait --event modify,move_self,close_write ${filename}.tex; \
        do xelatex -shell-escape -halt-on-error ${filename} &&   xelatex -shell-escape -halt-on-error \
            ${filename}; done

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg,snm,toc,nav}
