# COVID-19 SIR Model Project

A Python implementation of the SIR (Susceptible-Infected-Removed) epidemiological model to analyze and predict COVID-19 spread in Japan using real-world data.

## 📊 Overview

This project implements a discrete SIR model to analyze the spread of COVID-19 in Japan from January 22, 2020. The model uses real COVID-19 data from Johns Hopkins University to fit parameters and make predictions about the pandemic's progression.

## 🔬 What is the SIR Model?

The SIR model is a compartmental model that divides the population into three groups:
- **S (Susceptible)**: Individuals who can be infected
- **I (Infected)**: Currently infected individuals
- **R (Removed)**: Individuals who have recovered or died

The model uses differential equations to simulate how individuals move between these compartments over time.

## 📁 Project Structure

```
Covid-19-SIR-Model-Project/
├── main.py                                    # Main implementation file
├── requirements.txt                           # Python dependencies
├── time_series_covid19_confirmed_global.csv   # Global confirmed cases data
├── time_series_covid19_deaths_global.csv      # Global deaths data
├── time_series_covid19_recovered_global.csv   # Global recovered cases data
└── README.md                                  # This file
```

## 🚀 Features

- **Data Processing**: Loads and processes real COVID-19 data from CSV files
- **SIR Model Implementation**: Discrete-time SIR model simulation
- **Parameter Optimization**: Uses least squares optimization to fit model parameters
- **Visualization**: Generates multiple plots comparing actual vs. predicted data
- **Analysis**: Calculates key epidemiological metrics like R₀ and average infection duration

## 📋 Requirements

- Python 3.x
- numpy
- matplotlib
- scipy
- pandas

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hieunguyen2711/Covid-19-SIR-Model-Project.git
   cd Covid-19-SIR-Model-Project
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

Run the main script:
```bash
python main.py
```

The script will:
1. Load COVID-19 data for Japan
2. Process and normalize the data
3. Fit the SIR model parameters using optimization
4. Generate visualizations comparing actual vs. predicted data
5. Display key metrics including R₀ and average infection duration

## 📈 Results

The model provides several key insights:

- **R₀ Value**: ~1.14 (basic reproduction number)
- **Average Infection Duration**: ~11.9 days
- **Prediction**: The model suggests that COVID-19 had limited spread in Japan during the initial period, with the susceptible population remaining around 99.8%

## 📊 Visualizations

The project generates four main plots:
1. **Actual Infected vs. Removed over time**
2. **Actual Susceptible population over time**
3. **Model comparison**: Actual vs. Predicted Infected and Removed
4. **Susceptible comparison**: Actual vs. Predicted Susceptible population

## 🧮 Model Parameters

- **Population (N)**: 126,300,000 (Japan's population)
- **β (Beta)**: Transmission rate (optimized)
- **γ (Gamma)**: Recovery rate (optimized)
- **Time Period**: 350 days from January 22, 2020

## 📚 Data Sources

The COVID-19 data used in this project comes from Johns Hopkins University's COVID-19 Data Repository, specifically:
- Global confirmed cases time series
- Global deaths time series  
- Global recovered cases time series

## 🔬 Mathematical Model

The discrete SIR model uses these equations:
- S(n+1) = S(n) - βS(n)I(n)
- I(n+1) = I(n) + βS(n)I(n) - γI(n)
- R(n+1) = R(n) + γI(n)

Where:
- β is the transmission rate
- γ is the recovery rate
- R₀ = β/γ (basic reproduction number)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Hieu Nguyen**
- GitHub: [@hieunguyen2711](https://github.com/hieunguyen2711)

## 🙏 Acknowledgments

- Johns Hopkins University for providing the COVID-19 dataset
- The SIR model methodology based on epidemiological modeling principles