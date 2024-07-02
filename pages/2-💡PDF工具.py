import streamlit as st
import PyPDF2
import os
# 创建一个文件夹选择器
uploaded_folders = st.file_uploader("请选择PDF文件...", type="pdf", accept_multiple_files=True)
pdf_merger = PyPDF2.PdfMerger()
if st.button('合并文件'):
    if len(uploaded_folders) >= 1:
        for uploaded_file in uploaded_folders:
            pdf_merger.append(uploaded_file)
        st.write('合并成功')
        # 使用一个临时文件名来保存合并后的PDF
        with open("merged.pdf", "wb") as file:
            pdf_merger.write(file)
        # 清除临时文件
        pdf_merger.close()
        # 下载按钮
        btn = st.download_button(
            label="📥 下载文件",
            data=open("merged.pdf", "rb").read(),
            file_name="合并文件.pdf",
            mime="application/pdf",
        )
        # 删除临时文件
        os.remove("merged.pdf")
    else:
        st.write("请上传1个及以上的文件")
