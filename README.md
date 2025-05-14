# Damage Factor vs Intensity Dashboard

This project is an interactive dashboard built with Streamlit and Plotly for visualizing the relationship between Intensity and DamageFactor from an Excel file. Users can filter the data using sidebar filters and reset all filters with a single click.

## Features
- Interactive line chart: Intensity (x-axis) vs. DamageFactor (y-axis)
- Sidebar filters for: Infrastructure, Infra_details, Measure, Units, Model
- Reset Filters button to clear all selections
- Reads data from the `raw` sheet of `damagefactor.xlsx`

## Setup

1. **Clone the repository or download the files.**
2. **Install dependencies:**
   ```bash
   pip install streamlit pandas plotly openpyxl
   ```
3. **Place your Excel file** named `damagefactor.xlsx` in the project directory. Make sure it has a sheet named `raw` with columns:
   - Intensity
   - DamageFactor
   - Infrastructure
   - Infra_details
   - Measure
   - Units
   - Model

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
5. **Open your browser** to [http://localhost:8501](http://localhost:8501) to use the dashboard.

## Usage
- Use the sidebar to select filter values. The chart updates automatically.
- Click **Reset Filters** to clear all selections and start over.

## Customization
- To change filter order or add/remove filters, edit the `filter_columns` list in `app.py`.
- To use a different Excel file or sheet, update the `EXCEL_FILE` and `SHEET_NAME` variables in `app.py`.

---

**Enjoy exploring your data!** 