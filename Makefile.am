# require automake-1.7
AUTOMAKE_OPTIONS=1.7

SUBDIRS = demo

if ENABLE_DOCS
SUBDIRS += docs
endif

INCLUDES = $(PYTHON_INCLUDES)

EXTRA_DIST =	goocanvas.defs		\
		goocanvas.override	\
		arg-types.py		\
		ChangeLog-pre-git

BUILT_EXTRA_DIST = ChangeLog

# goocanvas module
pyexec_LTLIBRARIES = goocanvasmodule.la
goocanvasmodule_la_LDFLAGS = -module -avoid-version -no-undefined -export-symbols-regex initgoocanvas
goocanvasmodule_la_CFLAGS = $(PYGOOCANVAS_CFLAGS)
goocanvasmodule_la_LIBADD = $(PYGOOCANVAS_LIBS) $(PYTHON_LDFLAGS)
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



pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = pygoocanvas.pc
EXTRA_DIST += pygoocanvas.pc

if PLATFORM_WIN32
# Python .pyd modules are simply DLLs, but they have to be called .pyd for
# python to find them, and libtool only creates .dll.
install-exec-hook:
	mv $(pyexecdir)/goocanvasmodule.dll $(pyexecdir)/goocanvas.pyd
endif

.PHONY: ChangeLog

ChangeLog:
	@echo Creating $@
	@if test -d "$(srcdir)/.git"; then \
	  (GIT_DIR=$(top_srcdir)/.git ./missing --run git log PYGOOCANVAS_0_14_0^^.. --stat) | fmt --split-only > $@.tmp \
	  && mv -f $@.tmp $@ \
	  || ($(RM) $@.tmp; \
	      echo Failed to generate ChangeLog, your ChangeLog may be outdated >&2; \
	      (test -f $@ || echo git-log is required to generate this file >> $@)); \
	else \
	  test -f $@ || \
	  (echo A git checkout and git-log is required to generate ChangeLog >&2 && \
	  echo A git checkout and git-log is required to generate this file >> $@); \
	fi


distclean-local:
	if test $(srcdir) = .; then :; else \
	    rm -f $(BUILT_EXTRA_DIST); \
	fi

dist-hook: $(BUILT_EXTRA_DIST)
	files='$(BUILT_EXTRA_DIST)'; \
	for f in $$files; do \
	  if test -f $$f; then d=.; else d=$(srcdir); fi; \
	  rm -f $(distdir)/$$f && cp $$d/$$f $(distdir) || exit 1; done
