import plotly.graph_objects as go
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import os
import time
import datetime
from datetime import timedelta,date

import flask

# Tous les programmes qui permettent de récupérer les données
import read_aida
import lecture_mesoNH
import lecture_surfex




import navigation

from navigation import app

from navigation import today
from navigation import yesterday
from navigation import tomorow

from navigation import start_day
from navigation import end_day

from navigation import doy1
from navigation import doy2


#import comp_obs_model
#from comp_obs_model import *

#import sondages
#from sondages import *

#import rejeu_mesonh
#from rejeu_mesonh import *

########################
#
#   Rejeu SURFEX
#
########################
    
menu = html.Div([
        dcc.Link('Notice__', href='/MeteopoleX/notice'),
        dcc.Link('__Comparaisons Obs MétéoFlux/Modèles__', href='/MeteopoleX/'),
        dcc.Link('__Sondages__', href='/MeteopoleX/rs'),
        dcc.Link('__Rejeu MésoNH', href='/MeteopoleX/mesoNH'),
        ],className="twelve columns",style={"text-align": "right", "justifyContent":"center"})

surfex_layout = html.Div([
    html.H1('Rejeu de SURFEX'),
    menu
],className="twelve columns",style={"text-align": "center", "justifyContent":"center"})
    
    

