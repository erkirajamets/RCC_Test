import requests
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

def get_response(params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def plot_data(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['Baltics imbalance'], label='Baltics imbalance', marker='.', color='red', linewidth = '1')
    plt.plot(df['Timestamp'], df['Baltics upwards'], label='Baltics | Upward', marker='.', color='blue', linewidth = '1')
    plt.plot(df['Timestamp'], df['Baltics downwards'], label='Baltics | Downward', marker='.', color='green', linestyle = '--', linewidth = '1')

    locator = mdates.AutoDateLocator(minticks=7, maxticks=10)
    formatter = mdates.AutoDateFormatter(locator)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.gca().xaxis.set_major_locator(locator)  
    plt.title('Imbalance volumes and Normal activations - Total')
    plt.legend()
    plt.grid(axis = 'y')
    plt.tight_layout()
    plt.show()

url = "https://api-baltic.transparency-dashboard.eu/api/v1/export"
imbalance_params = {
    "id" : "imbalance_volumes",
    "start_date": "2024-08-01T00:00",
    "end_date": "2024-09-01T00:00",
    "output_time_zone": "CET",
    "output_format": "json"
}
activations_params = {
    "id" : "normal_activations_total",
    "start_date": "2024-08-01T00:00",
    "end_date": "2024-09-01T00:00",
    "output_time_zone": "CET",
    "output_format": "json"
}
imbalance_data = get_response(params=imbalance_params)
activations_data = get_response(params=activations_params)
if imbalance_data and activations_data:
    #values for imbalance, activations and timestamps
    imbalance_timeseries = imbalance_data['data']['timeseries']    
    imbalance_baltics_values = [entry['values'][0] for entry in imbalance_timeseries]
    activations_timeseries = activations_data['data']['timeseries']
    activations_baltics_upward_values = [entry['values'][0] for entry in activations_timeseries]
    activations_baltics_downward_values = [entry['values'][1] for entry in activations_timeseries]
    timestamps = [entry['from'] for entry in imbalance_timeseries]
    
    df = pd.DataFrame({
        'Timestamp': pd.to_datetime(timestamps), 
        'Baltics upwards': activations_baltics_upward_values,
        'Baltics downwards': activations_baltics_downward_values, 
        'Baltics imbalance': imbalance_baltics_values})
    plot_data(df)
