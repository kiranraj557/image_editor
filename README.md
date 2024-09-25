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


## output
 To run the code enter **streamlit run image_editor.py** in the terminal
 this will display the web app on your screen 

 ![image editor file uplode screen](/screenshot/Screenshot%20(1).png)
*screen1:* **Click on Browse files to upload image**



  ![ uploded image info](/screenshot/Screenshot%20(2).png)
*screen2:* **Information about uploded image**



  ![resizing, rotation, ](/screenshot/Screenshot%20(3).png)
*screen3:* **Adjust the value according to your choice to resize and rotate uploded image**



  ![select filters](/screenshot/Screenshot%20(4).png)
*screen4:* **To apply filter select any one of the options present or select None**

**click on submit button to see the edited image**

 

# Creating a Branch
A branch in GitHub is essentially a copy of your project's code<br> where you can make changes without affecting the main (or primary) codebase.
#### Steps to Create a Branch:
##### 1. Clone the repository:
    we had one commond to Clone
###### "git clone https://github.com/kiranraj557/image_editor.git"
##### 2. Create a new branch:
      we also have command to create branch
        "git checkout -b "requriments"
       This command creates new branch <br> and Switched to a new branch 'requriments'
##### 3. push the branch to git hub
       git push origin requriments
  This sends our newly created branch "requiremnts" to GitHub.

  
## Purpose of Creating a Branch:
 + ###### Isolated Development:
         can work on a new feature or bug fix without affecting the main codebase (usually the main or master branch).
 + ###### Collaboration: 
        Team members can work on different features or fixes in parallel without interfering with each other's work.
 + ###### Testing: 
         You can experiment with new ideas or test code without breaking the main project.
 + ###### Pull Requests:
         After completing work on a branch, you can create a pull request to merge the changes into the main branch.
         This allows other team members to review the code before it's merged.

   
# Creating a Pull Request (PR) in GitHub
#### Steps to Create a Pull Request:
##### 1. Go to your GitHub repository
        Visit the repository in your browser.
##### 2.Navigate to the "Pull Requests" tab
         At the top of the repository page, click on the "Pull requests" tab.
##### 3.Click on "New Pull Request" 
         On the right-hand side, you’ll see a green button labeled "New Pull Request."
##### 4.Write a meaningful Pull Request title and description
          Title: A brief description of what the PR is about.
          Description: Provide a more detailed explanation of the changes you made, why they were necessary, and any additional context.
##### 5. Create the Pull Request  
           Once everything is filled out, click the green "Create Pull Request" button.
##### 6. Review and Approval 
            After creating the PR, team members can review your changes, add comments, and request modifications if needed.
            Once approved, the changes can be merged into the main branch
    After  creation of pull request we have to merge pull request

    
# Merging a Pull Request (PR) in GitHub
         Once your Pull Request (PR) is created and reviewed, the final step is to merge it into the main branch
#### Steps to Merge a PR:
##### 1.Review the PR
        Ensure that the code has been reviewed and approved by team members.
        Address any comments or requested changes from reviewers.
##### 2.Click the "Merge Pull Request" button 
        Once the PR is approved, and there are no conflicts
        you’ll see a green "Merge Pull Request" button at the bottom of the PR.
        Click on it.
##### 3.Confirm the Merge  
        After clicking "Merge Pull Request", confirm the action by clicking the "Confirm Merge" button.
##### 4.Delete the branch 
        After merging, you’ll get an option to delete the branch. Deleting the branch is optional
        but recommended if the feature or bug fix is complete, to keep the repository clean.

         
   





