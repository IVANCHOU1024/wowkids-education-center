import streamlit as st
import pandas as pd
from comp import main_comp, page
import streamlit_antd_components as sac


st.set_page_config(page_title="Wowkids Education Center", page_icon=None, layout='wide', initial_sidebar_state='auto', menu_items=None)

with st.sidebar:
    st.image('./pictures/logo.png', caption=None, width=None, use_column_width=True, clamp=False, channels='RGB',
             output_format='auto')
    st.text('')

user, pswd = main_comp.login()
st.sidebar.divider()

print(user)


if user == 'Not logged in':
    identity = 'none'
elif user == 'teacher':
    identity = 'teacher'
else:
    identity = 'student'

print(identity)

main_selected = main_comp.main_menu(identity)

match main_selected:
    case 'Home':
        page.Home()
    case 'STEM Capability Test':
        page.Test()
    case 'STEM Capability Test Report':
        page.Report(user, pswd)
