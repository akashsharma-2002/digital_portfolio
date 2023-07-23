import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import base64

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "webpage" / "styles" / "main.css"
resume_file = current_dir / "webpage" / "assets" / "Akashsharma_ENG20AM0005.pdf"
profile_pic = current_dir / "webpage" / "assets" / "akash-profile-pic.png"
insta_log = current_dir / "webpage" / "assets" / "instaa.png"
linked = current_dir / "webpage" / "assets" / "linn.png"
twitter= current_dir / "webpage" / "assets" / "twit.png"
github= current_dir / "webpage" / "assets" / "gittu.png"
logo = current_dir / "webpage" / "assets" / "Akash-logos_white.png"
page_icon= current_dir / "webpage" / "assets" / "icon.jpeg"
fb= current_dir / "webpage" / "assets" / "fcb.png"
mail= current_dir / "webpage" / "assets" / "mail.png"
dssu= current_dir / "webpage" / "assets" / "dssu.png"
kvs= current_dir / "webpage" / "assets" / "kvs.png"

im=Image.open(page_icon)
st.set_page_config(
    page_title="Digital CV | Akash Sharma",
    page_icon=im,
    layout="wide",
)

logo = Image.open(logo)
st.image(logo, width=80)

# 1. as sidebar menu
selected=option_menu(
    menu_title=None,
    options=["Home","Project","Certificate","Education"],
    icons=["house","book","patch-check","book-half"],
    default_index=0,
    orientation='horizontal'
)

