import streamlit as st
import streamlit_antd_components as sac
from streamlit_echarts import st_echarts
import time
from comp import mysql_comp
from streamlit_modal import Modal

abilities = ['Perception', 'Application', 'Innovation', 'Business Sense', 'Social Impact',
                 'Reasoning', 'Communication', 'Hands-On Skills', 'Experiment Design', 'Data Analysis']
abilities_detail = [
                    "Perseption 洞察力",
                    "Application 应用",
                    "Innovation 创新",
                    "Business sense 商业",
                    "Social impact 社会影响力",
                    "Reasoning 推理思维",
                    "Communication 沟通艺术",
                    "Hands On Skills 操作技能",
                    "Experiment Design 实验设计",
                    "Data Analysis 数据分析"
                    ]
interpretation_en = [
    'Able to accurately understand and operate the equipment demonstrated by the coach skillfully.',
    'The ability to extract the potential application scenarios, target users, and specific problems that the device can solve from the teacher\'s demonstration.',
    'The application proposals show unique innovative thinking.',
    'Students\' proposed application schemes have significant market potential and commercial value.',
    'The application proposals put forward by students can have a positive impact at the social level.',
    'There is a reasonable logical connection between the application scenarios, target users, and problem-solving methods described in the application proposals presented by the students.',
    'Demostrated efficient communication and excellent expression skills.',
    'Students showed outstanding hands-on skills for implementation of creative works.',
    'Able to use the relationship between dependent variables and independent variables to design a structurally reasonable experiment.',
    'Students can accurately interpret experimental data and draw scientifically valid conclusions.'
]
interpretation_cn = [
    '能够准确理解并熟练操作老师展示的设备',
    '能从老师的设备演示中提炼出设备的潜在应用场景、目标用户以及能解决的具体问题',
    '学生提出的应用方案显示出独到的创新思维',
    '学生提出的应用方案具备明显的市场潜力和商业价值',
    '学生提出的应用方案能在社会层面产生积极影响',
    '学生阐述的应用方案中场景、目标用户和问题解决方式之间展现出合理的逻辑连贯性',
    '学生展现了高效沟通和精湛的表达技巧',
    '学生展现了出色的动手实践能力，成功完成了创意作品的搭建和技术实施',
    '学生能够利用因变量和自变量的关系设计出结构合理的实验',
    '学生能够准确地解读实验数据，得出科学有效的结论'
]

# my_modal = Modal(title="ATTENTION!", key="modal_key", max_width=500)
#
# if "confirm" not in st.session_state:
#     st.session_state["confirm"] = False


def Home():
    # st.title('Home')
    st.image('./pictures/Home/intro_l.png', caption=None, width=None, use_column_width=True, clamp=False,
                     channels='RGB',
                     output_format='auto')


def Register():

    st.title('Register')
    name = st.text_input("Name 姓名", value='')
    pswd = st.text_input("Password 密码 【EX：“探小星”（1月1日面试），密码设置“TXX0101”】", value='')
    date = st.date_input('Interview date 面试日期', format='YYYY/MM/DD')
    date = str(date)
    date = date[5]+date[6]+date[8]+date[9]

    print(name, pswd)

    sql = (
        "INSERT INTO account ("
        "name, password, id, role) "
        "VALUES (%s, %s, %s, %s)"
    )

    st.title('')
    if st.button("SAVE", type="primary", use_container_width=True):
        if name == '':
            st.error("Please enter name")
        elif pswd == '':
            st.error("Please enter password")
        else:
            mysql_comp.mysql_save(sql, (name, pswd, date, 'student'))
            st.success('Saved!')
            # st.warning('Save changes?')
            # if st.button("SURE", type="primary", use_container_width=True):
            #     mysql_comp.mysql_save(sql, (name, pswd, date, 'student'))
            #     st.success('Saved!')
            # with my_modal.container():
            #     st.markdown('Are you sure you want to save？')
            #     st.button("SURE", key="confirm")

    # if st.session_state["confirm"]:
    #     st.session_state["confirm"] = False
    #     mysql_comp.mysql_save(sql, (name, pswd, date, 'student'))
    #     st.experimental_rerun()


