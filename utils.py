import streamlit as st
import pandas as pd


def wgt_st_input(wgt_type:str, keyval:str, name:str, minval:int, maxval:int, initval:int, stepval:int, lblvis:str, disval:bool):
    if wgt_type == "Number Input":
        wgt = st.number_input(
            name,
            min_value=minval,
            max_value=maxval,
            value=initval,
            step=stepval,
            key=f"{keyval}_{name}",
            label_visibility=lblvis,
            disabled=disval)
    elif wgt_type == "Slider":
        wgt = st.slider(
            name,
            min_value=minval,
            max_value=maxval,
            value=initval,
            step=stepval,
            key=f"{keyval}_{name}",
            label_visibility=lblvis,
            disabled=disval)
    else:
        wgt = None
    return wgt