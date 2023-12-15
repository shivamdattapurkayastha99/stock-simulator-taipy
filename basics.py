import taipy as tp
import pandas as pd 
data = {
    "Date": pd.date_range("2023-01-01", periods=4, freq="D"),
    
    "Min": [222,419.7,662.7,323.5],
    "Max": [28.6,68.2,666.5,173.5]
}
title="Stock Stimulator by shivam"
path="logo2.png"
company_name="tata"
company_minp=10
company_maxp=100

def shivam(state):
    print("hello shivam")
    print(state.path)
    print(state.company_minp)
    with open("data.txt","w") as f:
        f.write(f"{state.company_name},{state.company_minp},{state.company_maxp}")


page="""

<|text-center|

<|{path}|image|>

<|{title}|hover_text="Welcome to stock screener"|>

Name of Stock:<|{company_name}|input|>

Min price:<|{company_minp}|input|>

Max price:<|{company_maxp}|input|>

<|Run simulation|button|on_action=shivam|>

<|{title}|hover_text="Your Simulation"|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>

>


"""


if __name__ == "__main__":
    
    tp.Gui(page).run(use_reloader=True)
