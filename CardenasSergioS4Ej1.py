import numpy as np
import matplotlib.pyplot as plt
def derivate(f, x, h, method=""):
	if method == "FD":
		return (f(x+h)-f(x))/h
	elif method == "CD":
		return (f(x+h/2.0)-f(x-h/2.0))/h
	elif method == "EP":
		return (8*(f(x+h/4.0)-f(x-h/4))-(f(x+h/2.0)-f(x-h/2.0)))/3.0/h
	else:
		return "method?"

def function(x):
	return np.cos(x)**2

def function_deriv(x):
	return -2*np.cos(x)*np.sin(x)

n = 1000
h_arr = np.linspace(10**-2, 10**-10, n)
x_arr = np.linspace(1, 1, n)

deriv = function_deriv(x_arr)
err_FD = (derivate(function, x_arr, h_arr, "FD")-deriv)/deriv
err_CD = (derivate(function, x_arr, h_arr, "CD")-deriv)/deriv
err_EP = (derivate(function, x_arr, h_arr, "EP")-deriv)/deriv

plt.subplot(311)
plt.plot(h_arr, np.log(abs(err_FD)))
plt.subplot(312)
plt.plot(h_arr, np.log(abs(err_CD)))
plt.subplot(313)
plt.plot(h_arr, np.log(abs(err_EP)))
plt.show()
