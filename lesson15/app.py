import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("weather_tokyo_data.csv")

# 🧼 pastro kolonat
df.columns = df.columns.str.strip().str.lower()

# -------------------------------
# FIX 1: krijo date nga year + day
# -------------------------------
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['day'])

# -------------------------------
# FIX 2: pastro temperature (ke hapësira)
# -------------------------------
df['temperature'] = df['temperature'].astype(str).str.strip().str.replace('(', '').str.replace(')', '')
df['temperature'] = df['temperature'].astype(float)

# -------------------------------
# 1. Temperature Overview
# -------------------------------
avg_temp = df['temperature'].mean()
print(f"Average Temperature: {avg_temp:.2f}°C")

# -------------------------------
# 2. Monthly Temperature
# -------------------------------
df['month'] = df['date'].dt.month

monthly_avg = df.groupby('month')['temperature'].mean()
print("\nMonthly Average Temperature:")
print(monthly_avg)

plt.figure(figsize=(8,5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Highs and Lows
# -------------------------------
hottest_day = df.loc[df['temperature'].idxmax()]
coldest_day = df.loc[df['temperature'].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)

# -------------------------------
# 4. Temperature Trends
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'], marker='o')
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Seasonal Average Temperature
# -------------------------------
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df['season'] = df['month'].apply(get_season)

seasonal_avg = df.groupby('season')['temperature'].mean()

print("\nSeasonal Average Temperature:")
print(seasonal_avg)

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("weather_tokyo_data.csv")

df.columns = df.columns.str.strip().str.lower()

# Create date
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['day'])

# Clean numeric columns
df['temperature'] = df['temperature'].astype(str).str.replace('(', '').str.replace(')', '').str.strip().astype(float)
df['humidity'] = df['humidity'].astype(float)
df['atmospheric pressure'] = df['atmospheric pressure'].astype(float)

# -------------------------------
# 1. BASIC STATS
# -------------------------------
print("\n📊 BASIC STATS")
print(df[['temperature','humidity','atmospheric pressure']].describe())

# -------------------------------
# 2. CORRELATION ANALYSIS
# -------------------------------
print("\n📈 CORRELATION MATRIX")
print(df[['temperature','humidity','atmospheric pressure']].corr())

# -------------------------------
# 3. MOVING AVERAGE (TREND)
# -------------------------------
df['temp_ma7'] = df['temperature'].rolling(window=7).mean()

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'], label="Temperature", alpha=0.5)
plt.plot(df['date'], df['temp_ma7'], label="7-day Moving Avg", color='red')
plt.legend()
plt.title("Temperature Trend")
plt.show()

# -------------------------------
# 4. TEMPERATURE vs HUMIDITY
# -------------------------------
plt.figure(figsize=(6,5))
plt.scatter(df['temperature'], df['humidity'], alpha=0.5)
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.show()

# -------------------------------
# 5. PRESSURE vs TEMPERATURE
# -------------------------------
plt.figure(figsize=(6,5))
plt.scatter(df['temperature'], df['atmospheric pressure'], alpha=0.5, color='green')
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.title("Temperature vs Pressure")
plt.show()

# -------------------------------
# 6. HOTTEST & COLDEST DAYS
# -------------------------------
print("\n🔥 HOTTEST DAY")
print(df.loc[df['temperature'].idxmax()])

print("\n❄ COLDEST DAY")
print(df.loc[df['temperature'].idxmin()])

# -------------------------------
# 7. HUMIDITY EXTREMES
# -------------------------------
print("\n💧 MOST HUMID DAY")
print(df.loc[df['humidity'].idxmax()])

print("\n🏜 LEAST HUMID DAY")
print(df.loc[df['humidity'].idxmin()])

# -------------------------------
# 8. DAILY TEMP RANGE (BONUS)
# -------------------------------
df['temp_range'] = df['temperature'] - df['temperature'].min()

plt.figure(figsize=(10,4))
plt.plot(df['date'], df['temp_range'], color='purple')
plt.title("Daily Temperature Range")
plt.show()

# -------------------------------
# 9. MONTHLY ANALYSIS
# -------------------------------
df['month'] = df['date'].dt.month

monthly_avg = df.groupby('month')['temperature'].mean()

plt.figure(figsize=(8,4))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Monthly Avg Temperature")
plt.show()

# -------------------------------
# 10. SUMMARY REPORT
# -------------------------------
print("\n📌 SUMMARY")
print(f"Average Temperature: {df['temperature'].mean():.2f}")
print(f"Average Humidity: {df['humidity'].mean():.2f}")
print(f"Average Pressure: {df['atmospheric pressure'].mean():.2f}")


# -------------------------------
# Seasonal Average Temperature (LINE CHART)
# -------------------------------

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

# krijo season nga date
df['season'] = df['date'].dt.month.apply(get_season)

# group
seasonal_temperature = df.groupby('season')['temperature'].mean()

# renditja e saktë e sezonave
season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
seasonal_temperature = seasonal_temperature.reindex(season_order)

# -------------------------------
# LINE PLOT
# -------------------------------
plt.figure(figsize=(8,5))

plt.plot(
    seasonal_temperature.index,
    seasonal_temperature.values,
    marker='o',
    linestyle='--'
)

# shto vlerat mbi pika
for i, value in enumerate(seasonal_temperature.values):
    plt.text(i, value, f"{value:.2f}", ha='center', va='bottom')

plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)

plt.tight_layout()
plt.show()