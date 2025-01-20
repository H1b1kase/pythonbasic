# from my_package import greet, multiply_numbers
# from my_package import farewell as fw
# greet("김정완")
#
# fw("김정완")
#
# multiply_numbers(2,4)

import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0, 10, 100);

plt.plot(x, numpy.sin(x), label='Sine', color='blue')
plt.show()
