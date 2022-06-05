import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats (Rushing) explorer')

st.markdown("""
This app performs simple webscraping of NFL football player stats data (focusing on rushing)!
* **Python libs:** base64, streamlit, pandas, numpy
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

st.sidebar.header('User input features')
selected_year = st.sidebar.selectbox("Year", list(reversed(range(1990, 2022))))

# Web scrapping
# https://www.pro-football-reference.com/years/2021/rushing.htm

@st.cache
def load_data(year):
  url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
  html = pd.read_html(url, header=1)
  df = html[0]
  raw = df.drop(df[df.Age == "Age"].index)
  raw = raw.fillna(0)
  player_stats = raw.drop(['Rk'], axis=1)
  return player_stats

players_stats = load_data(selected_year)

sorted_unique_team = sorted(players_stats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

unique_pos = ['RB', 'QB', 'WR', 'FB', 'TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

df_selected_team = players_stats[(players_stats.Tm.isin(selected_team)) & (players_stats.Pos.isin(selected_pos))]

st.header('Display player stats of selected team(s)')
st.write('Data dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

def filedownload(df):
  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()
  href = f"<a href='data:file/csv;base64,{b64}' download='player_stats.csv'>Download CSV file</a>"
  return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

#Heatmap
if st.button('Intercorrelation Heatmap'):
  st.header('Intercorrelation matrix Heatmap')
  df_selected_team.to_csv('output.csv', index=False)
  df = pd.read_csv('output.csv')

  corr = df.corr()
  mask = np.zeros_like(corr)
  mask[np.triu_indices_from(mask)] = True
  with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
  st.pyplot(f)