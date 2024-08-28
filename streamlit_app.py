import streamlit as st

st.set_page_config(page_title="Streamlit Cheat Sheet",
                   page_icon=":brain:", 
                   layout="wide")

st.header(":rainbow: Streamlit Cheat Sheet")
st.caption("This cheat sheet provides a quick reference to the most common Streamlit functions.")
st.write("Collated by Mr Matheson, with the help of the Streamlit documentation and a tiny bit of Github Copilot.")
tab1, tab2 = st.tabs(["Outputs","Inputs"])


with tab1:
    st.header("Outputs")
    # WRITING
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
            
    # HEADINGS AND OTHER TEXT TYPES
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
            
            
    # IMAGES AND MEDIA
    st.subheader("Images and Media")
    media_expand = st.expander("See st.image(), st.audio(), st.video() Examples")
    with media_expand:
        st.write("Each code snippet below shows the corresponding output underneath.")
        with st.echo():
            st.write("Image from the web")
            st.image("https://static.streamlit.io/examples/cat.jpg", caption="A cat")
            st.write("Image from the local file system")
            st.image("./images/dog.jpg", caption="A dog")
            st.write("Image from the web with custom width")
            st.image("https://static.streamlit.io/examples/cat.jpg", width=100, caption="A cat")
            
        st.divider()
        with st.echo():
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
        st.divider()
        with st.echo():
            st.video("https://www.youtube.com/watch?v=9Q8PwcDzb8M")
        st.divider()
        
    # DATAFRAMES AND TABLES
    st.subheader("DataFrames and Tables")
    table_expand = st.expander("See st.dataframe() and st.data_editor( Examples") 
    with table_expand:
        st.write("Each code snippet below shows the corresponding output underneath.")
        with st.echo():
            import pandas as pd
            st.write("Shane Edwards Career Stats - from AFLTables.com")
            df = pd.read_excel("ShaneEdwards.xlsx")
            st.dataframe(df)
            st.write("Highlight the maximum value in each column (use axis=1 for rows)")
            st.dataframe(df.style.highlight_max(axis=0))   
            
        st.divider()
        with st.echo():
            st.write("Editable DataFrame (Changes the stored data)")
            st.data_editor(df, key="editable_df")
            
        st.divider()
        
    # GRAPHS 
    st.subheader("Graphs")
    graph_expand = st.expander("See st.line_chart(), st.bar_chart(), st.area_chart and st.scatter_chart Examples")
    with graph_expand:
        st.write("Each code snippet below shows the corresponding output underneath.")
        st.subheader("Loading data from spreadsheet")
        st.write("""Before creating the graph we always need to load the data we will graph. 
                 In this case, we will load the data from the spreadsheet 'ShaneEdwards.xlsx'
                 which has statistics taken from AFLTables.com and put into a spreadsheet.""")
        with st.echo():
            import pandas as pd
            df = pd.read_excel("ShaneEdwards.xlsx")
            
        st.divider()
        with st.echo():
            st.write("Line Chart")
            st.line_chart(df, x="Year", y=["Kicks", "Handballs"])
        st.divider()
        with st.echo():
            st.write("Bar Chart")
            st.bar_chart(df, x="Year", y="Goals")
            st.write("Bar Chart Comparing Two Columns")
            st.bar_chart(df, x="Year", y=["Frees For", "Frees Against"], stack=False)
        st.divider()
        with st.echo():
            st.write("Scatter Chart")
            st.scatter_chart(df, x="Games", y="Disposals")
        
        st.divider()
        with st.echo():
            st.write("Area Charts")
            st.area_chart(df, x="Year", y="Tackles")
        st.divider()
    
with tab2:
    st.header("Inputs")
    # BUTTONS AND BASIC INPUTS
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

    # CHECKBOXES AND RADIO BUTTONS        
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

    # SELECT BOXES AND MULTI-SELECT        
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
            
    # DATE AND TIME INPUTS
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

    # SLIDERS AND PROGRESS BARS
    st.subheader("Sliders and Progress Bars")
    slider_expand = st.expander("See st.slider(), st.progress() Examples")
    with slider_expand:
        st.write("Each code snippet below shows the corresponding output underneath.")
        with st.echo():
            slider_input = st.slider("Slide me", min_value=0.0, max_value=100.0, value=50.0, step=5.0)
            st.write(f"You chose: {slider_input}")
            slider2_input = st.slider("Slide me too!", min_value=0, max_value=200, value=(50, 150), step=1)
            st.write("You chose: ", slider2_input)
        st.divider()
        
    # Working with DataFrames
    st.subheader("Working with DataFrames")
    dataframes_expand = st.expander("See examples on filtering and modifying DataFrames")
    with dataframes_expand:
        st.write("Each code snippet below shows the corresponding output underneath.")
        st.write("Loading the DataFrame from a spreadsheet")
        with st.echo():
            import pandas as pd
            df = pd.read_excel("ShaneEdwards.xlsx")
            st.write(df)
        
        st.divider()
        with st.echo():
            st.write("Filtering DataFrames")
            st.write("Filtering by column value (Year is 2017)")
            df_2017 = df[df["Year"] == 2017]
            st.write(df_2017)
            st.write("Filtering by multiple column values (More than 10 goals and More than 18 games)")
            df[(df["Goals"] > 10) & (df["Games"] > 18)]
            st.write()
        st.divider()
        with st.echo():
            st.write("Modifying DataFrames")
            st.write("Adding a new column - Disposals Per Game")
            df["Disposals Per Game"] = df["Disposals"] / df["Games"]
            st.write(df)
            st.write("Dropping a column (remove disposals per game)")
            df.drop(columns="Disposals Per Game", inplace=True)
            st.write(df)
        st.divider()
