# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import __callback
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


gsl_function_init = __callback.gsl_function_init
gsl_function_init_fdf = __callback.gsl_function_init_fdf
gsl_function_free = __callback.gsl_function_free
gsl_function_free_fdf = __callback.gsl_function_free_fdf
gsl_monte_function_init = __callback.gsl_monte_function_init
gsl_monte_function_free = __callback.gsl_monte_function_free
gsl_monte_plain_integrate = __callback.gsl_monte_plain_integrate
gsl_monte_plain_alloc = __callback.gsl_monte_plain_alloc
gsl_monte_plain_init = __callback.gsl_monte_plain_init
gsl_monte_plain_free = __callback.gsl_monte_plain_free
pygsl_monte_miser_get_min_calls = __callback.pygsl_monte_miser_get_min_calls
pygsl_monte_miser_get_min_calls_per_bisection = __callback.pygsl_monte_miser_get_min_calls_per_bisection
pygsl_monte_miser_get_dither = __callback.pygsl_monte_miser_get_dither
pygsl_monte_miser_get_estimate_frac = __callback.pygsl_monte_miser_get_estimate_frac
pygsl_monte_miser_get_alpha = __callback.pygsl_monte_miser_get_alpha
pygsl_monte_miser_set_min_calls = __callback.pygsl_monte_miser_set_min_calls
pygsl_monte_miser_set_min_calls_per_bisection = __callback.pygsl_monte_miser_set_min_calls_per_bisection
pygsl_monte_miser_set_dither = __callback.pygsl_monte_miser_set_dither
pygsl_monte_miser_set_estimate_frac = __callback.pygsl_monte_miser_set_estimate_frac
pygsl_monte_miser_set_alpha = __callback.pygsl_monte_miser_set_alpha
gsl_monte_miser_integrate = __callback.gsl_monte_miser_integrate
gsl_monte_miser_alloc = __callback.gsl_monte_miser_alloc
gsl_monte_miser_init = __callback.gsl_monte_miser_init
gsl_monte_miser_free = __callback.gsl_monte_miser_free
GSL_VEGAS_MODE_IMPORTANCE = __callback.GSL_VEGAS_MODE_IMPORTANCE
GSL_VEGAS_MODE_IMPORTANCE_ONLY = __callback.GSL_VEGAS_MODE_IMPORTANCE_ONLY
GSL_VEGAS_MODE_STRATIFIED = __callback.GSL_VEGAS_MODE_STRATIFIED
pygsl_monte_vegas_get_result = __callback.pygsl_monte_vegas_get_result
pygsl_monte_vegas_get_sigma = __callback.pygsl_monte_vegas_get_sigma
pygsl_monte_vegas_get_chisq = __callback.pygsl_monte_vegas_get_chisq
pygsl_monte_vegas_get_alpha = __callback.pygsl_monte_vegas_get_alpha
pygsl_monte_vegas_get_iterations = __callback.pygsl_monte_vegas_get_iterations
pygsl_monte_vegas_get_stage = __callback.pygsl_monte_vegas_get_stage
pygsl_monte_vegas_get_mode = __callback.pygsl_monte_vegas_get_mode
pygsl_monte_vegas_get_verbose = __callback.pygsl_monte_vegas_get_verbose
pygsl_monte_vegas_get_ostream = __callback.pygsl_monte_vegas_get_ostream
pygsl_monte_vegas_set_result = __callback.pygsl_monte_vegas_set_result
pygsl_monte_vegas_set_sigma = __callback.pygsl_monte_vegas_set_sigma
pygsl_monte_vegas_set_chisq = __callback.pygsl_monte_vegas_set_chisq
pygsl_monte_vegas_set_alpha = __callback.pygsl_monte_vegas_set_alpha
pygsl_monte_vegas_set_iterations = __callback.pygsl_monte_vegas_set_iterations
pygsl_monte_vegas_set_stage = __callback.pygsl_monte_vegas_set_stage
pygsl_monte_vegas_set_mode = __callback.pygsl_monte_vegas_set_mode
pygsl_monte_vegas_set_verbose = __callback.pygsl_monte_vegas_set_verbose
pygsl_monte_vegas_set_ostream = __callback.pygsl_monte_vegas_set_ostream
gsl_monte_vegas_integrate = __callback.gsl_monte_vegas_integrate
gsl_monte_vegas_alloc = __callback.gsl_monte_vegas_alloc
gsl_monte_vegas_init = __callback.gsl_monte_vegas_init
gsl_monte_vegas_free = __callback.gsl_monte_vegas_free
gsl_root_fsolver_alloc = __callback.gsl_root_fsolver_alloc
gsl_root_fsolver_free = __callback.gsl_root_fsolver_free
gsl_root_fdfsolver_alloc = __callback.gsl_root_fdfsolver_alloc
gsl_root_fdfsolver_free = __callback.gsl_root_fdfsolver_free
gsl_root_fsolver_set = __callback.gsl_root_fsolver_set
gsl_root_fdfsolver_set = __callback.gsl_root_fdfsolver_set
gsl_root_fsolver_name = __callback.gsl_root_fsolver_name
gsl_root_fdfsolver_name = __callback.gsl_root_fdfsolver_name
gsl_root_fsolver_iterate = __callback.gsl_root_fsolver_iterate
gsl_root_fdfsolver_iterate = __callback.gsl_root_fdfsolver_iterate
gsl_root_fsolver_root = __callback.gsl_root_fsolver_root
gsl_root_fdfsolver_root = __callback.gsl_root_fdfsolver_root
gsl_root_fsolver_x_lower = __callback.gsl_root_fsolver_x_lower
gsl_root_fsolver_x_upper = __callback.gsl_root_fsolver_x_upper
gsl_root_test_interval = __callback.gsl_root_test_interval
gsl_root_test_delta = __callback.gsl_root_test_delta
gsl_root_test_residual = __callback.gsl_root_test_residual
gsl_min_fminimizer_alloc = __callback.gsl_min_fminimizer_alloc
gsl_min_fminimizer_set = __callback.gsl_min_fminimizer_set
gsl_min_fminimizer_set_with_values = __callback.gsl_min_fminimizer_set_with_values
gsl_min_fminimizer_free = __callback.gsl_min_fminimizer_free
gsl_min_fminimizer_name = __callback.gsl_min_fminimizer_name
gsl_min_fminimizer_iterate = __callback.gsl_min_fminimizer_iterate
gsl_min_fminimizer_minimum = __callback.gsl_min_fminimizer_minimum
gsl_min_fminimizer_x_upper = __callback.gsl_min_fminimizer_x_upper
gsl_min_fminimizer_x_lower = __callback.gsl_min_fminimizer_x_lower
gsl_min_test_interval = __callback.gsl_min_test_interval
gsl_multiroot_function_init = __callback.gsl_multiroot_function_init
gsl_multiroot_function_init_fdf = __callback.gsl_multiroot_function_init_fdf
gsl_multiroot_function_getf = __callback.gsl_multiroot_function_getf
gsl_multiroot_function_fdf_getf = __callback.gsl_multiroot_function_fdf_getf
gsl_multiroot_function_getx = __callback.gsl_multiroot_function_getx
gsl_multiroot_function_fdf_getx = __callback.gsl_multiroot_function_fdf_getx
gsl_multiroot_function_free = __callback.gsl_multiroot_function_free
gsl_multiroot_function_free_fdf = __callback.gsl_multiroot_function_free_fdf
gsl_multiroot_fsolver_alloc = __callback.gsl_multiroot_fsolver_alloc
gsl_multiroot_fsolver_free = __callback.gsl_multiroot_fsolver_free
gsl_multiroot_fsolver_set = __callback.gsl_multiroot_fsolver_set
gsl_multiroot_fsolver_iterate = __callback.gsl_multiroot_fsolver_iterate
gsl_multiroot_fsolver_name = __callback.gsl_multiroot_fsolver_name
gsl_multiroot_fsolver_root = __callback.gsl_multiroot_fsolver_root
gsl_multiroot_fdfsolver_alloc = __callback.gsl_multiroot_fdfsolver_alloc
gsl_multiroot_fdfsolver_set = __callback.gsl_multiroot_fdfsolver_set
gsl_multiroot_fdfsolver_iterate = __callback.gsl_multiroot_fdfsolver_iterate
gsl_multiroot_fdfsolver_free = __callback.gsl_multiroot_fdfsolver_free
gsl_multiroot_fdfsolver_name = __callback.gsl_multiroot_fdfsolver_name
gsl_multiroot_fdfsolver_root = __callback.gsl_multiroot_fdfsolver_root
gsl_multiroot_test_delta = __callback.gsl_multiroot_test_delta
gsl_multiroot_test_residual = __callback.gsl_multiroot_test_residual
gsl_multimin_function_init = __callback.gsl_multimin_function_init
gsl_multimin_function_init_fdf = __callback.gsl_multimin_function_init_fdf
gsl_multimin_function_free = __callback.gsl_multimin_function_free
gsl_multimin_function_free_fdf = __callback.gsl_multimin_function_free_fdf
gsl_multimin_fminimizer_f = __callback.gsl_multimin_fminimizer_f
gsl_multimin_fminimizer_alloc = __callback.gsl_multimin_fminimizer_alloc
gsl_multimin_fminimizer_set = __callback.gsl_multimin_fminimizer_set
gsl_multimin_fminimizer_free = __callback.gsl_multimin_fminimizer_free
gsl_multimin_fminimizer_name = __callback.gsl_multimin_fminimizer_name
gsl_multimin_fminimizer_iterate = __callback.gsl_multimin_fminimizer_iterate
gsl_multimin_fminimizer_x = __callback.gsl_multimin_fminimizer_x
gsl_multimin_fminimizer_minimum = __callback.gsl_multimin_fminimizer_minimum
gsl_multimin_fminimizer_size = __callback.gsl_multimin_fminimizer_size
gsl_multimin_fdfminimizer_alloc = __callback.gsl_multimin_fdfminimizer_alloc
gsl_multimin_fdfminimizer_set = __callback.gsl_multimin_fdfminimizer_set
gsl_multimin_fdfminimizer_free = __callback.gsl_multimin_fdfminimizer_free
gsl_multimin_fdfminimizer_name = __callback.gsl_multimin_fdfminimizer_name
gsl_multimin_fdfminimizer_iterate = __callback.gsl_multimin_fdfminimizer_iterate
gsl_multimin_fdfminimizer_restart = __callback.gsl_multimin_fdfminimizer_restart
gsl_multimin_test_gradient = __callback.gsl_multimin_test_gradient
gsl_multimin_test_size = __callback.gsl_multimin_test_size
gsl_multimin_fdfminimizer_f = __callback.gsl_multimin_fdfminimizer_f
gsl_multimin_fdfminimizer_x = __callback.gsl_multimin_fdfminimizer_x
gsl_multimin_fdfminimizer_dx = __callback.gsl_multimin_fdfminimizer_dx
gsl_multimin_fdfminimizer_gradient = __callback.gsl_multimin_fdfminimizer_gradient
gsl_multimin_fdfminimizer_minimum = __callback.gsl_multimin_fdfminimizer_minimum
gsl_multifit_function_init = __callback.gsl_multifit_function_init
gsl_multifit_function_init_fdf = __callback.gsl_multifit_function_init_fdf
gsl_multifit_fsolver_getdx = __callback.gsl_multifit_fsolver_getdx
gsl_multifit_fsolver_getx = __callback.gsl_multifit_fsolver_getx
gsl_multifit_fsolver_getf = __callback.gsl_multifit_fsolver_getf
gsl_multifit_fdfsolver_getdx = __callback.gsl_multifit_fdfsolver_getdx
gsl_multifit_fdfsolver_getx = __callback.gsl_multifit_fdfsolver_getx
gsl_multifit_fdfsolver_getf = __callback.gsl_multifit_fdfsolver_getf
gsl_multifit_fdfsolver_getJ = __callback.gsl_multifit_fdfsolver_getJ
gsl_multifit_function_free = __callback.gsl_multifit_function_free
gsl_multifit_function_free_fdf = __callback.gsl_multifit_function_free_fdf
gsl_multifit_fsolver_alloc = __callback.gsl_multifit_fsolver_alloc
gsl_multifit_fsolver_free = __callback.gsl_multifit_fsolver_free
gsl_multifit_fsolver_set = __callback.gsl_multifit_fsolver_set
gsl_multifit_fsolver_iterate = __callback.gsl_multifit_fsolver_iterate
gsl_multifit_fsolver_name = __callback.gsl_multifit_fsolver_name
gsl_multifit_fsolver_position = __callback.gsl_multifit_fsolver_position
gsl_multifit_fdfsolver_alloc = __callback.gsl_multifit_fdfsolver_alloc
gsl_multifit_fdfsolver_set = __callback.gsl_multifit_fdfsolver_set
gsl_multifit_fdfsolver_iterate = __callback.gsl_multifit_fdfsolver_iterate
gsl_multifit_fdfsolver_free = __callback.gsl_multifit_fdfsolver_free
gsl_multifit_fdfsolver_name = __callback.gsl_multifit_fdfsolver_name
gsl_multifit_fdfsolver_position = __callback.gsl_multifit_fdfsolver_position
gsl_multifit_test_delta = __callback.gsl_multifit_test_delta
gsl_multifit_test_gradient = __callback.gsl_multifit_test_gradient
gsl_integration_workspace_alloc = __callback.gsl_integration_workspace_alloc
gsl_integration_workspace_free = __callback.gsl_integration_workspace_free
gsl_integration_workspace_get_size = __callback.gsl_integration_workspace_get_size
gsl_integration_qaws_table_alloc = __callback.gsl_integration_qaws_table_alloc
gsl_integration_qaws_table_set = __callback.gsl_integration_qaws_table_set
gsl_integration_qaws_table_free = __callback.gsl_integration_qaws_table_free
GSL_INTEG_COSINE = __callback.GSL_INTEG_COSINE
GSL_INTEG_SINE = __callback.GSL_INTEG_SINE
gsl_integration_qawo_table_alloc = __callback.gsl_integration_qawo_table_alloc
gsl_integration_qawo_table_set = __callback.gsl_integration_qawo_table_set
gsl_integration_qawo_table_set_length = __callback.gsl_integration_qawo_table_set_length
gsl_integration_qawo_table_free = __callback.gsl_integration_qawo_table_free
GSL_INTEG_GAUSS15 = __callback.GSL_INTEG_GAUSS15
GSL_INTEG_GAUSS21 = __callback.GSL_INTEG_GAUSS21
GSL_INTEG_GAUSS31 = __callback.GSL_INTEG_GAUSS31
GSL_INTEG_GAUSS41 = __callback.GSL_INTEG_GAUSS41
GSL_INTEG_GAUSS51 = __callback.GSL_INTEG_GAUSS51
GSL_INTEG_GAUSS61 = __callback.GSL_INTEG_GAUSS61
gsl_integration_qng = __callback.gsl_integration_qng
gsl_integration_qag = __callback.gsl_integration_qag
gsl_integration_qagi = __callback.gsl_integration_qagi
gsl_integration_qagiu = __callback.gsl_integration_qagiu
gsl_integration_qagil = __callback.gsl_integration_qagil
gsl_integration_qags = __callback.gsl_integration_qags
gsl_integration_qagp = __callback.gsl_integration_qagp
gsl_integration_qawc = __callback.gsl_integration_qawc
gsl_integration_qaws = __callback.gsl_integration_qaws
gsl_integration_qawo = __callback.gsl_integration_qawo
gsl_integration_qawf = __callback.gsl_integration_qawf
gsl_cheb_alloc = __callback.gsl_cheb_alloc
gsl_cheb_free = __callback.gsl_cheb_free
gsl_cheb_init = __callback.gsl_cheb_init
gsl_cheb_eval = __callback.gsl_cheb_eval
gsl_cheb_eval_err = __callback.gsl_cheb_eval_err
gsl_cheb_eval_n = __callback.gsl_cheb_eval_n
gsl_cheb_eval_n_err = __callback.gsl_cheb_eval_n_err
gsl_cheb_calc_deriv = __callback.gsl_cheb_calc_deriv
gsl_cheb_calc_integ = __callback.gsl_cheb_calc_integ
pygsl_cheb_get_coefficients = __callback.pygsl_cheb_get_coefficients
pygsl_cheb_set_coefficients = __callback.pygsl_cheb_set_coefficients
pygsl_cheb_get_a = __callback.pygsl_cheb_get_a
pygsl_cheb_get_b = __callback.pygsl_cheb_get_b
pygsl_cheb_set_a = __callback.pygsl_cheb_set_a
pygsl_cheb_set_b = __callback.pygsl_cheb_set_b
pygsl_cheb_get_order_sp = __callback.pygsl_cheb_get_order_sp
pygsl_cheb_set_order_sp = __callback.pygsl_cheb_set_order_sp
pygsl_cheb_get_f = __callback.pygsl_cheb_get_f
pygsl_cheb_set_f = __callback.pygsl_cheb_set_f
gsl_odeiv_step_alloc = __callback.gsl_odeiv_step_alloc
gsl_odeiv_step_reset = __callback.gsl_odeiv_step_reset
gsl_odeiv_step_free = __callback.gsl_odeiv_step_free
gsl_odeiv_step_name = __callback.gsl_odeiv_step_name
gsl_odeiv_step_order = __callback.gsl_odeiv_step_order
gsl_odeiv_hadj_dec = __callback.gsl_odeiv_hadj_dec
gsl_odeiv_hadj_inc = __callback.gsl_odeiv_hadj_inc
gsl_odeiv_hadj_nil = __callback.gsl_odeiv_hadj_nil
gsl_odeiv_control_alloc = __callback.gsl_odeiv_control_alloc
gsl_odeiv_control_init = __callback.gsl_odeiv_control_init
gsl_odeiv_control_free = __callback.gsl_odeiv_control_free
gsl_odeiv_control_name = __callback.gsl_odeiv_control_name
gsl_odeiv_control_standard_new = __callback.gsl_odeiv_control_standard_new
gsl_odeiv_control_y_new = __callback.gsl_odeiv_control_y_new
gsl_odeiv_control_yp_new = __callback.gsl_odeiv_control_yp_new
gsl_odeiv_evolve_alloc = __callback.gsl_odeiv_evolve_alloc
gsl_odeiv_evolve_reset = __callback.gsl_odeiv_evolve_reset
gsl_odeiv_evolve_free = __callback.gsl_odeiv_evolve_free
gsl_multifit_linear_alloc = __callback.gsl_multifit_linear_alloc
gsl_multifit_linear_free = __callback.gsl_multifit_linear_free
gsl_multifit_linear = __callback.gsl_multifit_linear
gsl_multifit_linear_svd = __callback.gsl_multifit_linear_svd
gsl_multifit_wlinear = __callback.gsl_multifit_wlinear
gsl_multifit_wlinear_svd = __callback.gsl_multifit_wlinear_svd
gsl_multifit_linear_est = __callback.gsl_multifit_linear_est
gsl_multifit_linear_est_matrix = __callback.gsl_multifit_linear_est_matrix
gsl_fit_linear = __callback.gsl_fit_linear
gsl_fit_wlinear = __callback.gsl_fit_wlinear
gsl_fit_linear_est = __callback.gsl_fit_linear_est
gsl_fit_mul = __callback.gsl_fit_mul
gsl_fit_wmul = __callback.gsl_fit_wmul
gsl_fit_mul_est = __callback.gsl_fit_mul_est

