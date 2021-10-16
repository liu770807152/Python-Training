'''
list 扁平化
'''
list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[k for i in list_ for k in i] #[1, 2, 3, 4, 5, 6, 7, 8, 9]
import numpy as np
print(np.r_[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

import itertools
print(list(itertools.chain(*[[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
sum(list_, [])
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
flatten(list_)
