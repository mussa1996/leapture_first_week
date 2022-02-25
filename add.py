from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
 double sqrt(double x); // list all the function prototypes from the
 double sin(double x); // library that we want to use
 """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string. This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_my_math",
"""
 #include <math.h> // the C header of the library
""",
library_dirs = [], # here we can provide where the library is located,
 # as we are using C standard library empty list is enough
 libraries = ['m'] # name of the library we want to interface
)

ffibuilder.compile(verbose=True)
