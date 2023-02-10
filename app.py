<<<<<<< HEAD

import streamlit as st
import pandas as pd
from PIL import Image

# Create a name for prrsentation
st.set_page_config(page_title="International Paper Financial Report Presentation", 
                   page_icon=":star2:",
                   layout="wide"
)

st.sidebar.success("Presentation Outline")

with st.sidebar:
    add_radio = st.radio("Revenue/NetSales Forcast:", ("Financial Data Performance and Visualization", "Check Stationary", "Differencing and Autocorrelation", "Auto-ARIMA/ARIMA Model Fitting", "Forecasting"))

# Adding title
st.title("International Paper Financial Report Analysis")
st.snow()

# Add subheader
st.header("International Paper - Financial data from 1993 to 2022")

# Import data
data = pd.read_csv("interational_paper_company.csv")
st.dataframe(data=data)
st.checkbox("Use container width", value=False, key="user_container_width")

st.text("\n")
st.subheader("Net Sales performance - Seasonal vs Non-Seasonal (Data from 2002 to 2022)")
# Show Financial performance
image = Image.open('./image/Net Sales Performance.PNG')
st.image(image)

# ARIMA Model
st.header("Using ARIMA model to forcast Netsale/Revenue")
st.text("\n")
st.subheader("Step1: Check Stationary")
# Show mean and variance
check = st.checkbox("Display mean and variance:", value=True)
st.write('', check)
if check:
    st.write("")

data2 = {"mean": [63445, 5826, 6758, 5786, 5503],
        "variance":[39572, 173711, 1919004, 315480, 89133]}
    
df = pd.DataFrame(data2)
st.dataframe(df)

code = '''parts = int(len(values)/5)
part1, part2, part3, part4, part5 = values[0:parts], values[parts:(parts*2)],values[(parts*2):(parts*3)], values[(parts*3):(parts*4)], values[(parts*4):(parts*5)]
mean1, mean2, mean3, mean4, mean5 = part1.mean(), part2.mean(), part3.mean(), part4.mean(), part5.mean()
var1, var2, var3, var4, var5 = part1.var(), part2.var(), part3.var(), part4.var(), part5.var()'''

st.code(code, language='python')

st.text("\n")
st.markdown("**Use Augmneted Dikey-Fuller test**")
image2 = Image.open('./image/P-value and critical value.PNG')
st.image(image2)
st.text("\n")
image3 = Image.open('./image/International Paper Revenue and SMA.PNG')
st.image(image3)
st.text("\n")
st.markdown("**Summary: The ADF Statistics is greater than the critical value at different levels, and also the p-value is great than 0.05, which means it fail to reject the hull hypothesis at 90%, 95% and 99%, this time series data is non-stationary**")

#Differencing and Autocorrelation
st.subheader("Step2: Exemplary Differencing and Autocorrelation")
check2 = st.checkbox("Manual differencing to make the time series stationary", value=True)
st.write('', check2)
if check2:
    st.write("")

image4 = Image.open('./image/Autocorrection and Difference - Non-Seasonal.PNG')
st.image(image4)

st.text('\n')
st.markdown(st.checkbox("Differencing and Partial Autocorrelation", value=True))
image5 = Image.open('./image/Partial Autocorrection and Difference - Non-Seasonal.PNG')
st.image(image5)

st.markdown(st.checkbox('Visualization of First Difference', value=True))
image6 = Image.open('./image/Line Graph of First Difference.PNG')
st.image(image6)
st.markdown("**Summary:**")
st.markdown('**After checking difference and autocorrelation in both seasonal and non-seasonal parts,  the time series becomes stationary after first order differencing, second order is overdifferenced and does not improve these values. First oder differencing is a good choice for the D parameter even though it is not perfectly stationary(week stationarity).**')

# Fit Auto-ARIMA Model
st.text('\n')
st.subheader("Step3: Fit an Auto-ARIMA Model")
image7 = Image.open('./image/Auto-ARIMA Result.PNG')
st.image(image7)
st.markdown('**Summary:**')
st.markdown('**Accoring to Auto-ARIMA model, the best model is (0,1,0). The MA2 terms coefficient close to zero, p-value P > |z| is less than 0.05, which are highly significant.**')


st.text('\n')
st.markdown(st.checkbox("The Graph of Net Sales Forecast", value=True))
image8 = Image.open('./image/Net Sales Forecast.PNG')
st.image(image8)

# Fit ARIMA Model
st.text('\n')
st.subheader('Fit an ARIMA Model')
image9 = Image.open('./image/ARIMA result.PNG')
st.image(image9)

st.text('\n')
st.markdown(st.checkbox('The Graph of Net Sales Forecast - ARIMA Model', value=True))
image10 = Image.open("./image/ARIMA Model Forecast.PNG")
st.image(image10)
st.markdown('**Summary:**')
=======

import streamlit as st
import pandas as pd
from PIL import Image

