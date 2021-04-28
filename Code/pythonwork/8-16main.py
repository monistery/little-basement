import b8_16
from b8_16 import input_userinfo
import b8_16 as mn
from b8_16 import input_userinfo as iu
from b8_16 import *

userinfo = b8_16.input_userinfo('zhao', 'jiawei', 'hui',
								age=20,
								rank='mid'
								)

print(userinfo)
userinfo = input_userinfo('bai', 'jicheng',
								age=21,
								rank='high'
								)
print("\n")								
print(userinfo)

userinfo = mn.input_userinfo('yao', 'yuan',
								age=18,
								rank='low'
								)
	
print("\n")								
print(userinfo)

userinfo = iu('tian', 'yi', 'zang',
				age=19,
				rank='mid'
			  )
print("\n")								
print(userinfo)
