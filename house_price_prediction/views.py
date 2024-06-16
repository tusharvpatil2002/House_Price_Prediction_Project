# house_price_prediction/views.py
from django.shortcuts import render
import pickle
import pandas as pd
import joblib

# Load the pickled model
#with open('house_price_prediction.pkl', 'rb') as model_file:
#    loaded_model = pickle.load(model_file)

loaded_model = joblib.load('house_price_prediction.pkl')


def predict_house_price(request):
    if request.method == 'POST':
        # Get user input data from the form
        city = request.POST.get('city')
        area = float(request.POST.get('area'))
        location = request.POST.get('location')
        num_bedrooms = int(request.POST.get('num_bedrooms'))

        # Convert user input into DataFrame
        user_data = {
            'City': city,
            'Area': area,
            'Location': location,
            'No. of Bedrooms': num_bedrooms
        }
        user_df = pd.DataFrame([user_data])

        # Predict using the loaded model
        predicted_price = loaded_model.predict(user_df)[0]

        # Render the result template with predicted price
        return render(request, 'result.html', {'predicted_price': predicted_price})

    # Render the form template for GET requests
    return render(request, 'index.html')
