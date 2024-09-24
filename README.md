# image_editor
This is my first Git Repository
<br>
it is a image editor done using streamlit in python


#### what is the project about?
 **A basic image editor using Streamlit and Pillow!**
 


#### 1.Setting Up Your Environment:
- Create a Python file named **image_editor.py** in vscode
#### How to clone  Git Repository
 - Open your project git repository  (https://github.com/kiranraj557/image_editor/tree/main)
 - Click on code and copy the Project URL
 - Open new window in VS Code
 - Click the Clone git repository
 - Paste the URL on repository source and press enter
 - Navigate to the folder path and click on select as repository destination
 - Open the clone repository in vs code

 #### How to Create Virtual Environment
 - Open terminal and run below commands
    - python -m venv .venv 
    - .venv\Scripts\activate  
    - pip install streamlit 
    - pip list
    - streamlit run image_editor.py
    - git pull
    - git checkout -b "update_readme"
    - git status

#### How to install required libraries

Install the library,if it's not already installed using:(enter these in vscode terminal)
 - pip install streamlit
 - pip install pillow


#### How to run
- To run the code enter **streamlit run image_editor.py** in the terminal
- This will display the web app on your screen 


# code explanation

#### 2.Importing Libraries:
```python
import streamlit as st 
from PIL import Image
from PIL.ImageFilter import *
```

#### 3.Creating the Streamlit App:
Set up the title of your application:
```python
st.markdown("<h1 style='text-align: center;'>Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---") # Horizontal line
```

#### 4.File Uploader:
Add a file uploader to allow users to upload images:
```python
image=st.file_uploader("upload Image",type=["jpg","png","jpeg"])
```

#### 5.Displaying Image Properties:
Create placeholders for image properties (mode, size, format):
```python
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()
```

#### 6.Processing the Uploaded Image:
Open the uploaded image using Pillow:
```python
if image:
    img = Image.open(image) # Display the image
    info.markdown("<h2 style='text-align:left;'>Information</h2>",unsafe_allow_html=True)
    size.markdown(f"<h6>size: {img.size} </h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>mode: {img.mode} </h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>format: {img.format} </h6>",unsafe_allow_html=True)
```

#### 7.Adding Resizing Functionality:
Created a heading for resizing:
```python
st.markdown("<h2 style='text-align:left;'>Resizing</h2>",unsafe_allow_html=True)
    width=st.number_input("width",value=img.width)
    height=st.number_input("height",value=img.height)
```    

#### 8.Adding Rotation Functionality:
Introduced a heading for rotation and added a number input for the degree of rotation:
```python
    st.markdown("<h2 style='text-align:left;'>Rotation</h2>",unsafe_allow_html=True)
    degree=st.number_input("degree",)
```

#### 9.Adding Filters:
Created a section for filters using a select box with options like "None", "Blur", "Detail", "Emboss", and "Smooth":
```python
    st.markdown("<h2 style='text-align:left;'>Filters</h2>",unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None","Blur","Detail","Emboss","Smooth"))
```

#### 10.Submit Button:
Introduced a submit button to trigger image processing:
```python
    s_btn=st.button("submit")
```    

#### 11.Resizing and Rotating:
When the submit button is clicked, the application resizes and rotates the image based on user input:
```python
    if s_btn:
        edited=img.resize((width,height)).rotate(degree)
        filtered=edited
```        

#### 12.Applying Filters:
Checked the selected filter and applied it:
```python
        if filters != "None":
            if filters == "Blur":
                filtered=edited.filter(BLUR)
            elif filters == "Detail":
                filtered=edited.filter(DETAIL)
            elif filters == "Emboss":
                filtered=edited.filter(EMBOSS)
            else:
                filtered=edited.filter(SMOOTH)
```                  

#### 13.Displaying the Final Image:
Finally displayed the edited or filtered image using:
```python
        st.image(filtered)
```        


#### output
 To run the code enter **streamlit run image_editor.py** in the terminal
 this will display the web app on your screen 





