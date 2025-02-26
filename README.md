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

--- 

# steps to use the web 

1. **Open the Web App:** After running the command, Streamlit will automatically open the app in your default web browser. If it doesn't, you can access it by navigating to http://localhost:8501.

2. **Upload an Image:**
- Select whether to upload an image file from your computer or provide a URL for an image.
- For "Upload File", use the file uploader to select an image from your local system.
- For "Enter Image URL", paste the URL of the image you want to use.

3. **Edit the Image:**
- Use the options on the sidebar to:
   - Resize the image by adjusting the width and height.
   - Rotate the image by selecting the desired degrees.
   - Apply a filter (Blur, Detail, Emboss, or Smooth).

4. **Apply Changes:** Click the "Apply Changes" button to apply the selected adjustments to the image.

5. **Download the Edited Image:** After the changes are applied, a preview of the edited image will appear. You can download the edited image by clicking the "Download Edited Image" button.

---
# output images

![Uplode Image](screenshot/Screenshot%20(1).png)
![Edit Image](screenshot/Screenshot%20(2).png)
![Apply Changes(Download Image)](screenshot/Screenshot%20(3).png)
