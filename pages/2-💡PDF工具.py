import streamlit as st
import PyPDF2
import os
import glob
def pdf_merge(pdf_list):
    # 获取当前文件夹路径
    # folder_path = os.getcwd()
    pdf_merger = PyPDF2.PdfMerger()
    # pdf_list = sorted(glob.glob(os.path.join(folder_path, '*.pdf')))
    pdf_list = sorted(pdf_list)
    # 遍历当前文件夹中的文件
    i = 0
    for pdf in pdf_list:
        print(pdf[-3:])
        if pdf[-3:] == 'pdf':
            pdf_merger.append(pdf)
            i += 1
    if i > 0:
        pdf_merger.write('D:/3.报销/4月/合并结果.pdf')
        pdf_merger.close()
# ('D:/3.报销/4月/4.16-18-203对账单.pdf', 'D:/3.报销/4月/4.17-18-203.pdf')
# 创建一个文件夹选择器
uploaded_folders = st.file_uploader("Choose a folder...", type="pdf", accept_multiple_files=True)
if st.button('合并文件'):
    st.write(len(uploaded_folders))
    if uploaded_folders is not None:
        pdf_merger = PyPDF2.PdfMerger()
        for uploaded_file in uploaded_folders:
            # st.write(uploaded_file.name)
            pdf_merger.append(uploaded_file)
        pdf_merger.write('合并结果.pdf')
# if uploaded_folders is not None:
    # 如果用户上传了文件夹，展示上传的文件夹的名称
    # st.write("Uploaded folder:", uploaded_folders)
