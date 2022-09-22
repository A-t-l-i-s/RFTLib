from ..Require import *





__all__=["pairing"]





def pairing(num1,num2):
	if (num1>=0):
		num1*=2
	else:
		num1*=-2
		num1-=1


	if (num2>=0):
		num2*=2
	else:
		num2*=-2
		num2-=1


	out=(num1+num2)*(num1+num2+1)/2+num1

	return out




