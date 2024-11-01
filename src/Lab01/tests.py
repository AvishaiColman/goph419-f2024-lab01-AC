import numpy

    
def test_root(ve_v0, alpha):
    '''
    Function that tests if the combination of velocity ratio and alpha max cause a negative square root to occur.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.

    Returns
    -------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    '''
    further = ((alpha / (1 + alpha)) * (ve_v0 ** 2))
    in_root = 1 - further
    if in_root < 0:
        raise ValueError(f"Your number is {in_root}. Can't take a sqrt of a negative number.")
    else:
        return ve_v0, alpha


    
def test_arcsin(ve_v0, alpha):
    '''
    Function that tests if it is possible to use the arcsin function given the inputed velocity ratio and max alpha.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.

    Returns
    -------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    '''
    x = (1 + alpha) * numpy.sqrt(1 - ((alpha) / (1 + alpha)) * (ve_v0 ** 2))
    if x < 0 or x > 1:
        raise ValueError('Can only compute the arcsin for values between and including 0 and 1.')
    else:
        return ve_v0, alpha
    

    
def test_alpha_min(ve_v0, alpha):
    '''
    Function to determine the minimum allowable alpha for a given velocity ratio.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.

    Returns
    -------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    '''
    if alpha < 0:
        raise ValueError('Alpha cannot be less than 0.')
    else:
        return ve_v0, alpha


def test_alpha_max(ve_v0, alpha):
    '''
    Function to determine the maximum allowable alpha for a given velocity ratio.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.

    Returns
    -------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    '''
    if alpha <= (1 / ((ve_v0 ** 2) - 1)):
        return ve_v0, alpha
    else:
        limit = 1 / ((ve_v0 ** 2) - 1)
        raise ValueError(f'Alpha must be less than or equal to {limit}')

def test_vel_min(ve_v0, alpha):
    '''
    Function to determine the minimum allowable velocity ratio for a given value of alpha.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.

    Returns
    -------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    '''
    if ve_v0 >= numpy.sqrt((alpha + 2) / (alpha + 1)):
        return ve_v0, alpha
    else:
        limit = numpy.sqrt((alpha + 2) / (alpha + 1))
        raise ValueError(f'The minimum velocity ratio must be greater than or equal to {limit}')

def test_vel_max(ve_v0, alpha):
    '''
    Function to determine the maximum allowable velocity ratio for a given value of alpha.

    Inputs
    ------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.

    Returns
    -------
    ve_v0 : float
        This is the ratio of escape velocity (ve) to the maximum initial velocity that the vehicle reaches shortly after launch (v0).
    alpha : float
        This is the target altitude ratio as a fraction of Earth's radius.
    '''
    if ve_v0 <= numpy.sqrt((1 + alpha) / alpha):
        return ve_v0, alpha
    else:
        limit = numpy.sqrt((1 + alpha) / alpha)
        raise ValueError(f'The maximum velocity must be less than or equal to {limit}')
    






    



