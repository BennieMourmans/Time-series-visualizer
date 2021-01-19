import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & 
(df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    plt.plot(df, color='red', linewidth=.5)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.figure(figsize=(10,5))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month

    # Draw bar plot
    g = sns.catplot(data=df_bar, x='year', y='value', kind='bar', hue='month', palette='bright', ci=None, legend=False)
    plt.legend(title='Months', loc='upper left', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    g.set_ylabels('Average Page Views')
    g.set_xlabels('Years')
    fig = g.fig

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(14,7))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(title='Year-wise Box Plot (Trend)', ylabel='Page Views', xlabel='Year')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).set(title='Month-wise Box Plot (Seasonality)', ylabel='Page Views', xlabel='Month')

    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
