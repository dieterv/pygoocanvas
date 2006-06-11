# require automake-1.7
AUTOMAKE_OPTIONS=1.7

SUBDIRS = demo


INCLUDES = $(PYTHON_INCLUDES) $(GOOCANVAS_CFLAGS) $(PYGTK_CFLAGS) $(GTK_CFLAGS)

EXTRA_DIST = goocanvas.defs goocanvas.override

# goocanvas module
pyexec_LTLIBRARIES = goocanvasmodule.la
goocanvasmodule_la_LDFLAGS = -module -avoid-version -export-symbols-regex initgoocanvas
goocanvasmodule_la_LIBADD = $(GOOCANVAS_LIBS)
goocanvasmodule_la_SOURCES = goocanvasmodule.c 
nodist_goocanvasmodule_la_SOURCES = goocanvas.c
goocanvas.c: goocanvas.defs goocanvas.override
CLEANFILES = goocanvas.c

.defs.c:
	(cd $(srcdir)\
	&& $(PYTHON) $(CODEGEN) \
		--override $*.override \
	    --register @PYGTK_DATADIR@/pygtk/2.0/defs/gdk-types.defs \
	    --register @PYGTK_DATADIR@/pygtk/2.0/defs/pango-types.defs \
	    --register @PYGTK_DATADIR@/pygtk/2.0/defs/gtk-types.defs \
		--prefix py$* $*.defs) > gen-$*.c \
	    && cp gen-$*.c $*.c \
	    && rm -f gen-$*.c
