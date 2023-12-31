
from st_on_hover_tabs import on_hover_tabs
import streamlit as st


def main():
    st.set_page_config(layout="wide")

    st.header("Garlic News Network 🧄")
    st.markdown('<style>' + open('./css/style.css').read() + '</style>', unsafe_allow_html=True)

    with st.sidebar:
        tabs = on_hover_tabs(tabName=['Home', 'Money', 'Economy'],
                             iconName=['home', 'money', 'economy'],
                             styles={'navtab': {'background-color': '#111',
                                                'color': '#818181',
                                                'font-size': '18px',
                                                'transition': '.3s',
                                                'white-space': 'nowrap',
                                                'text-transform': 'uppercase'},
                                     'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                           'cursor': 'pointer'}},
                                     'iconStyle': {'position': 'fixed',
                                                   'left': '7.5px',
                                                   'text-align': 'left'},
                                     'tabStyle': {'list-style-type': 'none',
                                                  'margin-bottom': '30px',
                                                  'padding-left': '30px'}},
                             key="1", default_choice=0)

    if tabs == 'Home':
        st.title("Navigation Bar")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Money':
        st.title("Paper")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Economy':
        st.title("Tom")
        st.write('Name of option is {}'.format(tabs))


if __name__ == '__main__':
    main()
