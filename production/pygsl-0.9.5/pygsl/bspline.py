# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _bspline
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class bspline(_object):
    """Proxy of C bspline struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, bspline, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, bspline, name)
    __repr__ = _swig_repr
    __swig_getmethods__["cov"] = _bspline.bspline_cov_get
    if _newclass:cov = _swig_property(_bspline.bspline_cov_get)
    __swig_getmethods__["coeffs"] = _bspline.bspline_coeffs_get
    if _newclass:coeffs = _swig_property(_bspline.bspline_coeffs_get)
    __swig_getmethods__["tmp"] = _bspline.bspline_tmp_get
    if _newclass:tmp = _swig_property(_bspline.bspline_tmp_get)
    __swig_getmethods__["w"] = _bspline.bspline_w_get
    if _newclass:w = _swig_property(_bspline.bspline_w_get)
    __swig_getmethods__["knots_a"] = _bspline.bspline_knots_a_get
    if _newclass:knots_a = _swig_property(_bspline.bspline_knots_a_get)
    __swig_getmethods__["coeffs_a"] = _bspline.bspline_coeffs_a_get
    if _newclass:coeffs_a = _swig_property(_bspline.bspline_coeffs_a_get)
    __swig_getmethods__["cov_a"] = _bspline.bspline_cov_a_get
    if _newclass:cov_a = _swig_property(_bspline.bspline_cov_a_get)
    __swig_getmethods__["tmp_a"] = _bspline.bspline_tmp_a_get
    if _newclass:tmp_a = _swig_property(_bspline.bspline_tmp_a_get)
    def __init__(self, *args, **kwargs): 
        """__init__(self, size_t K, size_t NBREAK) -> bspline"""
        this = _bspline.new_bspline(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bspline.delete_bspline
    __del__ = lambda self : None;
    def get_internal_knots(*args, **kwargs):
        """get_internal_knots(self) -> PyObject"""
        return _bspline.bspline_get_internal_knots(*args, **kwargs)

    def knots(*args, **kwargs):
        """knots(self, PyObject knots_o) -> gsl_error_flag_drop"""
        return _bspline.bspline_knots(*args, **kwargs)

    def knots_uniform(*args, **kwargs):
        """knots_uniform(self, double a, double b) -> gsl_error_flag_drop"""
        return _bspline.bspline_knots_uniform(*args, **kwargs)

    def eval_vector(*args, **kwargs):
        """eval_vector(self, gsl_vector IN) -> PyObject"""
        return _bspline.bspline_eval_vector(*args, **kwargs)

    def eval(*args, **kwargs):
        """eval(self, double X) -> PyObject"""
        return _bspline.bspline_eval(*args, **kwargs)

    def set_coefficients_and_covariance_matrix(*args, **kwargs):
        """set_coefficients_and_covariance_matrix(self, PyObject coeffs_o, PyObject cov_o) -> gsl_error_flag_drop"""
        return _bspline.bspline_set_coefficients_and_covariance_matrix(*args, **kwargs)

    def eval_dep(*args, **kwargs):
        """eval_dep(self, double x, double OUT) -> gsl_error_flag_drop"""
        return _bspline.bspline_eval_dep(*args, **kwargs)

    def eval_dep_vector(*args, **kwargs):
        """eval_dep_vector(self, gsl_vector X) -> PyObject"""
        return _bspline.bspline_eval_dep_vector(*args, **kwargs)

    def eval_dep_yerr(*args, **kwargs):
        """eval_dep_yerr(self, double x, double OUT, double OUT2) -> gsl_error_flag_drop"""
        return _bspline.bspline_eval_dep_yerr(*args, **kwargs)

    def eval_dep_yerr_vector(*args, **kwargs):
        """eval_dep_yerr_vector(self, gsl_vector X) -> PyObject"""
        return _bspline.bspline_eval_dep_yerr_vector(*args, **kwargs)

bspline_swigregister = _bspline.bspline_swigregister
bspline_swigregister(bspline)



