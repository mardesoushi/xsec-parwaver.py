import streamlit as st

## Modulos python
import altair as alt
from regex import D

from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation
from sklearn.metrics.pairwise import pairwise_distances
import tempfile
from haversine import Unit
import haversine as hs
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import os
import streamlit as st
import pandas as pd 
import numpy as np


st.set_page_config(
    page_title="LaTeX inputer",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

###########################################################################################################################
# Code start
st.title('Partial Wave Calculator')