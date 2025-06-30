# Betting Arbitrage Detector

This project allows you to detect **arbitrage** opportunities in prediction markets like Polymarket, calculate the optimal combination of bets to maximize profit, and test the algorithm using both real Polymarket data and local example datasets.

---

## 🚀 Installation and Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MauroPerna/betting-arbitrage.git
   cd betting-arbitrage
   ```

2. **Create a virtual environment with conda:**

   ```bash
   conda create -n betting-prediction-venv python=3.10
   conda activate betting-prediction-venv
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃‍♂️ How to Run the Project

### 1. **Test with local example data**

By default, the main script (`main.py`) can be run in test mode using the data from the file `data/data.json`.

```python
if __name__ == '__main__':
    main(test=True)    # Test mode, uses local JSON
```

```bash
python main.py
```

### 2. **Test with real Polymarket data**

To use the Polymarket API and search for real-time arbitrage:

```python
if __name__ == '__main__':
    main(test=False)   # Polymarket mode, uses the real API
```

```bash
python main.py
```

---

## 📚 Arbitrage Principle (Theoretical Explanation)

**Arbitrage** consists of taking advantage of price/probability differences in a market to secure a risk-free profit by betting on all possible outcomes of an event.

### **How does arbitrage work in Polymarket?**

In Polymarket, the "price" for each outcome represents its **implied probability** (e.g., 0.18 means 18%).
If the sum of the probabilities of all outcomes in a market is **less than 1**, there is a theoretical opportunity for arbitrage.

#### **Why?**

Because you can allocate your funds across all outcomes so that, regardless of the result, your profit is equal and positive.

---

## 🧮 **Formula for the Optimal Bet Distribution**

Let an event have `n` possible outcomes with prices (probabilities) \$p\_1, p\_2, ..., p\_n\$, and a total amount to bet \$T\$ (e.g., \$100):

### **How to calculate how much to bet on each outcome:**

For each outcome \$i\$:

$$
\text{stake}_i = \frac{T \cdot (1 - p_i)}{\sum_{j=1}^n (1 - p_j)}
$$


Where:

$$
p_i \text{ is the price (implied probability) of outcome } i
$$

$$
T \text{ is the total amount to bet (e.g., 100)}
$$

$$
\sum_{j=1}^n (1 - p_j) \text{ is the sum of all the relative advantages}
$$

---

### **How much do I profit? (Guaranteed Profit)**

The net profit if outcome \$i\$ wins is:

$$
\text{profit}_i = \frac{\text{stake}_i}{p_i} - T
$$

The **guaranteed net profit** will be the **minimum** of all `profit_i` (it must be greater than zero for there to be real arbitrage).

---

## ⚠️ Notes

* For real arbitrage, the sum of probabilities must be **strictly less than 1** and the minimum profit must be positive.
* The script prints the best combination of bets and the guaranteed profit (if it exists).

---

## 📦 Project Structure

```
betting-arbitrage/
├── main.py
├── utils.py
├── requirements.txt
└── data/
    └── data.json
```

---