if selected=="Home":
    NAME = "Akash Sharma"

    DESCRIPTION = """
    A passionate 4th year B.Tech CSE student at Dayananda Sagar University, specializing in AI/ML, I strive for excellence and innovation.
    I love exploring new ideas and creating exciting machine learning projects. Python is my go-to language, and I feel confident using it. 
    My portfolio showcases my work, where I've used AI to solve practical problems. I'm always eager to learn and push the boundaries of what AI can do. I believe in the power of innovation and strive to make a positive impact through my work in artificial intelligence.
    """
    EMAIL = "akashbest2002@gmail.com"
    SOCIAL_MEDIA = {
        "Instagram": "https://www.instagram.com/akaashhh_._/",
        "LinkedIn": "https://www.linkedin.com/in/akash-sharma-bb6680179/",
        "GitHub": "https://github.com/akashsharma-2002",
        "Twitter": "https://twitter.com/AkashSh69346463",
        "Facebook": "https://www.facebook.com/profile.php?id=100095050960351",

    }

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')


        st.image(profile_pic, width=260)
    with col2:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')


        st.title(NAME)
        st.write(DESCRIPTION)
        st.write('\n')

        st.markdown('SKILLS')
        st.write('\n')

        st.write('Python, Machine learning, Django , MySql, Computer Vision, NLP')
        st.write('\n')
        st.write('\n')

        st.download_button(

            label="✉️ Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
    with col3:
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st_lottie("https://lottie.host/77ba898a-77a3-4d73-8e3b-f03c206c83b2/UL37hIr4Nb.json")

    # st.write('\n')
    # st.write('\n')

    insta_log = Image.open(insta_log)
    linked_log = Image.open(linked)
    twitter_logo = Image.open(twitter)
    git_logo = Image.open(github)
    fb_logo = Image.open(fb)
    mail_logo = Image.open(mail)
    st.write('---')
    st.subheader("SOCIAL MEDIA")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        # st_lottie("https://lottie.host/63f22454-5331-425c-adae-be1caa5ccabd/ZinnC1mpEq.json",width=70)
        st.image(linked_log, width=40)  # Replace with the correct path to your LinkedIn logo
        st.write('\n')
        st.markdown(f'<a href="{SOCIAL_MEDIA["LinkedIn"]}" target="_blank" style="color:blue;">LinkedIn</a>',
                    unsafe_allow_html=True)

    with col2:
        # st_lottie("https://lottie.host/aa6570d8-11bc-4689-a2bb-58eed4e1b784/tsWDZP44CK.json", width=70)
        st.image(insta_log, width=40)
        st.write('\n')
        st.markdown(f'<a href="{SOCIAL_MEDIA["Instagram"]}" target="_blank" style="color:pink;">Instagram</a>',
                    unsafe_allow_html=True)

    with col3:
        st.image(mail_logo, width=40)
        st.write('\n')
        st.markdown(f'<a href="mailto:akashbest2002@gmail.com">Gmail</a>',
                    unsafe_allow_html=True)

    with col4:
        st.image(twitter_logo, width=40)
        st.write('\n')
        st.markdown(f'<a href="{SOCIAL_MEDIA["Twitter"]}" target="_blank" style="color:blue;">Twitter</a>',
                    unsafe_allow_html=True)

    with col5:
        st.image(git_logo, width=40)
        st.write('\n')
        st.markdown(f'<a href="{SOCIAL_MEDIA["GitHub"]}" target="_blank" style="color:blue;">GitHub</a>',
                    unsafe_allow_html=True)

    with col6:
        st.image(fb_logo, width=40)
        st.write('\n')
        st.markdown(f'<a href="{SOCIAL_MEDIA["Facebook"]}" target="_blank" style="color:blue;">FaceBook</a>',
                    unsafe_allow_html=True)



elif selected=="Project":

    st.write('\n')
    st.title('PROJECTS')
    st.write("---")
    col1, col2 = st.columns(2,gap="large")

    #PROJECT 1- BANGLORE HOUSE PRICE PREDICTION

    with col1:
        st.subheader("1:  Banglore House price prediction")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write("●   The Goal of the Project is to predicit the price of house in banglore using linear regression")
        st.write("●    model offers accurate and reliable estimates of property prices in this bustling city. Leveraging a vast dataset of real estate features, including location, amenities, and property size")
        st.write("●    the model effectively predicts house prices to empower buyers and sellers with valuable insights. Its robust performance and impressive accuracy make it an indispensable tool for anyone navigating the competitive Bangalore real estate market. ")
        #st.markdown(f'<a href="https://github.com/akashsharma-2002/HOUSE-PRICE-PREDICITON-IN-BANGLORE">Banglore house price prediction</a>')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(
            " check out my work [ Banglore house price prediction](https://github.com/akashsharma-2002/HOUSE-PRICE-PREDICITON-IN-BANGLORE)")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('---')
    with col2:
        st_lottie('https://lottie.host/ea760d39-f67a-4f61-99bd-fcda27873c93/rTmaTCUmJB.json',width=340)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        #st.write('\n')
        st.write('---')

    #PROJECT 2-
    with col1:
        st.write('\n')
        st.subheader("2:  Wound Detox")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('● The objective of this project is to develop a wound detection and prescription system. The trained model exhibits an impressive 94% accuracy in identifying wounds and suggesting the appropriate next steps for treatment.')
        st.write('● n critical cases, the system will promptly notify the nearest hospital, ensuring urgent medical attention.')
        st.write("● For treatable wounds, the model will generate precise prescriptions for the suitable medications, thereby alleviating the challenges of crowded pharmacies. ")
        st.write("● With this advanced solution, we aim to provide timely and effective wound care, enhancing healthcare accessibility and ensuring better patient outcomes.")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write()
        st.write('\n')
        st.write('\n')
        st.write('---')
    with col2:
        st.write('\n')
        st.write('\n')

        st_lottie('https://lottie.host/4c6bbcf3-a81c-4053-a2ef-be6d7c7925cd/q6yXlk0vbc.json',width=340)
        st.write('\n')
        st.write('\n')
        st.write('---')
        #st.write('\n')

    with col1:
        st.write('\n')
        st.subheader('Smart Virtual Personal Assistant')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write("●  This project aims to provide extensive access to your computer, enabling it to perform various tasks on your behalf, such as sending messages, emails, and making calls.")
        st.write("●  When you're feeling down, the system can play music to uplift your mood and brighten your day.")
        st.write("●   It assists in creating important notes, ensuring you don't miss any crucial information. The system can communicate on your behalf, handling tasks that traditional laptop assistants may be restricted from performing.")
        st.write("●   Unlike standard laptop assistants, our project breaks barriers, allowing your computer to perform a wide range of personalized and tailored tasks for your convenience.")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(" check out my work [ Smart virtual Assistant](https://github.com/akashsharma-2002/JARVIS/blob/main/JARVIS_OP)")
        st.write('\n')
        st.write('\n')
        st.write('---')
    with col2:
        st.write('\n')
        st.write('\n')
        st_lottie('https://lottie.host/63b2ce62-2480-472d-9ffe-2c22579a8fce/saZlfxuJ3T.json',width=340)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('---')

    #PROJECT 4

    with col1:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.subheader("Movie Recommendation System")
        st.write("● This project is designed to provide personalized movie recommendations based on user preferences.")
        st.write("● The intuitive Graphical User Interface (GUI) ensures a seamless and enjoyable movie selection experience.The model analyzes user behavior and preferences to suggest movies tailored to individual tastes.")
        st.write("●  It offers a wide range of movie genres, ensuring recommendations for every user's unique interests. With our movie recommendation model and user-friendly GUI, users can easily discover new and exciting films they might have otherwise missed.")
        st.write("●   By eliminating the hassle of manually searching for movies, our model streamlines the movie selection process, saving time and enhancing user satisfaction.")
        st.write('\n')
        st.write('\n')
        st.write('\n')


        st.write("check out my work [ Movie recommendation](https://github.com/akashsharma-2002/movie-recommendation)")
        st.write('\n')
        st.write('\n')
        st.write('---')
    with col2:
        st_lottie('https://lottie.host/5e23b449-472c-4d58-be16-f279b20f99ab/QEZ9LMR0Wc.json',width=340)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('---')

    #PROJECT 5

    with col1:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.subheader('NLP text classification on news analysis')
        st.write('This Python script performs text classification on a dataset of news articles.')
        st.write('The script leverages transformer-based models like BERT for accurate and efficient article classification.The script reads the dataset from the CSV file, where each row represents a news article.')
        st.write('The text data undergoes preprocessing to ensure optimal model training and performance. The script trains the transformer-based model for classification and evaluates its accuracy and performance on the dataset')
        st.write('With This NLP-based approach, news articles are efficiently categorized into predefined classes, enabling effective information organization and analysis.')
        st.write('\n')
        st.write('\n')
        st.write('\n')


        st.write('check out my work [ Text classification on news](https://github.com/akashsharma-2002/NLP-text-classification-on-news-analysis)')
        st.write('\n')
        st.write('\n')
        st.write('---')
    with col2:
        st_lottie('https://lottie.host/6620d429-c366-45ee-bc7d-73667bd3ff27/tKuxQDWiK3.json',width=340)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')
