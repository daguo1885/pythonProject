# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

st.set_page_config(page_title='多页面测试streamlit', page_icon='moon', layout="wide")
# Press the green button in the gutter to run the script.

st.header('这是一个关于Streamlit多页面功能的测试')

st.text('下面测试radio排列功能')

ab = st.radio('test', ['first', 'second', 'third'], horizontal=1)

st.info(f'你选择的是{ab}')

codea = st.text_input('请输入授权码！')

if codea == 'abc':
    st.success('You have got the right code!')
    st.text('new')
else:
    pass

# 侧边栏
def side_bar():
    # st.sidebar.image(pic, width=100)
    st.sidebar.title("客舱派遣辅助系统")
    info = st.sidebar.empty()
    info.caption('请在下方选择需要运行的功能：')

    # 数据准备
    data_prepare = st.sidebar.expander("数据准备")
    if data_prepare.button('自动更新'):
        info.caption('自动更新：自动更新database数据源')
        st.session_state.func_code = '自动更新'
    if data_prepare.button('手动更新'):
        info.caption('手动更新database数据表')
        st.session_state.func_code = '手动更新'
    if data_prepare.button('更新核酸检测数据'):
        info.caption('自动更新核酸检测数据')
        st.session_state.func_code = '核酸检测'
    # 派遣检查
    roster_check = st.sidebar.expander("派遣检查")
    if roster_check.button('连飞四天风险排查'):
        info.caption('连飞四天风险排查')
        st.session_state.func_code = '连飞四天风险排查'
    if roster_check.button('AC法规检查'):
        info.caption('解析AC法规检查结果')
        st.session_state.func_code = 'AC法规检查'
    if roster_check.button('衔接风险检查'):
        info.caption('解析外围衔接查询表')
        st.session_state.func_code = '衔接风险检查'
    if roster_check.button('学员带飞检查'):
        info.caption('学员带飞检查')
        st.session_state.func_code = '学员带飞检查'
    # 防疫检查
    fangyi = st.sidebar.expander('防疫检查')
    fy1, fy2 = fangyi.columns(2)
    if fy1.button('航站核酸检查'):
        info.caption('根据相关航站要求，检查已排人员48小时、72小时核酸符合性')
        st.session_state.func_code = '航站核酸检查'
    if fy1.button('运行轨迹排查'):
        info.caption('完成相关航站运行轨迹排查')
        st.session_state.func_code = '运行轨迹排查'
    if fy1.button('航班风险等级'):
        info.caption('根据指挥中心发布的航班风险等级表，查询客舱相应航班乘务长信息')
        st.session_state.func_code = '航班风险等级'
    if fy1.button('物资发放检查'):
        info.caption('乘务组防疫物资领用扫码记录检查')
        st.session_state.func_code = '物资发放检查'
    if fy2.button('核酸检测监控'):
        info.caption('根据本地核酸检测数据，生成核酸检测监控报表')
        st.session_state.func_code = '核酸检测监控'
    if fy2.button('核酸检测查询'):
        info.caption('根据本地核酸检测数据，生成核酸检测监控报表')
        st.session_state.func_code = '核酸检测查询'
    if fy2.button('南京乘务名单'):
        info.caption('自动生成南京机场公安要求的乘务组信息表')
        st.session_state.func_code = '南京乘务名单'
    if fy2.button('涉疫航班人员'):
        info.caption('自动生成涉疫航班乘务组报表')
        st.session_state.func_code = '航班人员报表'
    # 统计报表
    reporter = st.sidebar.expander('统计报表')
    if reporter.button('日运行简报'):
        info.caption('统计指定日期运行简报')
        st.session_state.func_code = '日运行简报'
    if reporter.button('周运行简报'):
        info.caption('统计上周运行数据')
        st.session_state.func_code = '周运行简报'
    if reporter.button('月统计报表'):
        info.caption('统计上月运行数据')
        st.session_state.func_code = '月统计报表'
    # 实用工具
    tool = st.sidebar.expander('实用工具')
    if tool.button('Excel文件拼接'):
        info.caption('Excel合并工具')
        st.session_state.func_code = 'Excel合并工具'
    if tool.button('多人任务查询'):
        info.caption('多人任务查询')
        st.session_state.func_code = '多人任务查询'
    if tool.button('员工号查询'):
        info.caption('批量查询员工号信息')
        st.session_state.func_code = '员工号查询'
    # 排班公平
    fair = st.sidebar.expander("排班公平")
    a, b = fair.columns(2)
    a.button('飞行小时检查')
    a.button('优质航线')
    b.button('一类航线')
    st.sidebar.markdown('</br>', unsafe_allow_html=True)
    st.sidebar.markdown('</br>', unsafe_allow_html=True)
    st.sidebar.markdown('</br>', unsafe_allow_html=True)
    st.sidebar.markdown('</br>', unsafe_allow_html=True)
    htm = '''
        <HR style="FILTER:alpha(opacity=20,finishopacity=0,style=1)"width="85%"color=#987cb9 SIZE=1>
        '''
    st.sidebar.markdown(htm, unsafe_allow_html=True)
    st.sidebar.caption('重庆客舱生产派遣版权所有(2022)')


side_bar()




