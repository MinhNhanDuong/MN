import streamlit as st
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
from wordcloud import WordCloud
from utils import get_page_text

st.set_page_config(page_title = "Covid Fake News Detection")

@st.cache(allow_output_mutation=True)
def get_nlp_model(path):   
    return spacy.load(path)

def generate_output(text):
	cats = nlp(text).cats
	 
	if ((cats['FAKE'] > cats['REAL']) and (cats['FAKE'] > cats['OTHER'])):
		  st.markdown("<h1><span style='color:red'>This is a Covid Fake News!</span></h1>",
							 unsafe_allow_html=True) 
	elif ((cats['REAL'] > cats['FAKE']) and (cats['REAL'] > cats['OTHER'])):
		  st.markdown("<h1><span style='color:green'>This is a Covid Real News!</span></h1>",
							 unsafe_allow_html=True)
	else:
		  st.markdown("<h1><span style='color:yellow'>This is a OTHER news!</span></h1>",
							 unsafe_allow_html=True)
   
             
	q_text = '> '.join(text.splitlines(True))   
	q_text = '> ' + q_text
	st.markdown(q_text)

	wc = WordCloud(width = 1000, height = 600,
						random_state = 1, background_color = 'white',
						stopwords = STOP_WORDS).generate(text) 
		 
	fig, ax = plt.subplots()
	ax.imshow(wc)
	ax.axis('off')
	st.pyplot(fig)
	print(cats)

nlp = get_nlp_model('model')

desc = "Bạn có thể nhập URL của một bài báo hoặc dán trực tiếp đoạn text."

st.title("Covid Fake News Detection")
st.markdown(desc)
#st.subheader("Enter the URL address/text of a news article")
select_input = st.radio("Select Input:", ["URL", "Text"])

if select_input == "URL":
    url = st.text_input("URL")   
    if st.button("Run"):
        text = get_page_text(url)
        generate_output(text)  

else:
    text = st.text_area("Text", height=300)
    if st.button("Run"):
        generate_output(text) 