elif selected=="Certificate":
    st.write('\n')
    st.write('\n')
    st.title("Certification and Achievement")
    st.write('---')
    col1,col2=st.columns(2,gap='large')
    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("1: Python certification")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('I successfully completed the Python course conducted by HackerRank. Upon passing the Python test, I earned a certificate to validate my proficiency in Python programming. This certificate serves as a recognition of my skills and knowledge in Python, enhancing my credibility as a Python developer.')
        st.write('\n')
        st.write('\n')
        st.write('Certificate  [ Python ](https://www.hackerrank.com/certificates/f354be9a3b16)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')


        st.write('DEC 2022')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('---')

    #CERIFCATE 2

    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("2: Application of shockwave in science and medicine")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('I have accomplished the "Application of Shockwave in Science and Medicine" course conducted by CDSIMER. My successful completion has earned me a certificate, validating my expertise in utilizing shockwave technology for scientific and medical applications. This certification recognizes my proficiency in this specialized field, boosting my credentials in the domain.')
        st.write('\n')
        st.write('\n')
        st.write('Certificate  [ Shockwave ](https://drive.google.com/file/d/13dVScg3uPmPZvije3RWAGGcakSIEyZFi/view?usp=sharing)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')


        st.write('MAR 2023')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')

    #CERTIFICATE 3

    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("3: NLP-Spur")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(
            'I have successfully completed the "NLP Spur" course conducted by Dayananda Sagar University. Upon completion, I received a certificate recognizing my proficiency in Natural Language Processing (NLP). This certificate validates my skills in utilizing NLP techniques and technologies, enhancing my credentials in this field.')

        st.write('\n')
        st.write('\n')
        st.write(
            'Certificate  [ nlp spur ](https://drive.google.com/file/d/1ruIz24zek4UjsKtcJdifRbS_P5rkCBCF/view?usp=sharing)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('APR 2023')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')

    #CERTIFICATE 4

    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("4: ChatGBT")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(
            'I have successfully completed the "ChatGBT" course conducted by Dayananda Sagar University. As a result, I received a certificate acknowledging my proficiency in utilizing ChatGBT technology. This certification validates my expertise in this innovative chatbot framework, enhancing my skills in the field of conversational AI.')

        st.write('\n')
        st.write('\n')
        st.write(
            'Certificate  [ chatgbt ](https://drive.google.com/file/d/1-IonrNJCEZe8-5zEsV7nYhicvbxHLtpG/view?usp=sharing)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('FEB 2023')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')

    #CERTIFCATE 5

    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("5: Mobile App Development")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(
            'I have successfully completed the "Mobile App Development" course conducted by GSSS. As a testament to my proficiency in mobile app development, I received a certificate. This recognition validates my skills in creating innovative and functional mobile applications, enhancing my credibility as a mobile app developer.')

        st.write('\n')
        st.write('\n')
        st.write(
            'Certificate  [ Mobile app  ](https://drive.google.com/file/d/1f6HMJhPWhNtfvuhPFzk-CJJOxaTjCvJ-/view?usp=sharing)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('FEB 2021')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')

    #CERTIFCATE 6


    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("6: FULL STACK DEVELOPMENT")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(
            'I have successfully completed the "Full Stack Development" course conducted by Dayananda Sagar University. As a result of my successful completion, I have received a certificate that acknowledges my proficiency in full-stack development. This certification validates my skills in both front-end and back-end development, enhancing my career prospects in the field of web development.')

        st.write('\n')
        st.write('\n')
        st.write(
            'Certificate  [ FULL STACK  ](https://drive.google.com/file/d/1AB3ksMhoOWAgcjmIIyjPzkBNAnRVfy-7/view?usp=sharing)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('MAY 2021')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')

    #CERTIFCATE 7


    with col1:
        st.write('\n')
        st.write('\n')
        st.subheader("7: CACHE ME IF YOU CAN")
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write(
            'I achieved the 4th rank in the "Cache Me If You Can" competition conducted by Coding Ninjas at DSU College. This remarkable accomplishment showcases my strong problem-solving and coding skills. It highlights my ability to excel in competitive coding challenges, furthering my reputation as a skilled coder in the college community.')

        st.write('\n')
        st.write('\n')
        st.write(
            'Certificate  [ CACHE ME IF YOU CAN ](https://drive.google.com/file/d/1SAWJhyX5PVoqPw-O8kHJzz45sywe-hjP/view?usp=sharing)')
        st.write('\n')
        st.write('\n')
        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.subheader('Date of completion')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('OCT 2021')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')

