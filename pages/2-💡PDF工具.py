import streamlit as st
import PyPDF2
import os
import glob

# ('D:/3.报销/4月/4.16-18-203对账单.pdf', 'D:/3.报销/4月/4.17-18-203.pdf')
# 创建一个文件夹选择器
uploaded_folders = st.file_uploader("Choose a folder...", type="pdf", accept_multiple_files=True)
if st.button('合并文件'):
    if uploaded_folders is not None:
        pdf_merger = PyPDF2.PdfMerger()
        for uploaded_file in uploaded_folders:
            # st.write(uploaded_file.name)
            pdf_merger.append(uploaded_file)
        # 获取桌面路径
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        # st.write(desktop_path)
        output_path = desktop_path + '\合并结果.pdf'
        # st.write(output_path)
        pdf_merger.write(output_path)
# if uploaded_folders is not None:
    # 如果用户上传了文件夹，展示上传的文件夹的名称
    # st.write("Uploaded folder:", uploaded_folders)
