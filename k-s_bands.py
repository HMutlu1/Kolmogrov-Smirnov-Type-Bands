import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

ata = np.random.exponential(scale=1.0, size=100)

theoretical_distribution = stats.expon()

sorted_data = np.sort(data)

ks_statistic, _ = stats.kstest(sorted_data, theoretical_distribution.cdf)


band_width = 0.1

lower_band = ks_statistic - band_width
upper_band = ks_statistic + band_width

plt.plot(sorted_data, np.linspace(0, 1, len(sorted_data), endpoint=False), label='Empirical Distribution Function')
plt.axvline(sorted_data[np.argmax(sorted_data > lower_band)], color='r', linestyle='--', label='Lower Band')
plt.axvline(sorted_data[np.argmax(sorted_data > upper_band)], color='g', linestyle='--', label='Upper Band')

plt.xlabel('Values')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.title('Kolmogorov-Smirnov Type Bands')
plt.show()
