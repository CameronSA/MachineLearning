import random
import pandas as pd


# Blur the data in line with a gaussian distribution to make it appear more realistic
def gaussian_blur(mu, sigma):
    return random.gauss(mu, sigma)

# Generates a polynomial function based on the given coefficients and applies it
def apply_function(coeffs, x_coord):
    y_calc = 0
    for n in range(0, len(coeffs)):
        y_calc += coeffs[n]*(x_coord**n)
    print(x_coord,y_calc)
    return y_calc

# Generate n datapoints with some error according to an x order polynomial with a y-intercept.
# coeffs - coefficients of parameter x of a y=mx equation (includes x^0)
# percentage_error - converted to an absolute error on each datapoint by taking the given percentage of the range of datapoints
def generate_poly_data(coeffs, n_points, percentage_error):
    x_coords, y_coords = [],[]

    # Calculate absolute x and y errors
    max_y = apply_function(coeffs, n_points)
    x_error = percentage_error*n_points/100.
    y_error = percentage_error*max_y/100.

    # Generate dataset
    for i in range(0, n_points):
        # Blur the x datapoint
        x_coord = gaussian_blur(i-(n_points/2.), x_error)

        # Build the polynomial function and calculate the y datapoint
        y_calc = apply_function(coeffs, x_coord)

        # Blur the y datapoint
        y_coord = gaussian_blur(y_calc, y_error)

        # Add the datapoints to arrays
        x_coords.append(x_coord)
        y_coords.append(y_coord)

    # Return a table of data
    return pd.DataFrame({'x':x_coords,'y':y_coords})