cvar = __callback.cvar
gsl_root_fsolver_bisection = cvar.gsl_root_fsolver_bisection
gsl_root_fsolver_brent = cvar.gsl_root_fsolver_brent
gsl_root_fsolver_falsepos = cvar.gsl_root_fsolver_falsepos
gsl_root_fdfsolver_newton = cvar.gsl_root_fdfsolver_newton
gsl_root_fdfsolver_secant = cvar.gsl_root_fdfsolver_secant
gsl_root_fdfsolver_steffenson = cvar.gsl_root_fdfsolver_steffenson
gsl_min_fminimizer_goldensection = cvar.gsl_min_fminimizer_goldensection
gsl_min_fminimizer_brent = cvar.gsl_min_fminimizer_brent
gsl_multiroot_fsolver_dnewton = cvar.gsl_multiroot_fsolver_dnewton
gsl_multiroot_fsolver_broyden = cvar.gsl_multiroot_fsolver_broyden
gsl_multiroot_fsolver_hybrid = cvar.gsl_multiroot_fsolver_hybrid
gsl_multiroot_fsolver_hybrids = cvar.gsl_multiroot_fsolver_hybrids
gsl_multiroot_fdfsolver_newton = cvar.gsl_multiroot_fdfsolver_newton
gsl_multiroot_fdfsolver_gnewton = cvar.gsl_multiroot_fdfsolver_gnewton
gsl_multiroot_fdfsolver_hybridj = cvar.gsl_multiroot_fdfsolver_hybridj
gsl_multiroot_fdfsolver_hybridsj = cvar.gsl_multiroot_fdfsolver_hybridsj
gsl_multimin_fdfminimizer_steepest_descent = cvar.gsl_multimin_fdfminimizer_steepest_descent
gsl_multimin_fdfminimizer_conjugate_pr = cvar.gsl_multimin_fdfminimizer_conjugate_pr
gsl_multimin_fdfminimizer_conjugate_fr = cvar.gsl_multimin_fdfminimizer_conjugate_fr
gsl_multimin_fdfminimizer_vector_bfgs = cvar.gsl_multimin_fdfminimizer_vector_bfgs
gsl_multimin_fminimizer_nmsimplex = cvar.gsl_multimin_fminimizer_nmsimplex
gsl_multifit_gradient = __callback.gsl_multifit_gradient
gsl_multifit_covar = __callback.gsl_multifit_covar
gsl_multifit_fdfsolver_lmder = cvar.gsl_multifit_fdfsolver_lmder
gsl_multifit_fdfsolver_lmsder = cvar.gsl_multifit_fdfsolver_lmsder
gsl_odeiv_step_rk2 = cvar.gsl_odeiv_step_rk2
gsl_odeiv_step_rk4 = cvar.gsl_odeiv_step_rk4
gsl_odeiv_step_rkf45 = cvar.gsl_odeiv_step_rkf45
gsl_odeiv_step_rkck = cvar.gsl_odeiv_step_rkck
gsl_odeiv_step_rk8pd = cvar.gsl_odeiv_step_rk8pd
gsl_odeiv_step_rk2imp = cvar.gsl_odeiv_step_rk2imp
gsl_odeiv_step_rk4imp = cvar.gsl_odeiv_step_rk4imp
gsl_odeiv_step_bsimp = cvar.gsl_odeiv_step_bsimp
gsl_odeiv_step_gear1 = cvar.gsl_odeiv_step_gear1
gsl_odeiv_step_gear2 = cvar.gsl_odeiv_step_gear2
gsl_odeiv_step_apply = __callback.gsl_odeiv_step_apply
gsl_odeiv_control_hadjust = __callback.gsl_odeiv_control_hadjust
gsl_odeiv_evolve_apply = __callback.gsl_odeiv_evolve_apply
gsl_odeiv_evolve_apply_vector = __callback.gsl_odeiv_evolve_apply_vector
