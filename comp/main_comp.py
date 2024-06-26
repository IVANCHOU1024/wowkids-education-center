import streamlit_antd_components as sac
import streamlit as st
from comp import mysql_comp

abilities = ['Perception', 'Application', 'Innovation', 'Business Sense', 'Social Impact',
             'Reasoning', 'Communication', 'Hands-On Skills', 'Experiment Design', 'Data Analysis']
MI = []
for item in abilities:
    i = sac.SegmentedItem(item)
    MI.append(i)


def main_menu(identity):
    with st.sidebar:
        if identity == 'teacher':
            selected = sac.menu([
                sac.MenuItem('Student register'),
                sac.MenuItem('STEM Capability Test')
            ], format_func='upper', size='sm', color="#7b2e76")
        elif identity == 'student':
            selected = sac.menu([
                sac.MenuItem('STEM Capability Test Report')
            ], format_func='upper', size='sm', color="#7b2e76")
        elif identity == 'none':
            selected = sac.menu([
                sac.MenuItem('Home')
            ], format_func='upper', size='sm', color="#7b2e76")

    return selected


def test_menu():
    selected = sac.segmented(MI, size='sm', divider=False, use_container_width=True, return_index=True)

    return selected


def login():
    ID, PSWD, notification = "", "", "Not logged in"
    login_sta = 0

    if "status" not in st.session_state:
        st.session_state.status = "Not logged in"
        st.session_state.notification = "Not logged in"
        st.session_state.pswd = "None"

    if login_sta == 0 and st.session_state.status == "Not logged in":
        ID = st.sidebar.text_input('Name 姓名')
        PSWD = st.sidebar.text_input('Password 密码')

        st.sidebar.caption(st.session_state.notification)

        with st.sidebar:
            if st.sidebar.button("LOG IN 登入", type="primary", use_container_width=True):
                login_sta = 1

    else:
        user_show = "Hello，" + st.session_state.status
        st.sidebar.title(user_show)

        if st.sidebar.button("LOG OUT 登出", type="primary", use_container_width=True):
            st.session_state.status = "Not logged in"
            st.session_state.notification = "Not logged in"
            st.experimental_rerun()

    if login_sta:
        st.session_state.status, st.session_state.notification, st.session_state.pswd = mysql_comp.mysql_login(ID, PSWD)
        st.experimental_rerun()

    return st.session_state.status, st.session_state.pswd
