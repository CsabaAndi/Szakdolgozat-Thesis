import streamlit as st


st.set_page_config(
    page_title="Tables",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

container = st.container(border=True)
col = st.columns((1.5, 4.5, 2), gap='medium')


deadline_text = f'''
### Deadlines:

- Code Beta / Documentation outline:
   - [ ] 2025.04.03
- Close to Done state: 
   - [ ] 2025.04.27
- Done state: 
   - [ ] 025.05.07
- Modulo upload (final): 
   - [ ] 2025.05.24

'''


code_text = f'''
### Code:

- [ ] Clean & Fix
- [ ] Add Machine Learning part
- [ ] Add Search bar to specify team data for the other parts

'''

document_text = f'''
### Documentation:

- [ ] Placeholder

'''

with st.container(border=True):
    st.markdown(deadline_text)

with st.container(border=True):
    st.markdown(code_text)
    
with st.container(border=True):
    st.markdown(document_text)