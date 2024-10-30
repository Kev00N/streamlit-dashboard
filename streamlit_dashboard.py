import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data from CSV and cache it for performance
@st.cache_data
def load_data():
    return pd.read_csv('dataset.csv')

# Load the dataset
data = load_data()

# Set the title and description of the dashboard
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

# Create a line chart for population over time
fig = px.line(data, x="year", y="population", color="sex", title="Population Over Time")
st.plotly_chart(fig)

# CSS styling for the employment status section
st.markdown("""
    <style>
    .employment-status-container {
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Create a container for the employment status trends
with st.container():
    st.markdown("<div class='employment-status-container'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Employment Status Trends in Kenya</h2>", unsafe_allow_html=True)

    # Create a dropdown to filter data by sex
    sex_options = data['sex'].unique()
    selected_sex = st.selectbox("Filter by Sex", options=['All'] + list(sex_options))

    # Filter data based on selected sex
    if selected_sex != 'All':
        filtered_data = data[data['sex'] == selected_sex]
    else:
        filtered_data = data

    # Create three columns for the line charts
    col1, col2, col3 = st.columns(3)

    # Total Inactive Population chart
    with col1:
        fig_population = px.line(filtered_data, x="year", y="total_inactive_population", color="sex", title="Total Inactive Population by Year and Sex")
        st.plotly_chart(fig_population, use_container_width=True)

    # Total Unemployed Population chart
    with col2:
        fig_unemployed = px.line(filtered_data, x="year", y="total_unemployed_population", color="sex", title="Total Unemployed Population by Year and Sex")
        st.plotly_chart(fig_unemployed, use_container_width=True)

    # Total Employed Population chart
    with col3:
        fig_employed = px.line(filtered_data, x="year", y="total_employed_population", color="sex", title="Total Employed Population by Year and Sex")
        st.plotly_chart(fig_employed, use_container_width=True)

    # Create three columns for the pie charts
    col4, col5, col6 = st.columns(3)

    # Pie chart for Total Inactive Population by Sex
    with col4:
        fig_total_inactive_by_sex = px.pie(filtered_data.groupby("sex")["total_inactive_population"].sum().reset_index(), names="sex", values="total_inactive_population", title="Total Inactive Population by Sex")
        st.plotly_chart(fig_total_inactive_by_sex, use_container_width=True)

    # Pie chart for Total Unemployed Population by Sex
    with col5:
        fig_total_unemployed_by_sex = px.pie(filtered_data.groupby("sex")["total_unemployed_population"].sum().reset_index(), names="sex", values="total_unemployed_population", title="Total Unemployed Population by Sex", hole=0.4)
        st.plotly_chart(fig_total_unemployed_by_sex, use_container_width=True)

    # Pie chart for Total Employed Population by Sex
    with col6:
        fig_total_employed_by_sex = px.pie(filtered_data.groupby("sex")["total_employed_population"].sum().reset_index(), names="sex", values="total_employed_population", title="Total Employed Population by Sex")
        st.plotly_chart(fig_total_employed_by_sex, use_container_width=True)

    # Close the container for the employment status section
    st.markdown("</div>", unsafe_allow_html=True)
    
st.markdown("<h2 style='text-align: center; margin-top: 40px;'>Employment Status by Education Level in Kenya</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center; color: blue;'>Basic Education</h3>", unsafe_allow_html=True)
    fig_basic_inactive = px.pie(
        data.groupby("sex")["Basic_unemployment"].sum().reset_index(),
        names="sex",
        values="Basic_unemployment",
        title="Basic Education - Inactive Population by Sex",
        hole=0.4
    )
    st.plotly_chart(fig_basic_inactive, use_container_width=True)

    filtered_data_basic = data[data['age_group'].isin(["15-24", "25-35"])]
    fig_basic_unemployed_age_sex = px.bar(
        filtered_data_basic.groupby(["age_group", "sex"])["Basic_unemployment"].sum().reset_index(),
        x="age_group",
        y="Basic_unemployment",
        color="sex",
        title="Basic Ed - Unemployed by Age Group and Sex",
        barmode="stack",
        category_orders={"age_group": ["15-24", "25-35"]},
        labels={"age_group": "Age Group", "Basic_unemployment": "Unemployed Population"}
    )
    st.plotly_chart(fig_basic_unemployed_age_sex, use_container_width=True)

with col2:
    st.markdown("<h3 style='text-align: center; color: blue;'>Intermediate Education</h3>", unsafe_allow_html=True)
    fig_intermediate_inactive = px.pie(
        data.groupby("sex")["Intermediate_unemployment"].sum().reset_index(),
        names="sex",
        values="Intermediate_unemployment",
        title="Intermediate Ed - Inactive Population by Sex",
        hole=0.4
    )
    st.plotly_chart(fig_intermediate_inactive, use_container_width=True)

    filtered_data_intermediate = data[data['age_group'].isin(["15-24", "25-35"])]
    fig_intermediate_unemployed_age_sex = px.bar(
        filtered_data_intermediate.groupby(["age_group", "sex"])["Intermediate_unemployment"].sum().reset_index(),
        x="age_group",
        y="Intermediate_unemployment",
        color="sex",
        title="Intermediate Ed - Unemployed by Age Group and Sex",
        barmode="stack",
        category_orders={"age_group": ["15-24", "25-35"]},
        labels={"age_group": "Age Group", "Intermediate_unemployment": "Unemployed Population"}
    )
    st.plotly_chart(fig_intermediate_unemployed_age_sex, use_container_width=True)

with col3:
    st.markdown("<h3 style='text-align: center; color: blue;'>Advanced Education</h3>", unsafe_allow_html=True)
    fig_advanced_inactive = px.pie(
        data.groupby(["year", "sex"])["Advanced_unemployment"].sum().reset_index(),
        names="sex",
        values="Advanced_unemployment",
        title="Advanced Ed - Inactive Population by Year and Sex",
        hole=0.4
    )
    st.plotly_chart(fig_advanced_inactive, use_container_width=True)

    filtered_data_advanced = data[data['age_group'].isin(["15-24", "25-35"])]
    fig_advanced_unemployed_age_sex = px.bar(
        filtered_data_advanced.groupby(["age_group", "sex"])["Advanced_unemployment"].sum().reset_index(),
        x="age_group",
        y="Advanced_unemployment",
        color="sex",
        title="Advanced Ed - Unemployed by Age Group and Sex",
        barmode="stack",
        category_orders={"age_group": ["15-24", "25-35"]},
        labels={"age_group": "Age Group", "Advanced_unemployment": "Unemployed Population"}
    )
    st.plotly_chart(fig_advanced_unemployed_age_sex, use_container_width=True)


