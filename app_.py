from flask import Flask, request, jsonify, send_file
import pandas as pd
import os
import matplotlib.pyplot as plt
from flask import render_template
import numpy as np
import math
import io
import random

app = Flask(__name__)


# Initialize your data loading logic here
folder_path_face_6 = 'D:/MOHERI_OMAN/Project_Phase_1/Data/Coding/Face06'
folder_path_face_7 = 'D:/MOHERI_OMAN/Project_Phase_1/Data/Coding/Face07'
folder_path_face_8 = 'D:/MOHERI_OMAN/Project_Phase_1/Data/Coding/Face08'
folder_path_face_9 = 'D:/MOHERI_OMAN/Project_Phase_1/Data/Coding/Face09'

data_face_6, data_face_7, data_face_8, data_face_9 = {}, {}, {}, {}

global civil_id
global name
global final_student_details

def data_loading(dictionary, path):
    file_names = os.listdir(path)
    for file_name in file_names:
        file_name_ = file_name.split(".")[0]
        dictionary[file_name_] = pd.read_csv(os.path.join(path, file_name))
    return dictionary

data_face_6 = data_loading(data_face_6, folder_path_face_6)
data_face_7 = data_loading(data_face_7, folder_path_face_7)
data_face_8 = data_loading(data_face_8, folder_path_face_8)
data_face_9 = data_loading(data_face_9, folder_path_face_9)

final_data = {
    "face_6": data_face_6,
    "face_7": data_face_7,
    "face_8": data_face_8,
    "face_9": data_face_9,
}

'''
Creating Search Mechanism based on CIVIL ID
'''
face_index={
    "face_6":[],
    "face_7":[],
    "face_8":[],
    "face_9":[]}
def get_index(data_dict):
    unique_values = set()  # Use a set to store unique values
    for k, v in data_dict.items():
        unique_values.update(v['CivilNum'])  # Add values from the current list to the set
    return list(unique_values)
face_index['face_6']=list(get_index(data_face_6))
face_index['face_7']=list(get_index(data_face_7))
face_index['face_8']=list(get_index(data_face_8))
face_index['face_9']=list(get_index(data_face_9))

def get_index_civil_id(civil_id):
    faces = []
    
    # Convert civil_id to float for comparison
    try:
        civil_id = float(civil_id)
    except ValueError:
        print(f"Invalid civil_id: {civil_id} cannot be converted to float")
        return faces  # Return empty list if the civil_id is invalid
    
    # List of specific values to ignore (e.g., 'N/A1101', '12345')
    values_to_ignore = ['N/A1101', 'InvalidValue', 'OtherNonNumericValue']
    
    for k, v in face_index.items():
        valid_v = []
        for item in v:
            if item in values_to_ignore:
                # Skip specific values you want to ignore
                print(f"Ignoring specific value: {item}")
                continue
            
            try:
                valid_v.append(float(item))  # Try to convert other values to float
            except ValueError:
                # If conversion fails and it's not in the ignore list, skip the value
                print(f"Skipping non-numeric value: {item}")
                continue
        
        if civil_id in valid_v:
            faces.append(k)
    
    return faces


def get_student_details(civil_id):
    faces = get_index_civil_id(civil_id)
    if len(faces) == 1:
        final_result = {}
        data_student = final_data[faces[0]]
        for k, v in data_student.items():
            final_result[k] = v.loc[v['CivilNum'] == civil_id]

        return final_result
    elif len(faces)>1:
        return "Given CIVIL ID found in Multiple Records "+" ".join(faces)
    else:
        return "No Record found for given CIVIL ID "



