import numpy 


def launch_angle(ve_v0, alpha):
    """
    Compute right hand side of equation (17). We will call this x.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius. 
    
    Returns
    -------
    x : float 
        The value of x (RHS of equation (17)).

    Notes
    -----
    This is using the GOPH419 Lab 1 equation numbering system.
    """
    in_sqrt = 1 - (alpha / (1 + alpha)) * (ve_v0 ** 2)
    out_sqrt = 1 + alpha
    x = out_sqrt * numpy.sqrt(in_sqrt)
    return x




def arcsin(x):
    """
    Compute the inverse sine of the x (the RHS of equation (17)).

    Inputs
    ------
    x : float
        This is the RHS of equation (17). This must satisfy 0 <= x <= 1.

    Returns
    -------
    phi : float
        This is the launch angle from vertical in radians.

    Notes
    -----
    This is using the Taylor Series approximation of arcsin. Equation (18) from GOPH419 Lab 1.
    """
    phi = 0.0
    eps_a = 1.0         # This is the approximate relative error.
    tol = 1.0e-16       # This is the stopping criterion.
    n = 1               # This is the current iteration.
    fact_n = 1          # This is the current iteration's respective factorial.
    n_max = 1000        # This is the maximum number of iterations allowed.
    while eps_a > tol and n < n_max:  
        fact_n = fact_n * n 
        def two_fact(c):
            product = 1
            for i in range(1, 2 * c + 1, 1):
                product = product * i
            return product
        dy = ((2 * x) ** (2 * n)) / ((n ** 2) * ((two_fact(n)) / (fact_n ** 2)))  
        phi += dy
        eps_a = abs(dy / phi)
        n = n + 1
    phi = numpy.sqrt(0.5 * phi)
    return phi

        

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """
    Compute the maximum and minimum allowable launch angles for the first stage of the rocket system 

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    tol_alpha : float
        This is the tolerance for maximum altitude.
        
    Returns
    -------
    phi_max : float
        This is the maximum allowable launch angle in radians.
    phi_min : float
        This is the minimum allowable launch angle in radians.

    Notes
    -----
    The function returns the variables in the order (phi_max, phi_min)
    """
    alp_min = (1 + tol_alpha) * alpha
    x_min = launch_angle(ve_v0, alp_min)        
    phi_min = arcsin(x_min)

    alp_max = (1 - tol_alpha) * alpha
    x_max = launch_angle(ve_v0, alp_max)         
    phi_max = arcsin(x_max)
    
    phi_range = numpy.array([phi_min, phi_max])
    return phi_range


        
        









