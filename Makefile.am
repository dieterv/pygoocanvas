# require automake-1.7
AUTOMAKE_OPTIONS=1.7

SUBDIRS = demo

if ENABLE_DOCS
SUBDIRS += docs
endif

INCLUDES = $(PYTHON_INCLUDES)

EXTRA_DIST = goocanvas.defs goocanvas.override arg-types.py

# goocanvas module
pyexec_LTLIBRARIES = goocanvasmodule.la
goocanvasmodule_la_LDFLAGS = -module -avoid-version -export-symbols-regex initgoocanvas
goocanvasmodule_la_CFLAGS = $(PYGOOCANVAS_CFLAGS)
goocanvasmodule_la_LIBADD = $(PYGOOCANVAS_LIBS)
goocanvasmodule_la_SOURCES = goocanvasmodule.c 
nodist_goocanvasmodule_la_SOURCES = goocanvas.c
goocanvas.c: goocanvas.defs goocanvas.override arg-types.py
CLEANFILES = goocanvas.c

.defs.c:
	(cd $(srcdir)\
	&& $(PYTHON) $(CODEGEN) \
		--override $*.override \
	    --load-types arg-types.py \
	    --register @PYGTK_DATADIR@/pygtk/2.0/defs/gdk-types.defs \
	    --register @PYGTK_DATADIR@/pygtk/2.0/defs/pango-types.defs \
	    --register @PYGTK_DATADIR@/pygtk/2.0/defs/gtk-types.defs \
		--prefix py$* $*.defs) > gen-$*.c \
	    && cp gen-$*.c $*.c \
	    && rm -f gen-$*.c
