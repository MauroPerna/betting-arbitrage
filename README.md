# Betting Arbitrage Detector

Este proyecto permite detectar oportunidades de **arbitraje** en mercados de predicción tipo Polymarket, calcular la combinación óptima de apuestas para maximizar la ganancia y probar el algoritmo tanto con datos reales de Polymarket como con datasets locales de ejemplo.

---

## 🚀 Instalación y Primeros Pasos

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/MauroPerna/betting-arbitrage.git
   cd betting-arbitrage
   ```

2. **Crea un entorno virtual con conda:**

   ```bash
   conda create -n betting-prediction-venv python=3.10
   conda activate betting-prediction-venv
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃‍♂️ Cómo correr el proyecto

### 1. **Probar con datos de ejemplo locales**

Por defecto, el script principal (`main.py`) se puede ejecutar en modo test usando los datos del archivo `data/data.json`.

```python
if __name__ == '__main__':
    main(test=True)    # Modo test, usa el JSON local
```

```bash
python main.py
```

### 2. **Probar con datos reales de Polymarket**

Para usar la API de Polymarket y buscar arbitraje en tiempo real:

```python
if __name__ == '__main__':
    main(test=False)   # Modo Polymarket, usa la API real
```

```bash
python main.py
```

---

## 📚 Principio de Arbitraje (Explicación Teórica)

El **arbitraje** consiste en aprovechar diferencias de precios/probabilidades en un mercado para asegurar una ganancia sin riesgo, apostando en todos los posibles resultados de un evento.

### **¿Cómo funciona el arbitraje en Polymarket?**

En Polymarket, el "price" de cada outcome representa la **probabilidad implícita** (ejemplo: 0.18 equivale al 18%).
Si la suma de las probabilidades de todos los outcomes de un mercado es **menor a 1**, existe una oportunidad teórica de arbitraje.

#### **¿Por qué?**

Porque podés distribuir tu dinero entre todos los outcomes de manera que, sin importar el resultado, tu ganancia sea igual y positiva.

---

## 🧮 **Fórmula para el reparto óptimo de apuestas**

Sea un evento con `n` posibles resultados y precios (probabilidades) $p_1, p_2, ..., p_n$, y un monto total a apostar $T$ (por ejemplo, \$100):

### **Cómo calcular cuánto apostar a cada outcome:**

Para cada outcome $i$:

$$
\text{stake}_i = \frac{T \cdot (1 - p_i)}{\sum_{j=1}^n (1 - p_j)}
$$

Donde:

* $p_i$ es el "price" (probabilidad implícita) del outcome $i$
* $T$ es el total a apostar (ejemplo, \$100)
* $\sum_{j=1}^n (1 - p_j)$ es la suma de todas las "ventajas relativas"

---

### **¿Cuánto gano? (Profit garantizado)**

La ganancia neta en caso de que gane el outcome $i$ es:

$$
\text{profit}_i = \frac{\text{stake}_i}{p_i} - T
$$

El **profit neto garantizado** será el **mínimo** de todos los $\text{profit}_i$ (debe ser mayor que cero para que haya arbitraje real).

---

## ⚠️ Notas

* Para arbitraje real, la suma de probabilidades debe ser **estrictamente menor que 1** y el profit mínimo positivo.
* El script imprime la mejor combinación de apuestas y la ganancia asegurada (si existe).

---

## 📦 Estructura del proyecto

```
betting-arbitrage/
├── main.py
├── utils.py
├── requirements.txt
└── data/
    └── data.json
```


