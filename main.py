from utility import *
import copy

dim = get_dimensions()
print(dim)

s_dim = copy.deepcopy(dim)
s_dim[0] += round(dim[2] / 17.66)
s_dim[1] = round(dim[3] / 20.05)
s_dim[2] = round(dim[2] / 1.13)
s_dim[3] = round(dim[3] / 1.05)

sc = get_screenshot(s_dim)
sc.show()