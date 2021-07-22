# Run by typing python3 main.py

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""

# import basics
import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# import stuff for our models
import torch
from aitextgen import aitextgen
import regex as re
import apiUploader
'''
Coding center code - comment out the following 4 lines of code when ready for production
'''

trump = aitextgen(model_folder="Trained_models/trump_model", to_gpu=False) # TRUMP MODEL
biden = aitextgen(model_folder="Trained_models/biden_trained_model", to_gpu=False)
grassley = aitextgen(model_folder="Trained_models/grassley_model", to_gpu=False)
oprah = aitextgen(model_folder="Trained_models/oprah_model", to_gpu=False)
jackie = aitextgen(model_folder="Trained_models/Jackie_model", to_gpu=False)
elon = aitextgen(model_folder="Trained_models/elon_4k_model", to_gpu=False)
nasa = aitextgen(model_folder="Trained_models/nasa_model", to_gpu=False)
moonpie = aitextgen(model_folder="Trained_models/moonpie_model", to_gpu=False)

    
promptOptions = {"elonmusk": elon,
                 "realdonaldtrump": trump,
                 "JoeBiden/POTUS": biden,
                 "MoonPie": moonpie,
                 "ChuckGrassley": grassley,
                 "EyeOfJackieChan": jackie,
                 "Oprah": oprah,
                 "NASA": nasa}

tempList = {'elonmusk': 0.65,
            'realdonaldtrump': 0.7,
            'JoeBiden/POTUS': 0.7,
            'MoonPie': 0.6,
            'ChuckGrassley': 0.75,
            'EyeOfJackieChan': 0.8,
            'Oprah': 0.8,
            'NASA': 0.7}

top_pList = {'elonmusk': 0.95,
             'realdonaldtrump': 0.96,
             'JoeBiden/POTUS': 0.9,
             'MoonPie': 0.95,
             'ChuckGrassley': 0.95,
             'EyeOfJackieChan': 0.95,
             'Oprah': 0.95,
             'NASA': 0.95}

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
#port = 34215 # random port num
#base_url = get_base_url(port)
#app = Flask(__name__, static_url_path=base_url+'static')

'''
Deployment code - uncomment the following line of code when ready for production
'''
app = Flask(__name__)

@app.route('/')
#@app.route(base_url)
def home():
    return render_template('Home.html', generated=None)

@app.route('/', methods=['POST'])
#@app.route(base_url, methods=['POST'])
def home_post():
    return redirect(url_for('results'))

@app.route('/team')
#@app.route(base_url + '/team')
def team():
    return render_template('Team.html', generated=None)

@app.route('/results')
#@app.route(base_url + '/results')
def results():
    return render_template('Tweet-Generator.html', generated=None)

@app.route('/generate_text', methods=["POST"])
#@app.route(base_url + '/generate_text', methods=["POST"])
def generate_text():
    """
    view function that will return json response for generated text. 
    """

    prompt = request.form['prompt']
    persona = request.form['accounts']
    ai = promptOptions[persona]
    temp = tempList[persona]
    topP = top_pList[persona]
    if prompt is not None:
        generated = ai.generate(
            n=1,
            batch_size=3,
            prompt=str(prompt),
            max_length=50,
            temperature=temp,
            top_p=topP,
            return_as_list=True
        )
        generated = re.sub('amp;','&', generated[0])
        sep = '\n\n'
        generated = generated.split(sep, 1)[0]

        generated = [generated]
    tweet = generated[0]
    apiUploader.uploadTweet(persona, tweet, prompt)

    data = {'generated_ls': generated}
    return jsonify(data)

if __name__ == "__main__":
    '''
    coding center code
    '''
    # IMPORTANT: change the cocalcx.ai-camp.org to the site where you are editing this file.
    website_url = 'cocalc1.ai-camp.org'
    print(f"Try to open\n\n    https://{website_url}" + base_url + '\n\n')

    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)

    '''
    scaffold code
    '''
  