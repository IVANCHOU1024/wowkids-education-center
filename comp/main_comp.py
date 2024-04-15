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
        match identity:
            case 'teacher':
                selected = sac.menu([
                    sac.MenuItem('STEM Ability Test')
                ], format_func='upper', size='sm')
            case 'student':
                selected = sac.menu([
                    sac.MenuItem('Home'),
                    sac.MenuItem('STEM Ability Test Report')
                ], format_func='upper', size='sm')
            case 'none':
                selected = sac.menu([
                    sac.MenuItem('Home')
                ], format_func='upper', size='sm')

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

    if login_sta == 0 and st.session_state.status == "Not logged in":
        ID = st.sidebar.text_input('Name 姓名')
        PSWD = st.sidebar.text_input('Password 密码')

        st.sidebar.caption(st.session_state.notification)

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
        st.session_state.status, st.session_state.notification = mysql_comp.mysql_login(ID, PSWD)
        st.experimental_rerun()

    return st.session_state.status