# Challenge 2 (Creating a histogram)
import matplotlib.pyplot as plt

nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.hist(nums, bins, color="black")
plt.xlabel("nums")
plt.ylabel("bins")
plt.title("Histogram of nums against bins")
plt.style.use('ggplot')
plt.show()
