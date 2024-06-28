import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_target_point(length, grade, stimp_speed):
    stimp_grade_product = stimp_speed * grade
    target_point = length / (1 + stimp_grade_product)
    return target_point

st.title("Putting Calculator")

# Input fields
length = st.number_input("Length of Putt (feet)", min_value=0.0, format="%.2f")
grade = st.number_input("Grade of Green (%)", min_value=0.0, format="%.2f")
stimp_speed = st.number_input("Stimp Speed (feet)", min_value=0.0, format="%.2f")

# Calculate target point
if st.button("Calculate"):
    target_point = calculate_target_point(length, grade, stimp_speed)
    st.write(f"Target Point: {target_point:.2f} feet")

    # Example Data for Plotting
    x_values = np.linspace(0, length, 100)
    y_values = target_point * (x_values / length)

    # Plotting the graph
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label='Putt Trajectory')
    ax.axhline(y=target_point, color='r', linestyle='--', label='Target Point')
    ax.set_xlabel('Distance (feet)')
    ax.set_ylabel('Putt Value')
    ax.set_title('Putting Trajectory and Target Point')
    ax.legend()
    st.pyplot(fig)

# Allow multiple graphs for comparison
if st.button("Plot Multiple Putts"):
    target_points = []
    lengths = []
    grades = []
    stimp_speeds = []

    with st.form(key='input_form'):
        lengths = st.text_input("Enter lengths of putts (comma-separated):")
        grades = st.text_input("Enter grades of green (comma-separated):")
        stimp_speeds = st.text_input("Enter stimp speeds (comma-separated):")
        submit_button = st.form_submit_button(label='Plot')

    if submit_button:
        lengths = list(map(float, lengths.split(',')))
        grades = list(map(float, grades.split(',')))
        stimp_speeds = list(map(float, stimp_speeds.split(',')))

        fig, ax = plt.subplots()

        for i in range(len(lengths)):
            target_point = calculate_target_point(lengths[i], grades[i], stimp_speeds[i])
            x_values = np.linspace(0, lengths[i], 100)
            y_values = target_point * (x_values / lengths[i])
            ax.plot(x_values, y_values, label=f'Putt {i+1}: Length={lengths[i]}, Grade={grades[i]}, Stimp={stimp_speeds[i]}')
            ax.axhline(y=target_point, linestyle='--')

        ax.set_xlabel('Distance (feet)')
        ax.set_ylabel('Putt Value')
        ax.set_title('Multiple Putting Trajectories')
        ax.legend()
        st.pyplot(fig)
