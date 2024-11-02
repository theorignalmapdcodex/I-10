
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Sourcing the cleaned version of 'Social Media Analyse Dataset' for dashboard visualizations purposes
digtech_socmeduse_data = pd.read_csv('C:/Users/micha/Desktop/DTK530 Assign 10/I-10/I-7_Datasets/digtech_socmeduse_data.csv')


st.header('Analysis of Digital Technology Use and Youth Mental Health (Health Technology)')


st.image('/content/drive/MyDrive/MEngDTI@Duke/DTK530/I-7 (mini-project)/Images/research.jpeg')

st.title('Introduction')

st.write("Welcome to the Digital Youth Wellness Dashboard!")
st.write("I've created this interactive dashboard to unpack a simple but crucial question: How is digital technology affecting young people's mental health worldwide? This dashboard brings together data on youth digital habits – from screen time to social media use – and connects these patterns to mental health indicators like addiction tendencies and self-control. Whether you're a parent, educator, counselor, or policymaker, you'll find insights here that matter for your work with young people.")
st.write("What makes this research different? We're not just looking at how much time kids spend online – we're examining what that time means for their wellbeing, and how we might better support healthy digital habits across different global contexts.")
st.write("The insights here aim to inform smarter interventions, better support systems, and more effective policies for youth mental health in our digital age.")



# A---- Interactive Box Selector for Graph Display ---- #
st.sidebar.title("Select the Graph to View")
selected_spearman_graph = st.sidebar.selectbox(
    "Spearman Correlation Graphs:",
    ["Correlation Matrix", "Perceived Addiction vs. Productivity"]
)

selected_mann_whitney_graph = st.sidebar.selectbox(
    "Mann-Whitney Test Graphs & Interpretations:",
    ["Total Time Spent on the Platform by Country", "Time Spent on Social Media by Economic Group (Stacked)"]
)

# ---- Display content based on selections ---- #
# B---- SPEARMAN RANK CORRELATION ---- #
# Viz5
if selected_spearman_graph == "Correlation Matrix":
    st.header('Objective #1 - Exploring the Link Between Social Media Addiction and User Productivity')
    st.header("i - Correlation Matrix of Key Variables")
    correlation_matrix = digtech_socmeduse_data[[
        'Total Time Spent on the Platform (mins)',
        'Perceived Addiction Level',
        'Perceived Self Control Level',
        'Impact on Productivity',
        "User's Satisfaction with Platform"
    ]].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Correlation Matrix of Key Variables')

    st.pyplot(fig)

    st.write("This visualization reveals the correlation matrix reveals strong relationships between perceived addiction level, self-control, productivity, and user satisfaction (eg. higher perceived addiction levels are associated with higher user satisfaction but lower self-control and productivity, with total time spent showing minimal correlation to these factors, suggesting that the quality and nature of platform engagement may be more crucial than quantity in determining mental health outcomes among youth using digital devices and social media.")


# Viz5_Refined
elif selected_spearman_graph == "Perceived Addiction vs. Productivity":
    st.header('Objective #1 - Exploring the Link Between Social Media Addiction and User Productivity')
    st.header("ii. Visualization 5: Perceived Addiction vs. Productivity")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(x='Perceived Addiction Level', y='Impact on Productivity', data=digtech_socmeduse_data, ax=ax)
    ax.set_title("Spearman's Rank Correlation: Addiction vs. Productivity")
    ax.set_xlabel("Perceived Addiction Level")
    ax.set_ylabel("Impact on Productivity")

    st.pyplot(fig)

    st.write("The graph shows a strong negative correlation between perceived social media addiction and productivity, where higher addiction levels are associated with lower productivity.")



