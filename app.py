#!/usr/bin/env python
# coding: utf-8
# %%

# %%
from flask import Flask,render_template,request

from audiocraft.models import musicgen
# from audiocraft.data.audio import audio_write
import os

model = musicgen.MusicGen.get_pretrained("small", device='cpu')

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/result_melody",methods=["GET","POST"])
def result_melody():
    prompt_text = request.form.get("q") 
    from gradio_client import Client

    client = Client("https://facebook-musicgen.hf.space/")
    result = client.predict(prompt_text, None, fn_index=0)
    print(result)
    return(render_template("result_melody.html",r=result[0]))

@app.route("/end",methods=["GET","POST"])
def end():
    print("end")
    return(render_template("end.html"))

if __name__ == "__main__":
    app.run()


# %%
