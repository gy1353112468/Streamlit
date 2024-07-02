import streamlit as st
import PyPDF2
import os
import json
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
        # btn = st.download_button(
        #     label="📥 下载文件",
        #     data=open("merged.pdf", "rb").read(),
        #     file_name="合并文件.pdf",
        #     mime="application/pdf",
        # )
        reader = PyPDF2.PdfReader("merged.pdf")
        writer = PyPDF2.PdfWriter()
        # 遍历PDF的每一页
        for page in reader.pages:
            # st.write(page)
            # 获取页面的宽度和高度
            width, height = page['/MediaBox'][2], page['/MediaBox'][3]
            # page['/MediaBox'][3]= 396
            # st.write(width, height)
            a4_width, a4_height = 595.2, 841.8
            a5_width, a5_height = 420.8, 595.2
            scale_factor = a5_width / a4_width
            if width < height:
                page.mediabox.upper_right = (595.2, 841.8)
                page.mediabox.lower_left = (0, 420.8)
            # 更新页面属性以适应A5大小
            writer.add_page(page)
        # for page in writer.pages:
        #     st.write(page)
        with open("result.pdf", "wb") as out:
            writer.write(out)
        # 下载按钮
        btn = st.download_button(
            label="📥 下载文件",
            data=open("result.pdf", "rb").read(),
            file_name="合并文件.pdf",
            mime="application/pdf",
        )
        # 删除临时文件
        os.remove("merged.pdf")
        os.remove("result.pdf")
    else:
        st.write("请上传1个及以上的文件")

