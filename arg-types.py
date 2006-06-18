from argtypes import ArgType, matcher

class CairoMatrixArg(ArgType):

    before = ('    %(name)s = &((PycairoMatrix*)(py_%(name)s))->matrix;\n')

    def write_param(self, ptype, pname, pdflt, pnull, info):
        info.varlist.add('PyObject', '*py_' + pname)
        info.varlist.add('cairo_matrix_t', '*'+pname)
        info.add_parselist('O', ['&py_'+pname], [pname])
        info.arglist.append(pname)
        info.codebefore.append (self.before % { 'name' : pname, 'namecopy' : 'NULL' })


    def write_return(self, ptype, ownsreturn, info):
        info.varlist.add('cairo_matrix_t', '*ret')
        info.codeafter.append('   return PycairoMatrix_FromMatrix(ret);\n');

matcher.register('cairo_matrix_t*', CairoMatrixArg())
