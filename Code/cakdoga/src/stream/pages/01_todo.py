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

- Code:
   - [ ] 2025.03.15
- Documentation: 
   - [ ] 2025.04.15
- My Deadline: 
   - [ ] 025.04.25
- Final! deadline: 
   - [ ] 2025.05.18

'''


code_text = f'''
### Code:

- [ ] TMP
- [ ] CONFIG fix

'''

document_text = f'''
### Documentation:

- [ ] TMP

'''

with st.container(border=True):
    st.markdown(deadline_text)

with st.container(border=True):
    st.markdown(code_text)
    
with st.container(border=True):
    st.markdown(document_text)