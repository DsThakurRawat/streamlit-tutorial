import streamlit as st

x = 10
y = 20

x + y  # This is a magic command — Streamlit will display 30 automatically

"Hello, Streamlit!"  # This string will be displayed as well
"""
In Streamlit, the term "magic command" usually refers to a special syntax that allows you to write expressions or small snippets of code directly in the script and Streamlit automatically renders the output without needing explicit st.write() or other display functions.

What is a Magic Command in Streamlit?
It's a shorthand way to display variables or expressions.

You simply write a Python expression on a line by itself, and Streamlit automatically calls st.write() on it.

Useful for quick prototyping or displaying results inline without extra code.


#How is it different from normal code?
  Normally in Streamlit, you'd write:
    st.write(x + y)
    st.write("Hello, Streamlit!")
## But with magic commands, you can just write:
x + y  # This will display 30 automatically

"""
""""
Important Notes:
Magic commands only work with expressions or values that have a meaningful display.

If you put a statement like a loop or an assignment (x = 10), it won't output anything.

It is convenient for quick demos but using explicit st.write(), st.text(), or other widgets is better for clarity in bigger apps.


"""
"""

How Magic works
Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using st.write (which you'll learn about later).

Also, magic is smart enough to ignore docstrings. That is, it ignores the strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn magic off in your ~/.streamlit/config.toml with the following setting:
[runner]
magicEnabled = false
"""
