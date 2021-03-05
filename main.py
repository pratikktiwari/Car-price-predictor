import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tkinter import *
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import car_names as cn
#open file for reading
data_url = ('cars_data.csv')
df = pd.read_csv(data_url)

#check whether data is loaded from csv or not
print(df.head())
# data = df 

# data = data[data.price != '?']
df['highway-mpg'].fillna((df['highway-mpg'].mean()), inplace=True)
# df['make']

def predict_based_on_user_input():
    cdf = df[['price','highway-mpg']]
    regr = LinearRegression()
    data_x = np.asanyarray(cdf[['highway-mpg']])
    data_y  = np.asanyarray(cdf[['price']])
    regr.fit(data_x, data_y)
    print('Coefficients: ', regr.coef_)
    print('Intercept   : ', regr.intercept_)

    #val_e1 = E1.get()
    val_e1 = e1_text_var.get()
    val_e1 = int(val_e1)
    predict_val_highway_mpg_price = regr.intercept_[0] + regr.coef_[0][0]*val_e1

    # =============================================================================
    cdf = df[['make','price']]
    label_encoder = LabelEncoder() 
    cdf['make'] = label_encoder.fit_transform(cdf['make'])
    # cdf.loc[:, ['make']]= label_encoder.fit_transform(cdf['make'])
    print(cdf.head(5))
    input_make = e2_text_var.get().lower()
    if input_make in cn.car_names_l:
        input_make = cn.car_names_l.index(input_make)
    # input_make = 1
    price=0
    make_list = cdf['make'].tolist()
    price_list = cdf['price'].tolist()
    count=0
    for i in range(len(make_list)):
        if make_list[i] == input_make:
            count=count+1
            price+=  price_list[i]
    avg_price_make = price/(count)
    # ============================================================================
    cdf = df[['price','num-of-doors']]
    regr = LinearRegression()
    data_x = np.asanyarray(cdf[['num-of-doors']])
    data_y  = np.asanyarray(cdf[['price']])
    regr.fit(data_x, data_y)
    print('Coefficients: ', regr.coef_)
    print('Intercept   : ', regr.intercept_)

    #val_e1 = E1.get()
    val_e1 = e3_text_var.get()
    val_e1 = int(val_e1)
    predict_val_highway_doors_price = regr.intercept_[0] + regr.coef_[0][0]*val_e1

    # ============================================================================
    cdf = df[['price','num-of-cylinders']]
    regr = LinearRegression()
    data_x = np.asanyarray(cdf[['num-of-cylinders']])
    data_y  = np.asanyarray(cdf[['price']])
    regr.fit(data_x, data_y)
    print('Coefficients: ', regr.coef_)
    print('Intercept   : ', regr.intercept_)

    #val_e1 = E1.get()
    val_e1 = e4_text_var.get()
    val_e1 = int(val_e1)
    predict_val_highway_cylinders_price = regr.intercept_[0] + regr.coef_[0][0]*val_e1

    # ============================================================================
    avg_price_all_params = (avg_price_make+predict_val_highway_mpg_price+predict_val_highway_doors_price+predict_val_highway_cylinders_price)/4
    display_txt = "\nThe estimated price is:\n\n "+"Rs."+str(int(avg_price_all_params))+"\n\n"
    L9.config(text = display_txt)
    
top = Tk()
#top.geometry('700x700')
photo = PhotoImage(file = 'car1.png')
photo = photo.subsample(2)
lbl = Label(top,image = photo)
lbl.image = photo
lbl.pack(padx=30,pady=10)

L1 = Label(top,text="_________ Car Price Predictor _________",font = ( "bold" , 32 , ), fg="blue")
L1.pack()

L2 = Label(top,text="ML Based LR Model",font = ( "bold" , 14 , ), fg="green")
L2.pack()

e1_text_var = StringVar()
e2_text_var = StringVar()
e3_text_var = StringVar()
e4_text_var = StringVar()
e5_text_var = StringVar()

L2 = Label(top,text="")
L2.pack(pady=10)

L8 = Label(top, text = 'Highway-mpg')
L8.pack()
E1 = Entry(top, bd=1, textvariable=e1_text_var)
E1.pack()

L2 = Label(top,text="")
L2.pack(pady=2)
L9 = Label(top, text = 'Make - [audi, jaguar etc.]')
L9.pack()

E2 = Entry(top, bd=1, textvariable=e2_text_var)
E2.pack()

L2 = Label(top,text="")
L2.pack(pady=2)
L10 = Label(top, text = 'Number of doors - [2 or 3 or 4 ...6]')
L10.pack()

E3 = Entry(top, bd=1, textvariable=e3_text_var)
E3.pack()

L2 = Label(top,text="")
L2.pack(pady=2)
L11 = Label(top, text = 'Number of cyliners - [2 or 3 or 4 ...12]')
L11.pack()

E4 = Entry(top, bd=1, textvariable=e4_text_var)
E4.pack()

L2 = Label(top,text="")
L2.pack(pady=2)
B10 = Button(top, text='Predict Now', command=predict_based_on_user_input)
B10.pack()

L9 = Label(top,font = ( "bold" , 16 , ), fg="red")
L9.pack()

top.mainloop()