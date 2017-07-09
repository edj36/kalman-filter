from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import numpy as np

"""
http://nbviewer.jupyter.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/04-One-Dimensional-Kalman-Filters.ipynb
"""
def update(prior, measurement):
	x, P = prior        # mean and variance of prior
	z, R = measurement  # mean and variance of measurement

	y = z - x           # residual
	K = P / (P + R)     # Kalman gain

	x = x + K*y         # posterior
	P = (1 - K) * P     # posterior variance
	return x, P

def predict(posterior, movement):
	x, P = posterior # mean and variance of posterior
	dx, Q = movement # mean and variance of movement
	x = x + dx
	P = P + Q
	return x, P

def calculate_initial_mean(prices): return np.mean(prices)

def calculate_initial_var(prices): return (np.std(prices))**2

def calculate_process_var(): return 0.01 

def calculate_sensor_var(prices): return (np.std(prices))**2

def kalman_filter(stock):
	close_prices = np.array(stock.get('Close'))

	initial_mean = calculate_initial_mean(close_prices) # get from some subset of data
	initial_var = calculate_initial_var(close_prices) # get from same ^ subset of data
	x = (initial_mean,initial_var)

	process_var = calculate_process_var() # variance of model (inherent)
	sensor_var = calculate_sensor_var(close_prices) # variance of observations
	process_model = (0, process_var) # 0 mean, white noise, random process (modeling stock as this)

	predictions = []

	for i in close_prices:
		prior = predict(x, process_model)
		x = update(prior, (i, sensor_var))
		predictions.append(prior)

	return [np.random.normal(i,np.sqrt(j)) for i,j in predictions]

















