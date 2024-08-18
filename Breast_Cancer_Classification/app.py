import app as st
import pickle

models = {}
for name in ["XGBoost", "Decision Tree", "Random Forest", "MLP", "SVM", "Logistic Regression"]:
    with open(f'models/{name}_model.pkl', 'rb') as f:
        models[name] = pickle.load(f)

st.title("Breat Cancer Classification")

tabs = ['Data Insights', 'Data Visualization', 'Test the Model']
current_tab = st.sidebar.radio('Navigation', tabs)

if current_tab == 'Data Insights':
    st.write('Data Insights tab content goes here')

elif current_tab == 'Data Visualization':
    st.write('Data Visualization tab content goes here')

elif current_tab == 'Test the Model':
    st.write('Test the Model tab content goes here')

    feature1 = st.text_input('Feature 1')

    if st.button('Predict'):
        pass
        #prediction = your_model.predict([[feature1, ...]])

        #st.write(f'Prediction: {prediction}')
        
if __name__ == '__main__':
    st.run()
