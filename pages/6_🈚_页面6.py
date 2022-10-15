import streamlit as st

st.set_page_config(page_title='子页面1', layout='wide')

st.header('This is a subpage')


def multi_checkbox(label, lst, horizontal: bool = False, cols=5):
    """
    # 实现复选框组功能，可实现水平排列
    :param label: 复选框组的标签
    :param lst: 要显示的列表
    :param horizontal: 水平放置设置，默认False
    :param cols: 当采取水平放置时，每一行显示的个数
    :return: 选中复选框列表
    """
    st.text(label)
    ff = []
    if horizontal:                  # 横向排列
        w = st.columns(cols)        # cols默认一行放置5个
    for j, i in enumerate(lst):
        if horizontal:
            j = j % cols
            with w[j]:
                zz = st.checkbox(i)
                if zz:
                    ff.append(i)
        else:
            zz = st.checkbox(i)
            if zz:
                ff.append(i)
    return ff


ab = multi_checkbox('Just a test!', ['a', 'b', 'c', 'd', 'e', 'f', 'g'], True, 3)

st.text(ab)

xa = st.radio('单选', ['ac', 'b', 'cd', 'ef'], horizontal=True)

st.text(xa)