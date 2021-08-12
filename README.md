# VCR
Virtual Chemical Reaction

Installation
Requirements
Python 3 needs to be installed. Install Python 3 with Anaconda

Once Python 3 is installed, Clone this repository and then create a conda environment

conda create -n vcr python=3.8
conda activate vcr
pip install transformers[tf-cpu]
pip install -r requirements.txt

How to run the project
Go to the project directory and make sure conda environment is active. If not then you can activate by running below command

conda activate vcr


Now start server by running

python app.py
Now the server will start. You can ctrl+click on the link in the terminal you can paste http://localhost:5000/ in your browser to launch the site.
