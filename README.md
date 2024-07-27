# Image-Enhancement

Command prompt: If you want to run in Cmd of your pc (system must contain Nvidia graphic card)

# Installation:
Simply run the command pip install -r requirements.txt to install the dependencies in cmd.
# Usage:
1)	Clone this repository and install the dependencies as mentioned above.
2)	Make a directory within this cloned repository with the name .streamlit (Don't forget the dot !!).
3)	Create a file config.toml in this directory.
4)	Copy-Paste the following contents in this file and save :
     [theme]
  	
     primaryColor="#b11b1b"

  	backgroundColor="#080e1c"

  	secondaryBackgroundColor="#203659"

  	textColor="#bf7c7c"

6)	Open the command prompt.
7)	Navigate to the root directory of this repository and simply run the command:
streamlit run app.py
(or)
By default, streamlit allows us to upload files of max. 200MB. If you want to have more size for uploading files, execute the command :
streamlit run app.py --server.maxUploadSize=1028

8)	Navigate to http://localhost:8501 in your web-browser.



# Google Colab : 
Use google colab if your system doesn’t contain graphic card or don’t want to stress your system.
# Usage:
1)	Upload the repository into your drive.
2)	Simply open and run the .ipynb file already present in the repository.
              (or)
3)	Open the new collab notebook.
4)	Change directory to the root directory of repository
5)	Simply run this commands:

! pip install streamlit -q

!wget -q -O - ipv4.icanhazip.com 

The above command gives IP address as a output which is password for your streamlit app.

! streamlit run app.py --client.showErrorDetails=false & npx localtunnel --port 8501

This command gives url like (https://full-jobs-hope.loca.lt) as output open the link.

7)	Use the password from previous command and open.
8)	Streamlit app is opened.


# In case of Training:
Download the data set like Div2k which consists of Low resolution and High resolution folders with their respective image.
Due to the large size of the data set. It is not included in this storage.

# The project code is in master branch.
