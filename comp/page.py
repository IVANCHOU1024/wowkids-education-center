import streamlit as st
import streamlit_antd_components as sac
import pandas as pd
from streamlit_echarts import st_echarts
# from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder

abilities = ['Perception', 'Application', 'Innovation', 'Business Sense', 'Social Impact',
                 'Reasoning', 'Communication', 'Hands-On Skills', 'Experiment Design', 'Data Analysis']
abilities_detail = [
                    "Perseption\n洞察力",
                    "Application\n应用",
                    "Innovation\n创新",
                    "Business sense\n商业",
                    "Social impact\n社会影响力",
                    "Reasoning\n推理思维",
                    "Communication\n沟通艺术",
                    "Hands On Skills\n操作技能",
                    "Experiment Design\n实验设计",
                    "Data Analysis\n数据分析"
                    ]
interpretation = [
    'Able to accurately understand and operate the equipment demonstrated by the coach skillfully.\n能够准确理解并熟练操作老师展示的设备',
    'The ability to extract the potential application scenarios, target users, and specific problems that the device can solve from the teacher\'s demonstration.\n能从老师的设备演示中提炼出设备的潜在应用场景、目标用户以及能解决的具体问题',
    'The application proposals show unique innovative thinking.\n学生提出的应用方案显示出独到的创新思维',
    'Students\' proposed application schemes have significant market potential and commercial value.\n学生提出的应用方案具备明显的市场潜力和商业价值',
    'The application proposals put forward by students can have a positive impact at the social level.\n学生提出的应用方案能在社会层面产生积极影响',
    'There is a reasonable logical connection between the application scenarios, target users, and problem-solving methods described in the application proposals presented by the students.\n学生阐述的应用方案中场景、目标用户和问题解决方式之间展现出合理的逻辑连贯性',
    'Demostrated efficient communication and excellent expression skills.\n学生展现了高效沟通和精湛的表达技巧',
    'Students showed outstanding hands-on skills for implementation of creative works.\n学生展现了出色的动手实践能力，成功完成了创意作品的搭建和技术实施',
    'Able to use the relationship between dependent variables and independent variables to design a structurally reasonable experiment.\n学生能够利用因变量和自变量的关系设计出结构合理的实验',
    'Students can accurately interpret experimental data and draw scientifically valid conclusions.\n学生能够准确地解读实验数据，得出科学有效的结论'
]


def Home():
    # st.title('Home')
    st.image('./pictures/Home/intro_l.png', caption=None, width=None, use_column_width=True, clamp=False,
                     channels='RGB',
                     output_format='auto')


def Test():
    st.title('Test')
    st.markdown(f'## Student\'s information 学生信息')
    ch1 = st.columns(4)
    with ch1[0]:
        st.text_input("Name 姓名")
    with ch1[1]:
        st.selectbox("Gender 性别", ("男", "女"))
    with ch1[2]:
        st.text_input("School 学校")
    with ch1[3]:
        st.number_input("Grade 年级", 0, 12, 6)

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
    if total_score >= 95:
        class_level = "P"
    elif 95 > total_score >= 80:
        class_level = "C+P"
    elif 80 > total_score >= 60:
        class_level = "C"
    else:
        class_level = "F"

    examiner = st.selectbox("Examiner 面试教练", ("张武彩", "周毅荣"))
    st.markdown(f'###### Total Scpre 总分: {total_score}')
    st.markdown(f'###### Applicable Class 可申请课程: {class_level}')


def Report():
    st.title('Report')
    st.markdown('#### STEM Capability Assessment Form 科创综合能力评估表')
    ch = st.columns(2)
    with ch[0]:
        option = {
            "legend": {"data": ["full score", "actual score"]},
            "radar": {
                "indicator": [
                    {"name": "Perseption\n洞察力", "max": 10},
                    {"name": "Application\n应用", "max": 10},
                    {"name": "Innovation\n创新", "max": 10},
                    {"name": "Business sense\n商业", "max": 10},
                    {"name": "Social impact\n社会影响力", "max": 10},
                    {"name": "Reasoning\n推理思维", "max": 10},
                    {"name": "Communication\n沟通艺术", "max": 10},
                    {"name": "Hands On Skills\n操作技能", "max": 10},
                    {"name": "Experiment Design\n实验设计", "max": 10},
                    {"name": "Data Analysis\n数据分析", "max": 10}
                ]
            },
            "series": [
                {
                    "name": "预算 vs 开销（Budget vs spending）",
                    "type": "radar",
                    "color": "purple",
                    "data": [{
                            "value": [9, 9, 10, 9, 8, 9, 9, 9, 9, 9]
                        }],
                }
            ],
        }
        st_echarts(option, height="400px")
    with ch[1]:
        score_data = {
            'Ability Evaluation 能力评估': abilities,
            'Full Score 满分': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            'Score 得分': [9, 9, 10, 9, 8, 9, 9, 9, 9, 9]
        }
        score_df = pd.DataFrame(score_data)
        st.dataframe(score_df, use_container_width=True, hide_index=True, column_config=None)

    data = {
        'Capability 能力': abilities_detail,
        'Interpretation 解释': interpretation,
        'Record 学生记录': [9, 9, 10, 9, 8, 9, 9, 9, 9, 9]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True, column_config=None)



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