# Create a name for prrsentation
st.set_page_config(page_title="International Paper Financial Report Presentation", 
                   page_icon=":star2:",
                   layout="wide"
)

st.sidebar.success("Presentation Outline")

with st.sidebar:
    add_radio = st.radio("Revenue/NetSales Forcast:", ("Financial Data Performance and Visualization", "Check Stationary", "Differencing and Autocorrelation", "Auto-ARIMA/ARIMA Model Fitting", "Forecasting"))

# Adding title
st.title("International Paper Financial Report Analysis")
st.snow()

# Add subheader
st.header("International Paper - Financial data from 1993 to 2022")

# Import data
data = pd.read_csv("interational_paper_company.csv")
st.dataframe(data=data)
st.checkbox("Use container width", value=False, key="user_container_width")

st.text("\n")
st.subheader("Net Sales performance - Seasonal vs Non-Seasonal (Data from 2002 to 2022)")
# Show Financial performance
image = Image.open('./image/Net Sales Performance.PNG')
st.image(image)

# ARIMA Model
st.header("Using ARIMA model to forcast Netsale/Revenue")
st.text("\n")
st.subheader("Step1: Check Stationary")
# Show mean and variance
check = st.checkbox("Display mean and variance:", value=True)
st.write('', check)
if check:
    st.write("")

data2 = {"mean": [63445, 5826, 6758, 5786, 5503],
        "variance":[39572, 173711, 1919004, 315480, 89133]}
    
df = pd.DataFrame(data2)
st.dataframe(df)

code = '''parts = int(len(values)/5)
part1, part2, part3, part4, part5 = values[0:parts], values[parts:(parts*2)],values[(parts*2):(parts*3)], values[(parts*3):(parts*4)], values[(parts*4):(parts*5)]
mean1, mean2, mean3, mean4, mean5 = part1.mean(), part2.mean(), part3.mean(), part4.mean(), part5.mean()
var1, var2, var3, var4, var5 = part1.var(), part2.var(), part3.var(), part4.var(), part5.var()'''

st.code(code, language='python')

st.text("\n")
st.markdown("**Use Augmneted Dikey-Fuller test**")
image2 = Image.open('./image/P-value and critical value.PNG')
st.image(image2)
st.text("\n")
image3 = Image.open('./image/International Paper Revenue and SMA.PNG')
st.image(image3)
st.text("\n")
st.markdown("**Summary: The ADF Statistics is greater than the critical value at different levels, and also the p-value is great than 0.05, which means it fail to reject the hull hypothesis at 90%, 95% and 99%, this time series data is non-stationary**")

#Differencing and Autocorrelation
st.subheader("Step2: Exemplary Differencing and Autocorrelation")
check2 = st.checkbox("Manual differencing to make the time series stationary", value=True)
st.write('', check2)
if check2:
    st.write("")

image4 = Image.open('./image/Autocorrection and Difference - Non-Seasonal.PNG')
st.image(image4)

st.text('\n')
st.markdown(st.checkbox("Differencing and Partial Autocorrelation", value=True))
image5 = Image.open('./image/Partial Autocorrection and Difference - Non-Seasonal.PNG')
st.image(image5)

st.markdown(st.checkbox('Visualization of First Difference', value=True))
image6 = Image.open('./image/Line Graph of First Difference.PNG')
st.image(image6)
st.markdown("**Summary:**")
st.markdown('**After checking difference and autocorrelation in both seasonal and non-seasonal parts,  the time series becomes stationary after first order differencing, second order is overdifferenced and does not improve these values. First oder differencing is a good choice for the D parameter even though it is not perfectly stationary(week stationarity).**')

# Fit Auto-ARIMA Model
st.text('\n')
st.subheader("Step3: Fit an Auto-ARIMA Model")
image7 = Image.open('./image/Auto-ARIMA Result.PNG')
st.image(image7)
st.markdown('**Summary:**')
st.markdown('**Accoring to Auto-ARIMA model, the best model is (0,1,0). The MA2 terms coefficient close to zero, p-value P > |z| is less than 0.05, which are highly significant.**')


st.text('\n')
st.markdown(st.checkbox("The Graph of Net Sales Forecast", value=True))
image8 = Image.open('./image/Net Sales Forecast.PNG')
st.image(image8)

# Fit ARIMA Model
st.text('\n')
st.subheader('Fit an ARIMA Model')
image9 = Image.open('./image/ARIMA result.PNG')
st.image(image9)

st.text('\n')
st.markdown(st.checkbox('The Graph of Net Sales Forecast - ARIMA Model', value=True))
image10 = Image.open("./image/ARIMA Model Forecast.PNG")
st.image(image10)
st.markdown('**Summary:**')
>>>>>>> 3965281f75630e57817453afccf2f3526d17220a
st.markdown("**Training data prediction are closed to the actual results, however, test data prediction are over predicted, which is not accurate.**")