# C---- MANN WHITNEY TEST ---- #
# Viz3
if selected_mann_whitney_graph == "Total Time Spent on the Platform by Country":
    st.header('Objective #2 - Comparing Social Media Usage Patterns: Developed vs. Developing Nations')
    st.header("iii - Total Time Spent on the Platform by Country")
    grouped_data = digtech_socmeduse_data.groupby(['Country', 'Social Media Platform Used'])['Total Time Spent on the Platform (mins)'].sum().reset_index()
    fig = px.bar(grouped_data, x='Country', y='Total Time Spent on the Platform (mins)', color='Social Media Platform Used',
                barmode='group', title='Total Time Spent (mins) on Platform by Location')
    fig.update_layout(xaxis_title='Location', yaxis_title='Total Time Spent (mins)')
    st.plotly_chart(fig)

    st.write("This visualization demonstrates significant variations in platform usage across different countries, with India showing the highest overall usage across all platforms, highlighting the importance of considering cultural and regional factors when studying the impact of digital technology on youth mental health.")


# Viz3_refined
elif selected_mann_whitney_graph == "Time Spent on Social Media by Economic Group (Stacked)":
    st.header('Objective #2 - Comparing Social Media Usage Patterns: Developed vs. Developing Nations')
    st.header("iii. Visualization 3: Time Spent on Social Media by Economic Group (Stacked)")
    developed_countries_data = digtech_socmeduse_data[digtech_socmeduse_data['Economic Group'] == 'Developed']['Total Time Spent on the Platform (mins)']
    developing_countries_data = digtech_socmeduse_data[digtech_socmeduse_data['Economic Group'] == 'Developing']['Total Time Spent on the Platform (mins)']

    # Combine data for stacked histogram
    combined_data = pd.DataFrame({
        'Time Spent': developed_countries_data.tolist() + developing_countries_data.tolist(),
        'Group': ['Developed'] * len(developed_countries_data) + ['Developing'] * len(developing_countries_data)
    })
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=combined_data, x='Time Spent', hue='Group', multiple='stack', kde=True, ax=ax)
    ax.set_title("Stacked Distribution of Time Spent on Social Media by Economic Group")
    ax.set_xlabel("Total Time Spent (minutes)")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    st.write("The graph compares time spent on social media between developed and developing nations, showing a broader distribution of higher usage in developed nations.")


##--------------------------------------------------------------------------------------------------------------------##

st.title('Conclusion')
st.header('Insights For Youth Support Professionals and Digital Wellness Activists Around Every Part of the World:')
st.write("This in-depth study (examining the patterns among 1000 participants) looked at how social media affects young people's ability to stay productive, and the results are eye-opening. What I discovered was a remarkably strong pattern: as young people's sense of being addicted to social media increases, their productivity takes a dramatic hit. This isn't just a minor effect - we're seeing that increased social media addiction and decreased productivity go hand in hand almost perfectly. Think of it like a seesaw - as one side (addiction) goes up, the other side (productivity) consistently goes down. This finding gives us solid proof of something many parents, teachers, and counselors have suspected, and it highlights the urgent need for better support systems and tools to help young people maintain a healthy relationship with social media while staying productive in their daily lives.")
st.write("Additionally, I made a fascinating discovery that challenges what many of us might assume. Despite the economic and technological differences between developed countries (like the US, Japan, and Germany) and developing nations (such as India, Brazil, and Vietnam), young people are spending remarkably similar amounts of time on social media platforms. This isn't just a rough observation - I used robust statistical methods that could detect even small differences, yet found none. This finding is particularly important for two key reasons. One, it suggests that digital behavior patterns and potential addiction risks among youth are truly global phenomena, not limited by economic boundaries or access to technology. And two, the challenges of excessive social media use that we may see in Tokyo or New York are likely very similar to those in Mumbai or São Paulo. A recommendation for those working on solutions - whether you're developing mental health apps, planning intervention programs, or crafting digital wellness policies - this means you might not need to completely reinvent the wheel for different markets. The core issues and behaviors you're trying to address are surprisingly consistent across the globe.")
st.write("\n")
st.write("PS:In the quest to interpret the graphs, especially the Correlation Matrix graph, is that hthough the strong (-ve) relationship supports my research focus on the connection between digital technology use and productivity outcomes among youth and even young adults, remember that correlation doesn't imply causation - we can't definitively say that addiction causes lower productivity (or vice versa) just from this correlation. Something worth noting.")
