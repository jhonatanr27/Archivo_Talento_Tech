import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="Título de tu Página",
    page_icon="🌟",  # Puedes usar un emoji o una imagen
    layout="wide",  # Opciones: "centered" o "wide"
    initial_sidebar_state="auto",  # Opciones: "auto", "expanded" o "collapsed"
    menu_items={
        "Get Help": "https://www.tusitio.com/ayuda",
        "Report a Bug": "https://www.tusitio.com/reportar-error",
        "About": "# Información sobre la página"
    }
)
