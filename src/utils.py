from random import normalvariate

def generate_rs_threshold(mu=0.53, sigma=0.25):
    return normalvariate(mu, sigma)