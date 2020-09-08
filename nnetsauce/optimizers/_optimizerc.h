/* Generated by Cython 0.29.21 */

#ifndef __PYX_HAVE__nnetsauce__optimizers___optimizerc
#define __PYX_HAVE__nnetsauce__optimizers___optimizerc

#include "Python.h"

#ifndef __PYX_HAVE_API__nnetsauce__optimizers___optimizerc

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C double call_f(PyObject *, PyObject *);
__PYX_EXTERN_C __Pyx_memviewslice calc_grad(PyObject *, PyObject *);
__PYX_EXTERN_C __Pyx_memviewslice calc_hessian(PyObject *, PyObject *);
__PYX_EXTERN_C double calc_learning_rate(PyObject *, __Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice);

#endif /* !__PYX_HAVE_API__nnetsauce__optimizers___optimizerc */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_optimizerc(void);
#else
PyMODINIT_FUNC PyInit__optimizerc(void);
#endif

#endif /* !__PYX_HAVE__nnetsauce__optimizers___optimizerc */
