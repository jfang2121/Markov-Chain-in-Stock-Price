#calculating the transition matrix value for AMZN
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_excel('AMZN_data.xlsx')

#create daily return from adj close
data['Return'] = data['Adj Close'].pct_change()
print(data)

def classify_return(ret):
    if ret < -0.01:
        return 'Bear'
    if ret >0.01:
        return 'Bull'
    else:
        return 'Stagnant'
    
data['Regime'] = data['Return'].apply(classify_return)
data.dropna(inplace = True)

#create next regime to calculate the percentage of bull bear base in transition matrix
data['Next Regime'] = data['Regime'].shift(-1)
data.dropna(inplace=True)
transition_counts = pd.crosstab(data['Regime'], data['Next Regime'])

# Display the transition count matrix
print(transition_counts)

transition_matrix = transition_counts.div(transition_counts.sum(axis=0), axis=0)
transition_matrix_twodec = transition_matrix.round(3)
print(transition_matrix_twodec)


#plotting return historial line and color red and green
colors = {'Bear': 'red', 'Bull': 'green', 'Stagnant': 'white'}
color_array = data['Regime'].map(colors)

# Plotting historical returns with color-coded regimes
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the background with the regime colors
for i in range(len(data) - 1):
    ax.axvspan(data['Date'].iloc[i], data['Date'].iloc[i + 1], color=color_array.iloc[i], alpha=0.5)

# Overlay the adjusted close price trend line
ax.plot(data['Date'], data['Adj Close'], color='navy', linewidth=2)

# Formatting the plot
ax.set_title('Amazon Historical Returns with Regimes')
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted Close Price')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.show()




#plotting transition matrix heatmap
plt.figure(figsize=(10, 7))
#cividis is color blind friendly
sns.heatmap(transition_matrix_twodec, annot=True,fmt=".3", cmap='cividis')
plt.title('Transition Matrix')
plt.xlabel('Next Regime')
plt.ylabel('Current Regime')
plt.show()

