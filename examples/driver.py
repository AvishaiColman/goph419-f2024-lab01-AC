import numpy
from Lab01.functions import launch_angle_range
from Lab01.tests import *
import matplotlib.pyplot as plt

'''
def main():
    test_root_max(2.0, 0.25, 0.02)
    test_root_min(2.0, 0.25, 0.02)
    test_arcsin_max(2.0, 0.25, 0.02)
    test_arcsin_min(2.0, 0.25, 0.02)
    test_alpha_min(2.0, 0.25)
    test_alpha_max(2.0, 0.25)
    test_vel_min(2.0, 0.25)
    test_vel_max(2.0, 0.25)
    if True:
        return launch_angle_range(2.0, 0.25, 0.02)
    
if __name__ == "__main__":
    print(main())
'''



def main():
    #---------------------------------------------------------------------------------------------------------------------------------
    # ve_v0 = 2.0
    # tol_alpha = 0.04
    
    alpha_vel = (1 / ((2.0 ** 2) - 1))                  # This is the upper bound of alpha

    # Test if the upper bound of alpha is viable to run through the launch angle
    test_alpha_max(2.0, alpha_vel)
    test_alpha_min(2.0, alpha_vel)
    test_root(2.0, alpha_vel)
    test_arcsin(2.0, alpha_vel)
    test_vel_min(2.0, alpha_vel)
    test_vel_max(2.0, alpha_vel)

    # Test if the lower bound of alpha is viable to run through the launch angle
    test_root(2.0, 0)
    test_arcsin(2.0, 0)
    test_alpha_min(2.0, 0)
    test_alpha_max(2.0, 0)
    test_vel_min(2.0, 0)

    alpha = (numpy.arange(0,  alpha_vel, 0.005))         # Creates a list of alpha values given the inputted ve_v0

    LAR_max = []                                        # This is the list of launch angle values for the maximum alpha
    LAR_min = []                                        # This is the list of launch angle values for the minimum alpha

    for i in alpha:
        launch = launch_angle_range(2.0, i, 0.04)
        LAR_max.append(launch[1])                       # Separates the maximum launch angle values from the minumum ones
        LAR_min.append(launch[0])
    
    
    plt.figure()
    plt.xlabel("Alpha")
    plt.ylabel("Launch Angle (phi) in rad")
    plt.plot(alpha, LAR_max, label = 'Maximum Launch Angle')            # This plots the max angle range
    plt.plot(alpha, LAR_min, label = 'Minimum Launch Angle')            # This plots the minimum angle range
    plt.xscale('linear')
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.title("Launch Angle from Vertical vs the Fraction of Earth's Radius Alpha")
    plt.savefig('Launch Angle vs Alpha')
    plt.show()
    
    #-------------------------------------------------------------------------------------------------------------------------------
    # alpha = 0.25
    # tol_alpha = 0.04

    UB_vel = numpy.sqrt((1 + 0.25) / 0.25)            # This is the upper bound of velocity for a given alpha
    LB_vel = numpy.sqrt((0.25 + 2) / (0.25 + 1))      # THis is the lower bound of velocity for a given alpha
    
    # Test if the upper bound of velocity is viable to run through the launch angle range
    test_root(UB_vel - 0.000000000000001, 0.25)         # Subtracting from UB_vel due to floating point error
    test_arcsin(UB_vel, 0.25)
    test_vel_min(UB_vel, 0.25)

    # Tests if the upper bound of velocity is viable to run through the launch angle range
    test_root(LB_vel, 0.25)
    test_arcsin(LB_vel, 0.25)
    test_vel_max(LB_vel, 0.25)

    
    velocity_ratio = numpy.arange(LB_vel, UB_vel, 0.005)

    LARv_max = []
    LARv_min = []

    for i in velocity_ratio:
        launch_2 = launch_angle_range(i, 0.25, 0.04)
        LARv_max.append(launch_2[1])
        LARv_min.append(launch_2[0])
    
    
    plt.figure()
    plt.xlabel('ve/v0')
    plt.ylabel('Launch Angle (phi) in rad')
    plt.plot(velocity_ratio, LARv_max, label = 'Maximum Launch Angle')
    plt.plot(velocity_ratio, LARv_min, label = 'Minimum Launch Angle')
    plt.xscale('linear')
    plt.yscale('linear')
    plt.grid(True)
    plt.legend()
    plt.title("Launch Angle from Vertical vs the Escape Velocity to Initial Velocity Ratio")
    plt.savefig('Launch Angle Velocity Ratio')
    plt.show()
    
    #-------------------------------------------------------------------------------------------------------------------------------
    #Error propagation of equation (17)
    # Using equation (17), find the jacobian matrix for alpha and the velocity ratio
    alpha1 = 0.25
    ve_v0 = 2.0

    in_sqrt = 1 - ((alpha1 / (1 + alpha1)) * (ve_v0 ** 2))
    sinphi_alpha = ((-2 * ve_v0 * alpha1) + (2 * alpha1) - (ve_v0 ** 2) + 2) / ((2 + (2 * alpha1)) * numpy.sqrt(in_sqrt))   # This is the partial derivative of sin(phi) with respect to alpha
    sinphi_ve_v0 = (-alpha1 * ve_v0) / numpy.sqrt(in_sqrt)      # This is the partial derivative of sin(phi) with respect to ve_v0

    #print(sinphi_alpha)
    #print(sinphi_ve_v0)
    J = numpy.array([sinphi_alpha, sinphi_ve_v0])

    J_2_norm = numpy.sqrt((sinphi_alpha ** 2) + (sinphi_ve_v0 ** 2))
    #print(J_2_norm)
    # Now find x
    x = numpy.array([alpha1, ve_v0])

    x_2_norm = numpy.sqrt((alpha1 ** 2) + (ve_v0 ** 2))
    #print(x_2_norm)
    # Now find f
    f = (alpha1 + 1) * numpy.sqrt(in_sqrt)
    #print(f)
    # The condition number can now be calculated

    CN = (x_2_norm * J_2_norm) / f

    if CN >= 0 and CN <= 1:
        condition = 'stable'
    elif CN > 1 and CN <= 10:
        condition = 'semi-stable'
    elif CN > 10:
        condition = 'unstable'
        
    print(f'The condition number of near the points alpha = {alpha1} and ve_v0 = {ve_v0} is {CN}')
    print(f'This indicates that the function is {condition} near these points.')

    # Calculate the magnitude of error of the equation given the input error magnitudes
    delta_alpha1 = 0.02         # Magnitude of error in alpha for input
    delta_ve_v0 = 0.05          # Magnitude of error in ve_v0 for input

    deltax_2_norm = numpy.sqrt((delta_alpha1 **2) + (delta_ve_v0 ** 2))
    deltaf = J_2_norm * deltax_2_norm
    print(f'The magnitude of error in the function is {deltaf}. This is in terms of the error in alpha: {delta_alpha1} and the error in ve_v0: {delta_ve_v0}.')
    
    return 

if __name__ == "__main__":
    main()