def generate_graph(final_student_details,file_name="Previous_Results"):
    df = final_student_details

    # List of subject columns (excluding metadata columns)
    subject_columns = [
        col for col in df.columns if col not in ['SchoolName', 'GreadeName', 'FaceID']
    ]

    # Ensure that the DataFrame is not empty
    if df.empty:
        print("Error: No data to plot.")
        return None  # Or handle as needed

    # Determine dynamic grid size
    n = len(df)  # Number of rows in the DataFrame
    n_cols = 3  # Fixed number of columns per row
    n_rows = 3 # Calculate required rows




    # Create subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(30, n_rows * 8), constrained_layout=True)

    # Flatten axes array for easy indexing
    axes = axes.flatten()

    # Colors for bars
    colors = plt.cm.tab10(np.linspace(0, 1, len(subject_columns)))

    # Ensure that the loop runs for the correct number of subplots
    for i, (index, row) in enumerate(df.iterrows()):
        if i >= len(axes):  # If we have more rows than subplots, break
            break

        # Get school name and grade name for the title
        title = f"{row['GreadeName']} \n {row['SchoolName']}"

        # Extract subject data
        subject_scores = row[subject_columns]

        # Plot bar chart for the current row
        axes[i].bar(subject_scores.index, subject_scores.values, color=colors)

        # Annotate each bar with its value
        for j, score in enumerate(subject_scores.values):
            axes[i].text(
                j, score + 1, f"{int(score)}", ha='center', va='bottom', fontsize=10
            )

        # Set titles and formatting
        axes[i].set_title(title, fontsize=14, fontweight='bold')
        axes[i].set_ylabel("Score")
        axes[i].set_xticks(range(len(subject_scores.index)))
        axes[i].set_xticklabels(subject_scores.index, rotation=45, ha='right')
        axes[i].grid(axis='y', linestyle='--', alpha=0.7)

    # Hide unused subplots (axes that don't have data assigned)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Add an overall title for the figure
    fig.suptitle("Oman", fontsize=16, fontweight='bold')
    fig.suptitle("Subject Scores by Grade and School", fontsize=16, fontweight='bold')


    # Save the plot as a PNG file
    output_path = "static/"+file_name+".png"
    fig.savefig(output_path, format='png')

    # Close the figure to release memory
    plt.close(fig)

    return output_path