elif selected=="Education":
    st.write('\n')
    st.write('\n')
    st.title("Education")
    st.write('---')
    col1,col2,col3=st.columns(3,gap="large")
    with col1:
        st.write('\n')
        st.write('\n')
        st.header("Dayanada Sagar University")
        st.write('\n')
        st.write('\n')
        st.write('Bachelor of Technology (B.Tech)')
        st.write('AI- 88% , python - 92%, Pattern Recognition- 86%, Machine learning 92%')
        st.write('\n')
        st.write('\n')

        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('DEC 2020 - AUG 2024')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')
    with col3:
        dssu=Image.open(dssu)
        st.write('\n')
        st.write('\n')
        st.image(dssu,width=230)

    #kv 12th

    with col1:
        st.write('\n')
        st.write('\n')
        st.header("KENDRIYA VIDYALAYA ISLAND GROUNDS CHENNAI(CBSE board)")
        st.write('\n')
        st.write('\n')
        st.write(' Senior Secondary (XII), Science')
        st.write('python- 88%, English- 89%, Maths- 82%')
        st.write('\n')
        st.write('\n')

        st.write('---')

    with col2:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('DEC 2018 - JUN 2020')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        st.write('---')
    with col3:
        kvs=Image.open(kvs)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.image(kvs,width=250)







