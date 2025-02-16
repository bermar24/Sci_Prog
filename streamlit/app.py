# pip install streamlit
# streamlit run app.py
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

# Streamlit UI
st.title('Energy_Consumption_Forecasting App')
st.text('This is a web app to explore earthquake data. ')
st.markdown('## This is **markdowns**')

uploaded_file = st.file_uploader('Upload your file here')

if uploaded_file:
    st.header('Data Statistics')
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())

    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xLabeU('Depth}')

    ax.set_ylabel("Magnitude")

    st.pyplot(fig)



# import pandas as pd
# from data_loader import DataLoader
# from model import RandomForestModel
# import matplotlib.pyplot as plt

# # Load data
# data_loader = DataLoader(emd_path='data/electricity_market_dataset.csv', om_path='data/open-meteo-50.09N8.65E117m.csv')
# df = data_loader.load_data()
#
# # Prepare features and target
# X = df.drop(columns=['GDP_Growth_Rate', 'Timestamp'])
# y = df['GDP_Growth_Rate']
#
# # Train model
# rf_model = RandomForestModel()
# rf_model.train(X, y)

# Streamlit UI
# st.title('Random Forest Prediction App')

# Checkbox to show data
# if st.checkbox('Show raw data'):
#     st.write(df)
#
# # Sample prediction
# single_data = X.iloc[0:1]
# predicted_value = rf_model.predict(single_data)
# st.write(f"Predicted Value: {predicted_value[0]:.2f}")
# st.write(f"Actual Value: {y.iloc[0]:.2f}")
#
# # Evaluate model
# mae, mse, r2 = rf_model.evaluate()
# st.write(f'Random Forest MAE: {mae}')
# st.write(f'Random Forest MSE: {mse}')
# st.write(f'Random Forest R2: {r2}')
#
# # Visualization
# st.subheader('Random Forest: Actual vs Predicted')
# y_pred_rf = rf_model.predict(X)
# plt.figure(figsize=(8, 6))
# plt.scatter(y, y_pred_rf)
# plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', lw=2)
# plt.xlabel('Actual GDP Growth Rate')
# plt.ylabel('Predicted GDP Growth Rate')
# st.pyplot(plt)


# streamlit run app.py