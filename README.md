# Food Delivery Analytics & AI Insights

An interactive, production-ready Streamlit dashboard built to analyze food delivery performance metrics, traffic impacts, courier ratings, and geographic delivery speeds.

* **Live Streamlit App**: https://d2qowjxphch7fxhcnzfos6.streamlit.app/
---

## Key Business Questions Addressed
1. **Traffic & Weather Impact**: How do high traffic densities (Jam, High) and adverse weather conditions (Stormy, Sandstorms) extend delivery completion times?
2. **Vehicle Efficiency**: Which vehicle types (motorcycles, scooters, electric scooters) maintain the highest courier ratings and fastest average delivery times?
3. **City Performance Bottlenecks**: Which metropolitan and semi-urban cities experience the longest delays, and what drives the variance in delivery speeds?
4. **Courier Demographics**: What is the relationship between courier age, experience, ratings, and overall operational efficiency?
5. **Order Type Optimization**: How do different types of orders (Buffet, Drinks, Meals, Snacks) affect preparation and transit times?

---

## What We Built & Accomplished
* **Data Pipeline & Cleaning**: Processed nearly 39,000 delivery records (`food_delivery_dataset.csv`), handling missing values in ratings, ages, and order times, and mapping distance groups and delivery speeds.
* **Interactive Dashboard (`app.py`)**: Built a fully responsive web application using Streamlit featuring real-time multi-select filtering for cities, vehicles, weather, traffic, and order types.
* **Advanced Visualizations**: Integrated Plotly charts including histograms, box plots, traffic-weather heatmaps, violin plots for courier ratings, and breakdown comparisons.
* **AI-Powered Insights**: Integrated Groq API functionality (`llama3-8b-8192`) to generate automated executive business recommendations directly from filtered dataset metrics.
* **Reporting & Export**: Added functionality to dynamically compute high-level business metrics and export custom professional PDF executive reports using `fpdf2`.
* **Cloud Deployment**: Successfully deployed and hosted the live application via Streamlit Cloud linked directly to this GitHub repository.
