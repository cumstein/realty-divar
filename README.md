# Divar Real Estate API Scraper

This Python script demonstrates how to fetch real estate listing data from Divar.ir using their official Open API. It allows you to query listings based on various parameters like category, city, size, and price range.

## Features

*   Fetches real estate data from Divar.ir.
*   Customizable search parameters (category, city, size, rooms, price).
*   Outputs data in JSON format.

## Setup

1.  **Obtain an API Key:** (already done, continue on 2.)
    *   Go to [Divar Kenar](https://divar.ir/kenar/management/apps/create). 
    *   Log in to your Divar account.
    *   Register a new application to obtain your unique API key.

2.  **Install Dependencies:**
    *   Ensure you have Python installed (Python 3.6+ is recommended).
    *   Install the `requests` library:
        ```bash
        pip install requests
        ```

## Usage

1.  **Save the Code:**
    *   Save or donwload the provided Python code into a file named `divar_api_scraper.py`.

2.  **Insert Your API Key:** (already done, continue on 3.)
    *   Open `divar_api_scraper.py` in a text editor.
    *   Locate the line `API_KEY = "YOUR_API_KEY_HERE"`.
    *   Replace `"YOUR_API_KEY_HERE"` with the actual API key you obtained from Divar Kenar.

3.  **Customize Search Parameters (Optional):**
    *   Modify the `data` dictionary in the script to adjust your search criteria (e.g., change `category`, `city`, `min`/`max` `size`, `rooms`, `min`/`max` `credit`).

4.  **Run the Script:**
    *   Open your terminal or command prompt.
    *   Navigate to the directory where you saved `divar_api_scraper.py`.
    *   Run the script using:
        ```bash
        python divar_api_scraper.py
        ```

## Output

The script will print the fetched real estate data in JSON format directly to your console. You can redirect this output to a file for further processing or analysis:

```bash
python divar_api_scraper.py > real_estate_data.json
```

## Further Steps

*   **Data Analysis:** Use the collected JSON data for market trend analysis.
*   **Price Estimation:** Train machine learning models (Linear Regression, etc.) using this data to predict real estate prices.
*   **Data Visualization:** Create charts and graphs to visualize the data insights.
