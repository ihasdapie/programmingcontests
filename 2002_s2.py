n = int(input())
d = int(input())

coef = n//d

remainder = n%d

def gcf(top, bottom, trial_factor, ret_factor):

	if trial_factor > bottom:
		return(ret_factor)
	
	elif bottom%trial_factor == 0 and top%trial_factor == 0:
		ret_factor = trial_factor
		return gcf(top, bottom, trial_factor + 1, ret_factor)
	
	else:
		return gcf(top, bottom, trial_factor + 1, ret_factor)


s_factor = gcf(remainder, d, 1, 1)

if remainder == 0:
	print(coef)

if coef == 0:
	print(str(int((remainder/s_factor))) + "/" + str(int((d/s_factor))))


if remainder != 0 and coef != 0:
	print(str(coef)+ " " + str(int((remainder/s_factor))) + "/" + str(int((d/s_factor))))
