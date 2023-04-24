import pymongo
import streamlit as st
from pymongo import MongoClient as mc
from datetime import date,datetime
import requests
import time
import json

cluster = mc('mongodb+srv://Devesh:Devesh@phishingsite.ajbvsdh.mongodb.net/test')
db = cluster["DB"]
collection = db["Data"]

st.set_page_config (page_title="Phishing Site", page_icon="",layout="wide")
st.markdown(""" <style>#Sidebsr {visibility: hidden;}footer {visibility: hidden;}</style> """, unsafe_allow_html=True)
st.write('<style>div.block-container{padding-left:2.3rem;padding-top:0.9rem;}</style>', unsafe_allow_html=True)
st.markdown("<h2 style='color:#FFFFFF ;text-align: center; ;border-color:#66fcf1;background: #271c54;border-radius:15px;width: '1000';height: 150px;   '>Detecting a Phishing Site</h2>",unsafe_allow_html=True)
for i in range(1,3):
    st.write("")

col1, col2, col3,col4 = st.columns([2.5,1,9,1])

with col1:
    st.subheader('')
    project = st.selectbox("Select..",['Introduction', 'What is URL', 'Prediction','Predicted URL'])   

with col3:
    if project == 'Introduction':
        st.subheader('')
        st.image("w.jpg",width=680)
        st.subheader('')

        st.subheader('What is Phishing Site ?')
        st.subheader('')

        st.markdown("<h4 style='color:#FFFFFF; background:#24284E;padding:20px;border-radius:10px'> Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers.</h4>",unsafe_allow_html=True)
        st.subheader('')
        st.markdown("<h4 style='color:#FFFFFF; background:#24284E;padding:20px;border-radius:10px'>It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message.</h4>",unsafe_allow_html=True)
        st.subheader('')       
        st.markdown("<h4 style='color:#FFFFFF; background:#24284E;padding:20px;border-radius:10px'>The recipient is then tricked into clicking a malicious link, which can lead to the installation of malware, the freezing of the system as part of a ransomware attack or the revealing of sensitive information.</h4>",unsafe_allow_html=True)
        st.subheader('')
        st.markdown("<h4 style='color:#FFFFFF; background:#24284E;padding:20px;border-radius:10px'>An attack can have devastating results. For individuals, this includes unauthorized purchases, the stealing of funds, or identify theft.</h4>",unsafe_allow_html=True)

        st.subheader('')
        st.subheader('Flowchart:')
        st.image("q.png")


    if project == 'What is URL':

        st.subheader('')
        st.subheader('What is a URL and what does it do?')
        st.subheader('')
        st.info('The URL is an important part of a website. It’s what people type into their browser to find your site, and it is what search engines like Google use to index your pages for relevance. URLs are not only necessary for getting found online, but they also work as a way to tell you more about the page that someone wants you to see.')

        st.info('The URL can indicate what the page is about and how it relates to other pages on your site (if there is a subfolder called “/blog/” in the URL, it indicates that the page is a blog article). The URL will also be helpful when linking internally within your own website because it tells users which section of your site you want them to visit next.')
        st.subheader('')
        st.subheader('To fully understand what a URL is, you need to understand the different parts that make it up. ')
        st.subheader('A URL consists of multiple parts.')
        
        st.subheader('')
        st.image("url.png")
        st.subheader('')
        st.subheader('Protocol:')
        st.info('The protocol determines how the information requests travel from a user to a domain and back. Big brands and self-respecting entities will use HTTPS over HTTP because it’s more secure. This often leaves HTTP links as partners in crime for URL phishing attacks')

        st.subheader('')
        st.subheader('Subdomain:')
        st.info('Subdomains are a way of splitting up a website into different sections. WWW is also considered a subdomain.')

        st.subheader('')
        st.subheader('Second-level domain')
        st.info('This is basically your domain name, without the top-level domain. In our domain name, “one.com”, the word “one” represents are second-level domain.')

        st.subheader('')
        st.subheader('Top-level domain')
        st.info('The top-level domain, or domain extension, is the final part of the domain name. For example, .com, .net or .eu.')

        st.subheader('')
        st.subheader('Path')
        st.info('The path is mostly defined by the URL structure of your website.')



    if project == 'Prediction':

        with st.container():
            st.header('')
            st.subheader('Enter a URL...')
            # name = 
            name = st.text_input("..",value="https://www.geeksforgeeks.org/")

            Urls = [name]

            API_key = 'ab224db80445e559096f4be1c9040a2cc198205c7dbf9c3c27ee2a515b5eb724'
            url = 'https://www.virustotal.com/vtapi/v2/url/report'
           
            parameters = {'apikey': API_key, 'resource': Urls[0]}            
            response= requests.get(url=url, params=parameters)
            json_response= json.loads(response.text)

            if json_response['positives'] <= 0:
                aa = 'Good'
                post = {"URL":name, "Label":aa}

            else:
                aa = 'Bad'
                post = {"URL":name, "Label":aa}

            if(st.button("Check",key=1)):
                time.sleep(5)
                if aa == 'Good':
                    st.success('The above URL is a valid URL',icon="✅")
                else:
                    st.warning('The above URL is a Phishing Site',icon="⚠") 

            st.write('')
            st.markdown("---")
            st.write('')

            st.subheader('Enter the above Predicted URL in DataBase?')
            if(st.button("Yes",key=2)):
                
           
                collection.insert_one(post)
                # st.experimental_rerun()
                st.write('The URL have been entered in DataBase.')

    if project == 'Predicted URL':
        # st.text('Predicted URL')
        q1, q2,q3 = st.columns([7,1,1])
        with q1:

            st.markdown("<h3 style='color:#66fcf1;text-align: center;'>URL</h3>",unsafe_allow_html=True)
            st.write('')
            for record in collection.find({},{ "_id": 0,"URL":1 }):
                for v in record.values():              
                    def header(v):                 
                        st.markdown(f'<p style="border-style: solid;border-color:#66fcf1;background-color:#271c54;text-align: center;padding:18.2px; color:white; font-size:16px; border-radius:8px;">{v}</p>', unsafe_allow_html=True)
                    header(v)

        with q2:
            st.markdown("<h3 style='color:#66fcf1;text-align: center;'>Label</h3>",unsafe_allow_html=True)
            st.write('')
            for record in collection.find({},{ "_id": 0,"Label":1 }):
                for v in record.values():              
                    def header(v):                 
                        st.markdown(f'<p style="border-style: solid;border-color:#66fcf1;background-color:#271c54;text-align: center;padding:18.2px; color:white; font-size:16px; border-radius:8px;">{v}</p>', unsafe_allow_html=True)
                    header(v)

        with q3:
            for i in range(1,6):
                st.write('')
            for record in collection.find({},{ "_id": 1}):
                for vv in record.values():
                    if st.button("🗑",key=vv):
                        delete = {"_id": vv}
                        collection.delete_one(delete)
                        st.experimental_rerun()			
                    st.markdown("""<style>.stButton > button {border-style: solid;border-color:#66fcf1;color: white;background: #271c54;width: 40px;height: 51px;}</style>""", unsafe_allow_html=True)