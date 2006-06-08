#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <pygobject.h>
#include <pygtk/pygtk.h>
#include <goocanvas-1.0/goocanvas.h>

# include <pycairo/pycairo.h>
Pycairo_CAPI_t *Pycairo_CAPI;


void pygoocanvas_register_classes (PyObject *d); 
void pygoocanvas_add_constants(PyObject *module, const gchar *strip_prefix);

extern PyMethodDef pygoocanvas_functions[];
 
DL_EXPORT (void)
initgoocanvas (void)
{
    PyObject *m, *d;


    Pycairo_IMPORT;
    if (Pycairo_CAPI == NULL)
        return;

    m = Py_InitModule ("goocanvas", pygoocanvas_functions);
    d = PyModule_GetDict (m);
    
    init_pygobject ();
    
    pygoocanvas_register_classes (d);
    pygoocanvas_add_constants(m, "GOO_TYPE_CANVAS_");
	
    if (PyErr_Occurred ())
        Py_FatalError ("can't initialise module goocanvas");
}
