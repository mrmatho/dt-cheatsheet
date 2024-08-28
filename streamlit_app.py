import streamlit as st

st.set_page_config(page_title="Streamlit Cheat Sheet", page_icon=":brain:", layout="wide")

st.title("Streamlit Cheat Sheet")

st.subheader("Writing")
writing_expander = st.expander("See st.write() Examples")
with writing_expander:
    st.write("Each code snippet below shows the corresponding output underneath.")
    st.divider()
    with st.echo():
        st.write("Here's some text")
    st.divider()
    
    with st.echo():
        st.write("Some more *text* with different **emphases**")
        st.write("And even [links](https://www.streamlit.io)")
        st.write("Or perhaps some `code`")
    st.divider()
        
    st.write("You can also write raw HTML, like this:")
    with st.echo():
        st.write("<p style='color: blue;'>Hello, world!</p>", unsafe_allow_html=True)
st.subheader("Headings and other specific text types ")    
head_expand = st.expander("See st.title(), st.header(), st.subheader() Examples")   
with head_expand:
    st.write("Each code snippet below shows the corresponding output underneath.")
    with st.echo():
        st.title("This is a title")
        st.header("This is a header")
        st.subheader("This is a subheader")
    st.divider()
    st.write("You can use the equation language LaTeX to write mathematical equations.")
    with st.echo():
        st.latex(r"a + ar +\frac{1}{2+a} - a r^3 ")
        
st.subheader("Buttons and Basic Inputs")
input_expand = st.expander("See st.button(), st.text_input(), st.number_input() Examples")
with input_expand:
    st.write("Each code snippet below shows the corresponding output underneath.")
    with st.echo():
        if st.button("Click me!"):
            st.write("Button clicked!")
    st.divider()
    with st.echo():
        text_input = st.text_input("Enter some text")
        st.write(f"You entered: {text_input}")
    st.divider()
    with st.echo():
        number_input = st.number_input("Enter a number")
        st.write(f"You entered: {number_input}")
        second_number_input = st.number_input("Enter another number", min_value=0.0, max_value=100.0, value=50.0, step=5.0)
        st.write(f"You also entered: {second_number_input}")
        integer_number_input = st.number_input("Enter an integer", min_value=0, max_value=200, value=50, step=1)
        
st.subheader("Checkboxes and Radio Buttons")
checkbox_expand = st.expander("See st.checkbox(), st.radio() Examples")
with checkbox_expand:
    st.write("Each code snippet below shows the corresponding output underneath.")
    with st.echo():
        if st.checkbox("Check me out!"):
            st.write("Checkbox checked!")
    st.divider()
    with st.echo():
        radio_input = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
        st.write(f"You chose: {radio_input}")
        
st.subheader("Select Boxes and Multi-Select")
select_expand = st.expander("See st.selectbox(), st.multiselect() Examples")
with select_expand:
    st.write("Each code snippet below shows the corresponding output underneath.")
    with st.echo():
        select_input = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
        st.write(f"You chose: {select_input}")
    st.divider()
    with st.echo():
        multiselect_input = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
        st.write(f"You chose: {multiselect_input}")
st.subheader("Date and Time Inputs")
date_expand = st.expander("See st.date_input(), st.time_input(), st.date_time_input() Examples")
with date_expand:
    st.write("Each code snippet below shows the corresponding output underneath.")
    with st.echo():
        date_input = st.date_input("Pick a date")
        st.write(f"You chose: {date_input}")
    st.divider()
    with st.echo():
        time_input = st.time_input("Pick a time", value="now", step=60)
        st.write(f"You chose: {time_input}")
    st.divider()



st.subheader("Sliders and Progress Bars")
slider_expand = st.expander("See st.slider(), st.progress() Examples")
with slider_expand:
    st.write("Each code snippet below shows the corresponding output underneath.")
    with st.echo():
        slider_input = st.slider("Slide me", min_value=0.0, max_value=100.0, value=50.0, step=5.0)
        st.write(f"You chose: {slider_input}")
    st.divider()
    with st.echo():
        progress_input = st.progress(0)
        for percent_complete in range(101):
            progress_input.progress(percent_complete)
