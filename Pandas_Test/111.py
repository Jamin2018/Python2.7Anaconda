# -*- coding: utf-8 -*-

import re
s = '123345556abc0'

r = r'\d*'
print(re.match(r,s))