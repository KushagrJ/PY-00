# -*- coding: utf-8 -*-
# Python 3.8.6

import matplotlib.pyplot as plt

figure1 = plt.figure(1)
plt.plot([1, 2, 3, 4])

figure2 = plt.figure(2)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
plt.xlabel("Integers")
plt.ylabel("Squares")

plt.show()





# /* Trivia - 17.py
#
#  * The matplotlib.pyplot module's official documentation calls for the use of
#    plt as an alias.
#  * plt.show() is required to view the graph on this system. On many systems,
#    plt.plot() directly displays the graph. For eg.,
#    import matplotlib.pyplot as plt; plt.plot([1, 2, 3, 4])
#  * 1, 2, 3 & 4 are taken as the y-coordinates in plt.plot([1, 2, 3, 4]).
#  * 1, 2, 3 & 4 and 1, 4, 9 & 16 are taken as the x- and y-coordinates in
#    plt.plot([1, 2, 3, 4], [1, 4, 9, 16]), respectively.
#  * "ro" in plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro") displays the graph as
#    discrete red dots. Other options include "r-" for continuous red lines,
#    "r--" for continuous red dashes, "rs" for discrete red squares, "r^" for
#    discrete red triangles, "r+" for discrete red pluses and "r*" for discrete
#    red stars, among others. The default option is continuous blue lines. The
#    'r' can be replaced with 'b' for blue, 'g' for green, etc.
#
#  * End of Trivia */
