import streamlit as st
import pandas as pd
from comp import main_comp, page
import streamlit_antd_components as sac


st.set_page_config(page_title="Wowkids Education Center", page_icon=None, layout='wide', initial_sidebar_state='expanded', menu_items=None)

with st.sidebar:
    st.image('./pictures/logo.png', caption=None, width=None, use_column_width=True, clamp=False, channels='RGB',
             output_format='auto')
    st.text('')

user, pswd = main_comp.login()
st.sidebar.divider()

print(user)


if user == 'Not logged in':
    with st.sidebar():
        selected = sac.menu([
            sac.MenuItem('Home')
        ], format_func='upper', size='sm', color="#7b2e76")
elif user == 'teacher':
    with st.sidebar():
        selected = sac.menu([
            sac.MenuItem('STEM Capability Test')
        ], format_func='upper', size='sm', color="#7b2e76")
else:
    with st.sidebar():
        selected = sac.menu([
            sac.MenuItem('STEM Capability Test Report')
        ], format_func='upper', size='sm', color="#7b2e76")


match selected:
    case 'Home':
        page.Home()
    case 'STEM Capability Test':
        page.Test()
    case 'STEM Capability Test Report':
        page.Report(user, pswd)
    case 'Student register':
        page.Register()