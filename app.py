from flask import Flask, request, render_template, send_file
import numpy as np
import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import io

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Enable debug mode
app.config['DEBUG'] = True

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=request.form.get('reading_score'),
                writing_score=request.form.get('writing_score')
            )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")

            # Add the predicted score to the DataFrame
            pred_df['predicted_score'] = results[0]

            return render_template('home.html', results=results[0])
        except Exception as e:
            print(f"An error occurred: {e}")
            return render_template('home.html', results="An error occurred. Please try again.")

# Route for visualization
@app.route('/visualize', methods=['GET', 'POST'])
def visualize():
    if request.method == 'GET':
        return render_template('visualize.html')
    else:
        try:
            hue_option = request.form.get('hue_option')
            df = pd.read_csv('artifacts\\train.csv')  # Adjust the path as necessary

            # Fetch the latest prediction data
            gender = request.form.get('gender')
            race_ethnicity = request.form.get('race_ethnicity')
            parental_level_of_education = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_preparation_course = request.form.get('test_preparation_course')
            reading_score = float(request.form.get('reading_score'))
            writing_score = float(request.form.get('writing_score'))

            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )
            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            pred_df['predicted_score'] = results[0]

            plt.figure(figsize=(10, 6))
            scatter_plot = sns.scatterplot(data=df, x=hue_option, y='math score', hue=hue_option, alpha=0.5)
            scatter_plot = sns.scatterplot(data=pred_df, x=hue_option, y='predicted_score', color='red', s=100, label='Predicted Score')
            plt.title('Scatter plot of Predicted Math Score')
            plt.xlabel(hue_option.replace('_', ' ').title())
            plt.ylabel('Predicted Math Score')

            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)

            return send_file(img, mimetype='image/png')
        except Exception as e:
            print(f"An error occurred: {e}")
            return render_template('visualize.html', error="An error occurred. Please try again.")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
