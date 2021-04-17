from generate_data import generate_poly_data
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = generate_poly_data([0,1],100,0)
    data.plot(kind='scatter',x='x',y='y',color='blue')
    plt.show()