import gc
from io import BytesIO

import numpy as np
import torch
from PIL import Image

import utils
from utils import inputs
import streamlit as st
import os
import requests # request img from web
import shutil # save img locally
from utils import load_gan
import logging
os.environ["REPLICATE_API_TOKEN"] = "81f2e4dc54d050256a9aa63fc1ad0679aa35a287"


def main() :
    logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

    model,version = load_gan()
    with torch.no_grad():
        torch.cuda.empty_cache()
    ##########################"
    st.set_page_config(page_title="Anime_Gan", page_icon="🤖")
    utils.initialize_template()
    st.write(
        """<style>
        [data-testid="column"] {
            width: calc(50% - 1rem);
            flex: 1 1 calc(50% - 1rem);
            min-width: calc(50% - 1rem);
        }
        </style>""",
        unsafe_allow_html=True,
    )
    #############################
    st.title("Anime Generation")

    inputs = utils.inputs
    # print(inputs)

    col1,col2 = st.columns(2)
    with col1 :
        pass
    image_spin_holder = st.empty()

    if st.button(label="Feeling Lucky",
                    type="secondary"):
        with image_spin_holder:
            with st.spinner("Please wait while your image is being generated..."):
                with col2:

                    output = utils.generate_text_lucky(version, inputs, st.empty())
                    img = utils.add_images(output)
        utils.share_button(output)


    # inputs['prompt'] = st.text_input('Enter Text',placeholder="write a description")

    col1, col2 = st.columns(2)

    #

    inputs['prompt'] = st.text_input('Enter Text', placeholder="write a description")

    if st.button(label="Generate text",
                    type="secondary"):
        with image_spin_holder:
            with st.spinner("Please wait while your image is being generated..."):
                with col2:
                    output = utils.generate_img(version, inputs, image_spin_holder)
                    img = utils.add_images(output)

        utils.share_button(output)

    with col1:
        pass

    import base64

    gc.collect()
    # if st.button('Download'):
    #     # st.markdown("<a href=" + output[0] + " download>Download Image</a>", unsafe_allow_html=True)
    #     st.markdown('<a href="' + base64(output) + '" download>Download Image</a>', unsafe_allow_html=True)
    #     # st.markdown("<a href=" + image_url + " download>Download Image</a>", unsafe_allow_html=True)
    #
    #     # # Add a share button
    #     # if st.button("Share on Twitter"):
    #     #     st.text("Share this on Twitter")
    #     #     st.text("https://twitter.com/intent/tweet?text=" + prompt)
    #     # if st.button("Share"):
    #     #     if st.button("Share"):

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


















































#
#
#
# layout_streamlit()
# prompt = st.text_input('Enter Text')
#
# from utils import load_gan
# model,version = load_gan()
# # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
# inputs = inputs
# print(inputs["prompt"])
# print(inputs)
# # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
#
# output = version.predict(**inputs)
#
# print(len(output))
# print(output)
#
# ## image saving :
# res = requests.get(output[0])
# img_data = res.content
# st.image(img_data, caption='Image from link', use_column_width=True)
#
# # if res.status_code == 200:
# #     file_name = "zabba.jpg"
# #     with open(file_name, 'wb') as f:
# #         shutil.copyfileobj(res.content, f)
# #     print('Image sucessfully Downloaded: ', file_name)
# # else:
# #     print('Image Couldn\'t be retrieved')
