BUILDDIR = $(top_builddir)/docs

REF_VERSION = $(PYGOOCANVAS_MAJOR_VERSION).$(PYGOOCANVAS_MINOR_VERSION)
FULL_VERSION = $(REF_VERSION).$(PYGOOCANVAS_MICRO_VERSION)

HTML_STYLE = $(PYGOBJECT_DATADIR)/pygobject/xsl/ref-html-style.xsl
PDF_STYLE = $(PYGOBJECT_DATADIR)/pygobject/xsl/pdf-style.xsl

XMLFILES = 												\
	reference/pygoocanvas-ref.xml						\
	reference/pygoocanvas-hierarchy.xml					\
	reference/pygoocanvas-core-classes.xml				\
	reference/pygoocanvas-std-items.xml					\
    reference/pygoocanvas-model-items.xml				\
    reference/pygoocanvas-misc-items.xml				\
	reference/pygoocanvas-canvas.xml					\
	reference/pygoocanvas-item.xml						\
	reference/pygoocanvas-item-simple.xml				\
    reference/pygoocanvas-item-model.xml				\
    reference/pygoocanvas-item-model-simple.xml			\
    reference/pygoocanvas-style.xml						\
	reference/pygoocanvas-ellipse.xml					\
    reference/pygoocanvas-ellipse-model.xml				\
    reference/pygoocanvas-group.xml						\
    reference/pygoocanvas-group-model.xml				\
	reference/pygoocanvas-image.xml						\
    reference/pygoocanvas-image-model.xml				\
    reference/pygoocanvas-misc.xml						\
	reference/pygoocanvas-path.xml						\
    reference/pygoocanvas-path-model.xml				\
	reference/pygoocanvas-polyline.xml					\
    reference/pygoocanvas-polyline-model.xml			\
	reference/pygoocanvas-rect.xml						\
    reference/pygoocanvas-rect-model.xml				\
	reference/pygoocanvas-text.xml						\
    reference/pygoocanvas-table.xml						\
    reference/pygoocanvas-table-model.xml				\
    reference/pygoocanvas-text-model.xml				\
	reference/pygoocanvas-widget.xml


HTMLdir = $(datadir)/gtk-doc/html/pygoocanvas
HTML_DATA =										\
	html/class-hierarchy.html					\
	html/pygoocanvas-core-classes.html			\
	html/pygoocanvas-std-items.html				\
    html/pygoocanvas-model-items.html			\
    html/pygoocanvas-misc-items.html			\
	html/class-canvas.html						\
	html/class-item.html						\
	html/class-item-simple.html					\
    html/class-item-model.html					\
	html/class-item-model-simple.html			\
    html/class-canvas-style.html				\
	html/class-canvas-ellipse.html				\
    html/class-canvas-ellipse-model.html		\
    html/class-canvas-group.html				\
    html/class-canvas-group-model.html			\
	html/class-canvas-image.html				\
    html/class-canvas-image-model.html			\
    html/class-canvas-misc.html					\
	html/class-canvas-path.html					\
    html/class-canvas-path-model.html			\
	html/class-canvas-polyline.html				\
    html/class-canvas-polyline-model.html		\
	html/class-canvas-rect.html					\
    html/class-canvas-rect-model.html			\
	html/class-canvas-text.html					\
    html/class-canvas-table.html				\
    html/class-canvas-table-model.html			\
    html/class-canvas-text-model.html			\
    html/class-canvas-widget.html				\
	html/index.html								\
	html/index.sgml								\
	html/pygoocanvas.devhelp

CSS_FILES = $(PYGOBJECT_PYGDOCS)/style.css
CSSdir = $(HTMLdir)
CSS_DATA = $(CSS_FILES)

BUILT_SOURCES = 			\
	build_stamp 			\
	reference/builddate.xml	\
	$(HTML_DATA)

CLEANFILES = 				\
	build_stamp 			\
	pygoocanvas-ref.*		\
	reference/builddate.xml	\
	$(HTML_DATA)

EXTRA_DIST = 			\
	$(XMLFILES) 		\
	$(XSLFILES)			\
	$(FIX_XREF)

REFERENCE_DEPS = 		\
	reference 			\
	$(XMLFILES)			\
	$(XSLFILES)

$(HTML_DATA): build_stamp

reference/builddate.xml: $(REFERENCE_DEPS)
	$(PYTHON) -c 'import datetime; print datetime.date.today()' > $@

build_stamp: $(REFERENCE_DEPS)reference/builddate.xml
	xsltproc --nonet --xinclude -o $(BUILDDIR)/html/ \
		 --path $(BUILDDIR)/reference:$(srcdir)/reference \
                 --stringparam gtkdoc.bookname "pygoocanvas" \
                 --stringparam gtkdoc.version ${REF_VERSION} \
                 $(HTML_STYLE) $(srcdir)/reference/pygoocanvas-ref.xml
	$(PYGOBJECT_FIXXREF) -i /usr/share/gtk-doc/html/pygtk/ $(BUILDDIR)/html 
	touch $@

pdf: $(REFERENCE_DEPS) reference/builddate.xml
	xsltproc --nonet --xinclude -o pygoocanvas-ref.fo \
	         $(PDF_STYLE) reference/pygoocanvas-ref.xml
	pdfxmltex pygoocanvas-ref.fo >output </dev/null