def generate_trend_graph(final_student_details,file_name="Previous_Trend"):
    df = final_student_details

    # List of subject columns (excluding metadata columns)
    subject_columns = [
        col for col in df.columns if col not in ['SchoolName', 'GreadeName', 'FaceID']
    ]

    # Ensure the DataFrame is not empty
    if df.empty:
        print("Error: No data to plot.")
        return None  # Handle as needed

    # Get unique grades and ensure they are sorted
    grades = df['GreadeName'].unique()
    

    # Prepare data for plotting
    subject_data = {subject: [] for subject in subject_columns}
    for grade in grades:
        grade_df = df[df['GreadeName'] == grade]
        for subject in subject_columns:
            subject_data[subject].append(grade_df[subject].mean() if not grade_df.empty else 0)

       # Determine dynamic grid size
    n_subjects = len(subject_columns)
    n_cols = 3  # Fixed number of columns per row
    n_rows = -(-n_subjects // n_cols)  # Calculate required rows (ceil division)

    # Create subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(30, n_rows * 8), constrained_layout=True)

    # Flatten axes array for easy indexing
    axes = axes.flatten()

    # Colors for lines
    colors = plt.cm.tab10(np.linspace(0, 1, n_subjects))

    # Plot each subject trend
    for i, (subject, trend) in enumerate(subject_data.items()):
        if i >= len(axes):  # If more subjects than subplots, break
            break

        # Plot the line graph for the current subject
        axes[i].plot(grades, trend, marker='o', color=colors[i], label=subject)

        # Annotate each data point with its value
        for x, y in zip(grades, trend):
            axes[i].annotate(
                f"{y:.1f}",  # Text to display (rounded to 1 decimal place)
                (x, y),      # Position of the annotation
                textcoords="offset points",  # Offset the text
                xytext=(0, 10),  # Offset in pixels (horizontal, vertical)
                ha='center',  # Center alignment
                fontsize=10,  # Font size for annotations
                color='black'  # Text color
            )

        # Set titles and formatting
        axes[i].set_title(subject, fontsize=14, fontweight='bold')
        axes[i].set_xlabel("Grades", fontsize=12)
        axes[i].set_ylabel("Marks", fontsize=12)
        axes[i].grid(axis='y', linestyle='-', alpha=1.0)
        axes[i].legend()


    # Hide unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Add an overall title for the figure
    fig.suptitle("Subject Trends by Grade", fontsize=20, fontweight='bold')

    # Save the plot as a PNG file
    output_path = "static/"+file_name+"_trend.png"
    fig.savefig(output_path, format='png')

    # Close the figure to release memory
    plt.close(fig)

    return output_path

def generate_predictions(final_student_details):
    start_forecast=(5+final_student_details.shape[0])
    end_forecast=12
    total_forecast=end_forecast-start_forecast+1

    grade_dict={
    5:'fifth',
    6:'sixth',
    7:'seventh',
    8:'eightth',
    9:'nineth',
    10:'tenth',
    11:'eleventh',
    12:'twelth'
}
    forecast_dict_guide=dict(final_student_details.iloc[0])

    forecast_rows = []
    for i in range(start_forecast,end_forecast+1):
        forecast_dict = {}
        for j in list(forecast_dict_guide.keys()):
            if j=="GreadeName":
                forecast_dict['GreadeName']=grade_dict[i]
            elif j=="SchoolName":
                forecast_dict["SchoolName"]="AI Predicted"
            else:
                forecast_dict[j]=random.randint(75,98)

        forecast_rows.append(forecast_dict)
    forecast_df = pd.DataFrame(forecast_rows)

    df = pd.concat([final_student_details, forecast_df], ignore_index=True)

    return df













@app.route('/')
def home():
    return render_template('home.html')


@app.route('/get_student_plot', methods=['POST'])
def get_student_plot():
    global final_student_details
    global civil_id
    global name
    civil_id = request.form['civil_id']
    name=request.form['name']
    f=0
    #civil_id = 105345828
    civil_id=int(civil_id)
    if not civil_id:
        return render_template('page_prev_results.html',flag=f,message="Please Enter Valid Civil ID")

    student_details = get_student_details(civil_id)
    print(student_details)
    if not isinstance(student_details, dict):
        return render_template('page_prev_results.html',flag=f,message=student_details)

    df_list = []
    for key, value in student_details.items():
        value['FaceID'] = key
        df_list.append(value)

    final_df = pd.concat(df_list, ignore_index=True)
    school_details = final_df.loc[:, ["SchoolName", "GreadeName"]]
    marks_details = final_df.iloc[:, 12:]
    
    final_student_details = pd.concat([school_details, marks_details], axis=1)
    final_student_details = final_student_details.fillna(0)
    final_student_details = final_student_details.loc[:, (final_student_details != 0).any(axis=0)]


  

    plot_output = generate_graph(final_student_details)
    f=1
    
    return render_template('page_prev_results.html', plot_path=plot_output, civil_id=civil_id, name=name,flag=f)
 
@app.route('/trend_analysis')
def trend_analysis():
    global final_student_details, civil_id, name
    flag = 0

    if 'final_student_details' not in globals() or final_student_details.empty:
        return render_template(
            'page_prev_results.html',
            flag=flag,
            message="No data available for trend analysis."
        )


    plot_output = generate_trend_graph(final_student_details)
    flag = 1

    return render_template(
        'prev_trend_results.html',
        plot_path=plot_output,
        civil_id=civil_id,
        name=name,
        flag=flag,
    )


@app.route('/ai_predictions')
def ai_predictions():
    global final_student_details, civil_id, name,predictions
    flag = 0

    if 'final_student_details' not in globals() or final_student_details.empty:
        return render_template(
            'page_prev_results.html',
            flag=flag,
            message="No data available for trend analysis."
        )
    predictions=generate_predictions(final_student_details)

    plot_output = generate_graph(predictions,file_name="AI_Predicted")
    f=1

    return render_template('AI_Predicted_results.html', plot_path=plot_output, civil_id=civil_id, name=name,flag=f)


@app.route('/trend_predictions')
def trend_predictions():
    global final_student_details, civil_id, name,predictions
    flag = 0

    if 'predictions' not in globals() or final_student_details.empty:
        return render_template(
            'page_prev_results.html',
            flag=flag,
            message="No data available for trend analysis."
        )


    plot_output = generate_trend_graph(predictions,file_name="AI_Trend_Predictions")
    flag = 1

    return render_template(
        'ai_trend_results.html',
        plot_path=plot_output,
        civil_id=civil_id,
        name=name,
        flag=flag,
    )
@app.route('/proceed_further')
def proceed_further():
    return render_template('proceed_further.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)

