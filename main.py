import streamlit as st
import pandas as pd
from comp import main_comp, page


st.set_page_config(page_title="None", page_icon=None, layout='wide', initial_sidebar_state='auto', menu_items=None)

st.sidebar.image('./pictures/logo_tr.png', caption=None, width=None, use_column_width=True, clamp=False, channels='RGB',
         output_format='auto')
st.sidebar.text('')
user = main_comp.login()
st.sidebar.divider()

print(user)

if user == 'Not logged in':
    identity = 'none'
elif user == 'astra_teacher':
    identity = 'teacher'
else:
    identity = 'student'

main_selected = main_comp.main_menu(identity)

match main_selected:
    case 'Home':
        page.Home()
    case 'STEM Ability Test':
        page.Test()
    case 'STEM Ability Test Report':
        page.Report()
