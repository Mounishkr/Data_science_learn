# **Matplotlib & Seaborn Cheat Sheet**

## **1. Introduction to Matplotlib**
Matplotlib is a Python library for creating static, animated, and interactive visualizations.

### **Installation**
```python
pip install matplotlib
```

### **Basic Plot**
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()
```

### **Features**
- **Versatility**: Supports line plots, bar charts, histograms, etc.
- **Customization**: Control colors, labels, ticks, legends.
- **Integration**: Works with NumPy and Pandas.
- **Publication Quality**: High-resolution plots.

---

## **2. Subplots**
Create multiple plots in a single figure.

### **1D Array of Subplots**
```python
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.subplot(1, 2, 2)  # 2nd plot
plt.plot([1, 2, 3], [6, 5, 4])
plt.show()
```

### **2D Array of Subplots**
```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 1].scatter([1, 2, 3], [4, 5, 6])
axs[1, 0].bar([1, 2, 3], [4, 5, 6])
axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 5])
plt.show()
```

---

## **3. Controlling Axes, Ticks, Labels, Legends**
### **Set Axis Limits**
```python
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xlim(0, 5)  # X-axis range
plt.ylim(0, 35)  # Y-axis range
plt.show()
```

### **Custom Ticks**
```python
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xticks([1, 2, 3, 4], ['One', 'Two', 'Three', 'Four'])
plt.yticks([10, 20, 30], ['Low', 'Medium', 'High'])
plt.show()
```

### **Labels & Title**
```python
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xlabel('X-axis', fontsize=14, color='blue')
plt.ylabel('Y-axis', fontsize=14, color='red')
plt.title('Plot Title', fontsize=16)
plt.show()
```

### **Legends**
```python
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], label='Line 1')
plt.plot([1, 2, 3, 4], [30, 25, 20, 15], label='Line 2')
plt.legend(loc='upper left')
plt.show()
```

---

## **4. Annotations & Saving Plots**
### **Text Annotation**
```python
plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
plt.annotate('Peak', xy=(3, 6), xytext=(4, 7),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.show()
```

### **Save Plot**
```python
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

---

## **5. Seaborn Library**
Seaborn is built on Matplotlib and provides high-level statistical visualizations.

### **Installation**
```python
pip install seaborn
```

### **Scatter Plot**
```python
import seaborn as sns
data = {"x": [1, 2, 3, 4, 5], "y": [2, 5, 3, 8, 10]}
sns.scatterplot(x="x", y="y", data=data)
plt.show()
```

### **Line Plot**
```python
sns.lineplot(x=[1, 2, 3, 4, 5], y=[2, 5, 3, 8, 10])
plt.show()
```

### **Histogram**
```python
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()
```

### **Box Plot**
```python
data = {"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]}
sns.boxplot(data=data)
plt.show()
```

### **Pair Plot**
```python
df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
plt.show()
```

---

## **6. 3D Plots**
### **3D Scatter Plot**
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 2, 3], [2, 4, 6], [3, 6, 9])
plt.show()
```

### **3D Surface Plot**
```python
import numpy as np
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()
```

---

## **7. Playing with Text**
### **Word Cloud**
```python
from wordcloud import WordCloud
text = "Python Matplotlib Seaborn Data Science"
wordcloud = WordCloud(width=800, height=400).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### **Text on Plot**
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.text(2, 5, 'Important Point', fontsize=12, color='red')
plt.show()
```

---

## **Summary of Key Functions**
| **Function**          | **Description**                          |
|-----------------------|------------------------------------------|
| `plt.plot()`          | Line plot                                |
| `plt.scatter()`       | Scatter plot                             |
| `plt.bar()`           | Bar chart                                |
| `plt.hist()`          | Histogram                                |
| `plt.subplots()`      | Multiple subplots                        |
| `plt.xlabel()`        | X-axis label                             |
| `plt.ylabel()`        | Y-axis label                             |
| `plt.title()`         | Plot title                               |
| `plt.legend()`        | Add legend                               |
| `plt.savefig()`       | Save plot                                |
| `sns.scatterplot()`   | Seaborn scatter plot                     |
| `sns.lineplot()`      | Seaborn line plot                        |
| `sns.boxplot()`       | Seaborn box plot                         |
| `sns.pairplot()`      | Seaborn pair plot                        |

---

This cheat sheet covers essential Matplotlib and Seaborn functionalities with examples. Use it for quick reference while working on data visualizations! 🚀
