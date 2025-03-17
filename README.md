# 📈 **HMMs_StockMarket: Hidden Markov Model for Market Regime Detection**

## 🔍 **Project Overview**
This project applies a **Hidden Markov Model (HMM)** to analyze stock market regimes and forecast future trends. By leveraging historical **log returns**, we identify three market states:

- 🟢 **Bull Market** 🚀 (Strong uptrend)
- 🟠 **Neutral Market** ⚖️ (Sideways movement)
- 🔴 **Bear Market** 🐻 (Downtrend or crisis period)

The model is trained on historical **S&P 500** data from **2005–2011**, capturing the 2008 financial crisis. The results include **state transitions**, **stationary distributions**, and **market forecasts** using probability matrices.

---
## 📊 **1️⃣ Mean Log Returns & Covariances per State**

After training our **HMM**, we extract the mean log returns and covariances for each market regime:

| Market Regime | Mean Log Return | Variance |
|--------------|----------------|----------|
| 🟢 **Bull Market** | **0.0646** | **0.1892** |
| 🟠 **Neutral Market** | **-0.0366** | **0.9588** |
| 🔴 **Bear Market** | **-0.2322** | **6.5811** |

🔹 **Inference:** The **Bull Market** has the highest returns and lowest volatility, while the **Bear Market** has negative returns with the highest volatility.

---
## 🔄 **2️⃣ Transition Probability Matrix**
The **HMM transition matrix** captures the probability of switching between different market states:

\[
P = \begin{bmatrix}
0.9703 & 0.0297 & 0.0000 \\
0.0362 & 0.9574 & 0.0063 \\
0.0000 & 0.0348 & 0.9652
\end{bmatrix}
\]

🔹 **Interpretation:**
- The market tends to remain in the same state for long periods (high diagonal values).
- A **Bull Market** has only a **2.97% probability** of transitioning to a **Neutral Market**.
- A **Bear Market** has a **3.48% probability** of recovering to a **Neutral Market**.

Using this transition matrix, we can forecast future probabilities by multiplying it with the current state vector:

\[ N_{t+1} = N_t \cdot Q \]

---
## 📅 **3️⃣ Market Regimes with Moving Averages**

We compare the **HMM-inferred market states** with moving averages to validate our model.

### **Moving Averages Used:**
- **50-day SMA (Short-Term Trend) ➝ Blue Line**
- **200-day SMA (Long-Term Trend) ➝ Red Line**
- **Stock Price ➝ Black Line**
- **HMM-Inferred States ➝ Color-Coded Dots**

### **Trading Insights:**
✅ **Golden Cross (Bullish Signal):** If **SMA_50** crosses above **SMA_200**, a bull market is likely.  
✅ **Death Cross (Bearish Signal):** If **SMA_50** crosses below **SMA_200**, a bear market might follow.  

If the **HMM state transitions** align with these crossovers, our model successfully captures market trends.

---
## 📌 **4️⃣ Stationary Distribution Analysis**
The stationary distribution reveals **long-term probabilities** of each market regime:

| Market Regime | Probability |
|--------------|-------------|
| 🟢 **Bull Market** | **50.83%** |
| 🟠 **Neutral Market** | **41.60%** |
| 🔴 **Bear Market** | **7.56%** |

### **Key Takeaways:**
- **Bull Market is dominant (~50%)**, aligning with historical data that markets rise over time.
- **Neutral Market occurs ~41.6% of the time**, indicating frequent sideways movement.
- **Bear Markets are rare (~7.56%)**, reinforcing the idea that crashes are temporary.

---
## 🔮 **5️⃣ Market Forecasting Using HMM Probabilities**
Using **predictive probabilities**, we estimate the **next day's market state**:

\[
N_{t+1} = N_t \cdot P
\]

This allows us to forecast **multi-day transitions** using the n-step Markov property:

\[
N_{t+n} = N_t \cdot P^n
\]

🔹 **Current Prediction:** Based on today’s data, the market is most likely in a **Neutral State**.

---
## 🛠️ **Future Improvements: Adding MCMC for Bayesian Inference**
Next, we will integrate **Markov Chain Monte Carlo (MCMC)** methods to:
- Estimate **state transition uncertainties**.
- Compare HMM with **Bayesian Hidden Markov Models**.
- Improve market forecasting using **Monte Carlo simulations**.

🚀 **Stay tuned for further model enhancements!**

---
## 📜 **How to Run the Project**
### **1️⃣ Clone Repository:**
```bash
 git clone https://github.com/yourusername/HMMs_StockMarket.git
 cd HMMs_StockMarket
```
### **2️⃣ Set Up Virtual Environment:**
```bash
 python -m venv .venv
 source .venv/bin/activate  # (Mac/Linux)
 .venv\Scripts\activate    # (Windows)
```
### **3️⃣ Install Dependencies:**
```bash
 pip install -r requirements.txt
```
### **4️⃣ Run the Jupyter Notebook:**
```bash
 jupyter notebook
```
### **5️⃣ Train the HMM Model:**
Run the notebook in `notebooks/` to train the model and visualize market states.

---
## 🎯 **Final Thoughts**
This project demonstrates the power of **Hidden Markov Models** for financial analysis. With additional **MCMC sampling**, we aim to further refine predictions and risk assessments.

📌 **Contributions & Feedback Welcome!** If you have any suggestions or improvements, feel free to **open a pull request**. 🚀

