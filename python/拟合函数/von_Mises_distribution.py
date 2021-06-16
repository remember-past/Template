from scipy.stats import vonmises
kappa = 3
r = vonmises.rvs(kappa, size=1000)
plt.hist(r, normed=True,alpha=0.2)

vonmises.fit(r)
# returns (1.2222011312461918, 0.024913780423670054, 2.4243546157480105e-30)

vonmises.fit(r, loc=0, scale=1)
# returns (1.549290021706847, 0.0013319431181202394, 7.1653626652619939e-29)

vonmises.fit(r, fscale=1)

# https://stackoverflow.com/questions/39020222/python-scipy-how-to-fit-a-von-mises-distribution