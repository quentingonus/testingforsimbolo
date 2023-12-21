import requests
import streamlit as st

def get_mmk_rate():
  url = "http://forex.cbm.gov.mm/api/latest"
  res = requests.get(url).json()
  rate = res.get('rates', {})
  return f"current USD/MMK rate from Central Bank is {rate.get('USD')}"

user_btn = st.button("Get MMK Rate", type="primary")

if user_btn:
  st.write("Getting MMK_USD rates")
  st.write(get_mmk_rate())