def Test():
    st.title('Test')
    st.markdown(f'## Student\'s information 学生信息')
    ch1 = st.columns(4)
    with ch1[0]:
        name = st.text_input("Name 姓名")
    with ch1[1]:
        gender = st.selectbox("Gender 性别", ("男", "女"))
    with ch1[2]:
        school = st.text_input("School 学校")
    with ch1[3]:
        grade = st.number_input("Grade 年级", 0, 12, 6)

    pswd = st.text_input("Password 密码 【EX：“探小星”（1月1日面试），密码设置“TXX0101”】", value='')

    st.divider()

    st.markdown(f'## Student\'s test 测试记录')
    s1, r1 = scoring_items(
        'Perception',
        '洞察力',
        'Able to accurately understand and operate the equipment demonstrated by the coach skillfully.',
        '能够准确理解并熟练操作老师展示的设备'
    )
    s2, r2 = scoring_items(
        'Application',
        '应用',
        'The ability to extract the potential application scenarios, target users, and specific problems that the device can solve from the teacher\'s demonstration.',
        '能从老师的设备演示中提炼出设备的潜在应用场景、目标用户以及能解决的具体问题'
    )
    s3, r3 = scoring_items(
        'Innovation',
        '创新',
        'The application proposals show unique innovative thinking. ',
        '学生提出的应用方案显示出独到的创新思维'
    )
    s4, r4 = scoring_items(
        'Business sense',
        '商业',
        'Students\' proposed application schemes have significant market potential and commercial value.',
        '学生提出的应用方案具备明显的市场潜力和商业价值'
    )
    s5, r5 = scoring_items(
        'Social impact',
        '社会影响力',
        'The application proposals put forward by students can have a positive impact at the social level.',
        '学生提出的应用方案能在社会层面产生积极影响'
    )
    s6, r6 = scoring_items(
        'Reasoning',
        '推理思维',
        'There is a reasonable logical connection between the application scenarios, target users, and problem-solving methods described in the application proposals presented by the students.',
        '学生阐述的应用方案中场景、目标用户和问题解决方式之间展现出合理的逻辑连贯性'
    )
    s7, r7 = scoring_items(
        'Communication',
        '沟通艺术',
        'Demostrated efficient communication and excellent expression skills.',
        '学生展现了高效沟通和精湛的表达技巧'
    )
    s8, r8 = scoring_items(
        'Hands On Skills',
        '技术操作技能',
        'Students showed outstanding hands-on skills for implementation of creative works.',
        '学生展现了出色的动手实践能力，成功完成了创意作品的搭建和技术实施'
    )
    s9, r9 = scoring_items(
        'Experiment Design',
        '实验设计',
        'Able to use the relationship between dependent variables and independent variables to design a structurally reasonable experiment.',
        '学生能够利用因变量和自变量的关系设计出结构合理的实验'
    )
    s10, r10 = scoring_items(
        'Data Analysis',
        '数据分析',
        'Students can accurately interpret experimental data and draw scientifically valid conclusions.',
        '学生能够准确地解读实验数据，得出科学有效的结论'
    )

    total_score = s1 + s2 + s3 + s4 + s5 + s6 + s7+ s8 + s9 + s10
    record_data = [r1, r2, r3, r4, r5, r6, r7, r8, r9, s10]

    st.divider()

    st.markdown(f'## Result 评测结果')
    # if total_score >= 95:
    #     class_level = "P"
    # elif 95 > total_score >= 80:
    #     class_level = "C+P"
    # elif 80 > total_score >= 60:
    #     class_level = "C"
    # else:
    #     class_level = "F"

    examiner = st.selectbox("Examiner 面试教练", ("张武彩", "周毅荣"))
    class_level = st.selectbox("Applicable Class 可申请课程", ("C+P", "C", "F"))

    date = time.strftime("%m%d", time.localtime())

    sql1 = (
        "INSERT INTO account ("
        "name, password, id, role) "
        "VALUES (%s, %s, %s, %s)"
    )

    sql2 = (
        "INSERT INTO student_data ("
        "date, name, gender, school, grade, "
        "p_s, p_r, a_s, a_r, i_s, i_r, b_s, b_r, s_s, s_r, r_s, r_r, c_s, c_r, h_s, h_r, e_s, e_r, d_s, d_r, "
        "examiner, total_score, applicable_class) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )

    st.title('')

    if st.button("SAVE", type="primary", use_container_width=True):
        if name == '':
            st.error("Please enter name")
        elif school == '':
            st.error("Please enter school")
        elif pswd == '':
            st.error("Please enter password")
        elif r1 == '':
            st.error(f"Please enter the record of \"{abilities[0]}\"")
        elif r2 == '':
            st.error(f"Please enter the record of \"{abilities[1]}\"")
        elif r3 == '':
            st.error(f"Please enter the record of \"{abilities[2]}\"")
        elif r4 == '':
            st.error(f"Please enter the record of \"{abilities[3]}\"")
        elif r5 == '':
            st.error(f"Please enter the record of \"{abilities[4]}\"")
        elif r6 == '':
            st.error(f"Please enter the record of \"{abilities[5]}\"")
        elif r7 == '':
            st.error(f"Please enter the record of \"{abilities[6]}\"")
        elif r8 == '':
            st.error(f"Please enter the record of \"{abilities[7]}\"")
        elif r9 == '':
            st.error(f"Please enter the record of \"{abilities[8]}\"")
        elif r10 == '':
            st.error(f"Please enter the record of \"{abilities[9]}\"")
        else:
            mysql_comp.mysql_save(sql1, (name, pswd, date, 'student'))
            mysql_comp.mysql_save(sql2, (date, name, gender, school, grade,
                                        s1, r1, s2, r2, s3, r3, s4, r4, s5, r5, s6, r6, s7, r7, s8, r8, s9, r9, s10,
                                        r10,
                                        examiner, total_score, class_level))
            st.success('Saved!')

            # st.warning('Save changes?')
            # if st.button("SURE", type="primary", use_container_width=True):
            #     mysql_comp.mysql_save(sql, (date, name, gender, school, grade,
            #                                 s1, r1, s2, r2, s3, r3, s4, r4, s5, r5, s6, r6, s7, r7, s8, r8, s9, r9, s10,
            #                                 r10,
            #                                 examiner, total_score, class_level))
            #     st.success('Saved!')
            # with my_modal.container():
            #     st.markdown('Are you sure you want to save？')
            #     st.button("SURE", key="confirm")

    # if st.session_state["confirm"]:
    #     st.session_state["confirm"] = False
    #     mysql_comp.mysql_save(sql, (date, name, gender, school, grade,
    #                                 s1, r1, s2, r2, s3, r3, s4, r4, s5, r5, s6, r6, s7, r7, s8, r8, s9, r9, s10,
    #                                 r10,
    #                                 examiner, total_score, class_level))
    #     st.experimental_rerun()


def Report(user, pswd):
    st.title('Creative Project Evaluation Form')
    st.subheader('科创综合能力评估表')

    result = mysql_comp.mysql_search('*', 'account', 'name', user, 'password', pswd)

    if result == ():
        st.markdown('#### No Data')
    else:
        date = result[0]['id']
        data = mysql_comp.mysql_search('*', 'student_data', 'name', user, 'date', date)

        if data == '()':
            st.markdown('#### No Data')
        else:
            st.title('')
            st.markdown(f'###### Student\'s Name: {user}')
            st.markdown(f'###### Applicable Course: {data[0]["applicable_class"]}')
            st.title('')
            score = [
                data[0]['p_s'],
                data[0]['a_s'],
                data[0]['i_s'],
                data[0]['b_s'],
                data[0]['s_s'],
                data[0]['r_s'],
                data[0]['c_s'],
                data[0]['h_s'],
                data[0]['e_s'],
                data[0]['d_s']
            ]
            record = [
                data[0]['p_r'],
                data[0]['a_r'],
                data[0]['i_r'],
                data[0]['b_r'],
                data[0]['s_r'],
                data[0]['r_r'],
                data[0]['c_r'],
                data[0]['h_r'],
                data[0]['e_r'],
                data[0]['d_r']
            ]

            option = {
                "legend": {"data": ["full score", "actual score"]},
                "radar": {
                    "indicator": [
                        {"name": f"Perseption\n洞察力: {score[0]}", "max": 10},
                        {"name": f"Application\n应用: {score[1]}", "max": 10},
                        {"name": f"Innovation\n创新: {score[2]}", "max": 10},
                        {"name": f"Business sense\n商业: {score[3]}", "max": 10},
                        {"name": f"Social impact\n社会影响力: {score[4]}", "max": 10},
                        {"name": f"Reasoning\n推理思维: {score[5]}", "max": 10},
                        {"name": f"Communication\n沟通艺术: {score[6]}", "max": 10},
                        {"name": f"Hands On Skills\n操作技能: {score[7]}", "max": 10},
                        {"name": f"Experiment Design\n实验设计: {score[8]}", "max": 10},
                        {"name": f"Data Analysis\n数据分析: {score[9]}", "max": 10}
                    ]
                },
                "series": [
                    {
                        "name": "",
                        "type": "radar",
                        "color": "purple",
                        "data": [{
                                "value": score
                            }],
                    }
                ],
            }
            st_echarts(option, height="300px")

            #     score_data = {
            #         'Ability Evaluation 能力评估': abilities,
            #         'Full Score 满分': ['10', '10', '10', '10', '10', '10', '10', '10', '10', '10'],
            #         'Score 得分': score
            #     }
            #     score_df = pd.DataFrame(score_data)
            #     print(score_df)
            #     st.dataframe(score_df, use_container_width=True, hide_index=True, column_config=None)
            st.title('')

            tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(abilities)
            with tab1:
                report_show(abilities_detail[0], interpretation_en[0], interpretation_cn[0], score[0], record[0])
            with tab2:
                report_show(abilities_detail[1], interpretation_en[1], interpretation_cn[1], score[1], record[1])
            with tab3:
                report_show(abilities_detail[2], interpretation_en[2], interpretation_cn[2], score[2], record[2])
            with tab4:
                report_show(abilities_detail[3], interpretation_en[3], interpretation_cn[3], score[3], record[3])
            with tab5:
                report_show(abilities_detail[4], interpretation_en[4], interpretation_cn[4], score[4], record[4])
            with tab6:
                report_show(abilities_detail[5], interpretation_en[5], interpretation_cn[5], score[5], record[5])
            with tab7:
                report_show(abilities_detail[6], interpretation_en[6], interpretation_cn[6], score[6], record[6])
            with tab8:
                report_show(abilities_detail[7], interpretation_en[7], interpretation_cn[7], score[7], record[7])
            with tab9:
                report_show(abilities_detail[8], interpretation_en[8], interpretation_cn[8], score[8], record[8])
            with tab10:
                report_show(abilities_detail[9], interpretation_en[9], interpretation_cn[9], score[9], record[9])

                # ch = st.columns(3)
                # with ch[0]:
                #     st.markdown(f'### {abilities[i]}')
                #     st.markdown(f'#### score:{score[i]}')
                # with ch[1]:
                #     st.markdown(f'###### {interpretation[i]}')
                #
                # st.divider()


def report_show(p1, p2, p3, p4, p5):
    st.markdown(f'#### {p1}')
    st.markdown(f'#### Score: {p4}')
    st.write(f'#### Interpretation:')
    st.write(f'{p2}')
    st.write(f'{p3}')
    st.markdown(f'#### Record:')
    st.write(f'{p5}')


def Perception():
    st.title('PERCEPTION 洞察力', anchor=None)
    st.write('')
    st.write('Able to accurately understand and operate the equipment demonstrated by the coach skillfully.')
    st.write('能够准确理解并熟练操作老师展示的设备')
    st.write('')

    st.markdown('### Score 得分')
    score = sac.rate(value=2.0, count=10, symbol=sac.BsIcon('circle-fill', size=None, color=None))
    st.markdown(f'#### Score: {int(score)}')
    st.write('')

    st.markdown('### Record 学生记录')
    st.text_area('',key='')


def scoring_items(item_en, item_cn, expl_en, expl_cn):
    with st.expander(item_en.upper()+item_cn):
        st.markdown(f'### {item_en.upper()} {item_cn}')
        st.write('')
        st.markdown(f'###### {expl_en}\n{expl_cn}')
        # st.markdown(f'###### {expl_cn}')
        st.write('')

        # st.markdown(f'### {item_en} Score')
        score = st.number_input(f'{item_en} Score {item_cn}得分', 0, 10, 8, key=f'slider_{item_en}')
        st.write(f'Score: {int(score)}')
        st.write('')
        # st.markdown('### Record')
        record = st.text_area(f'{item_en} Record {item_cn}记录', key=f'text_{item_en}')

        # st.divider()

    return score, record