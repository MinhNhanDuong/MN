if True:
    if True: #import libraries
        import streamlit as st

        import numpy as np
        import pandas as pd
        
        import pickle as pk
        from PIL import Image
    ############################

    ############################
    def main():
        st.title('Titanic - Dự đoán còn sống hay đã chết')

        #Load model
        st.write('Chưa được lập trình!')
        
        menu=['Kiểm tra model','Dự đoán hành khách','Gán nhãn và lưu file']
        choice=st.sidebar.selectbox('Menu',menu)
        st.subheader(choice)

        if choice=='Kiểm tra model':
            #Load dữ liệu
            st.subheader('1. Load dữ liệu có chứa label')

            file_csv = st.file_uploader("Upload file csv tại đây", type=([".csv"]))
            st.markdown("""Nếu không có mẫu, bạn có thể tham khảo data <a href="https://github.com/Thienlong1312/titanic-pred-app/tree/main/data/">tại đây</a>.""", unsafe_allow_html=True,)
            if st.button('Hoặc đơn giản nhấn vào đây!'):
                file_csv='data/titanic.csv'
            if file_csv:
                data=pd.read_csv(file_csv)
                if 'survived' not in data.columns:
                    st.write('Dữ liệu không có nhãn, vui lòng chọn dữ liệu khác')
                else:
                    #Xử lý dữ liệu
                    st.subheader('2. Xử lý dữ liệu')
                    st.write('Chưa được lập trình!')

                    #Chuẩn đoán dữ liệu
                    st.subheader('3. Chuẩn đoán dữ liệu')
                    st.write('Chưa được lập trình!')

                    #Vẽ biểu đồ
                    st.subheader('4. Vẽ biểu đồ')
                    st.write('Chưa được lập trình!')
            else:
                image = Image.open('image/titanic_image.jpg')
                st.image(image, caption=None,use_column_width=True,width=None)
        elif choice=='Dự đoán hành khách':
            st.write('- Dự đoán hành khách sau chuyến titanic còn sống hay đã chết hoặc bạn có thể thử vận may của bạn')
            st.write('(Câu hỏi * là những câu hỏi bắt buộc)')
            st.subheader('Lựa chọn thuộc tính')

            st.write('Chưa được lập trình!')

            if st.button('Dự đoán'):
                st.write('Chưa được lập trình!')
                st.write('Chưa được lập trình!')
            else:
                st.write('- ...')
                st.write('- ...')
                st.write('- ...')
                st.write('- ...')
                st.write('- ...')
                st.write('- ...')
                st.write('- ...')
                st.write('- ...')
        else:
            #Load dữ liệu
            st.subheader('1. Load dữ liệu muốn gán nhãn')

            file_csv = st.file_uploader("Upload a csv file", type=([".csv"]))
            st.markdown("""Nếu không có mẫu, bạn có thể tham khảo data <a href="https://github.com/Thienlong1312/titanic-pred-app/tree/main/data/">tại đây</a>.""", unsafe_allow_html=True,)
            if st.button('Hoặc đơn giản nhấn vào đây!'):
                file_csv='data/titanic_new.csv'
            if file_csv:
                X=pd.read_csv(file_csv)
                if 'survived' in X.columns:
                    st.write('Dữ liệu đã có nhãn, vui lòng chọn dữ liệu khác')
                
                else:
                    #Xử lý dữ liệu
                    st.subheader('2. Xử lý dữ liệu')
                    st.write('Chưa được lập trình!')

                    #Gán nhãn cho dữ liệu
                    st.subheader('3. Gán nhãn cho dữ liệu')
                    st.write('Chưa được lập trình!')

                    #Kiểm tra xem có dữ liệu nào model không đoán được
                    

                    #Tải dữ liệu xuống
                    st.write('Chưa được lập trình!')
            else:
                image = Image.open('image/titanic_image_2.jpg')
                st.image(image, caption=None,use_column_width=True,width=None)
        return

    if __name__=='__main__':
        main()





































































