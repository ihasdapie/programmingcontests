

def memoize(f):
	mem = {}
	def g(x):
		if x not in mem:
			mem[x] = f(x)
		return mem[x]
	return g

@memoize
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)



print(fib(100))
