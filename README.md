<<<<<<< HEAD
# International Paper Company Financial Report Analysis

For this project, I use machine learning to do revenue/net sales forecasting for International Paper Company from 2002 to 2022. 

(S)ARIMA Model, short for "Auto-Regressive Integrated Moving Average", is one of powerful statistcis models for time series analysis(to predict future points in the series). 

**Here are the two main concepts that are applied in this project:**

- ARIMA model: time series analysis for the prediction of revenue/net sales 
- Streamlit library: summarize project output for the preparation of presentation
<br>

**Please see the graph of financial (Net sales) performance from 1993 to 2022 quarterly data base:**
<br>

Obviously, for these recent years, there was a downtrend on revenue movement compared with the period betwwen 1993 and 2014. In 2020, it reached out to the lowest point during the hardest-hit season of covid-19.

![Project3_Fianacial_Report_Analysis](Image/Net%20Sales%20Performance.PNG)

Then I start applying ARIMA machine learning model after reviewing general net sale performace. I picked 20 years data only from 2002 to 2022 on time series data prediction.

**1. Use statistics concept to confirm whether original data is stationary or not.**

Here are the value of mean and variance, I split the data by five different parts to get the output of mean and variance.
![Project3_Fianacial_Report_Analysis](Image/Mean%20and%20Variance.PNG)

Here are the basic statistics result for hyperthesis testing:
<br>
<br>

![Project3_Fianacial_Report_Analysis](Image/P-value%20and%20critical%20value.PNG)

Here is the graph of actual net sale amounts with simple moving average performance:

![Project3_Fianacial_Report_Analysis](Image/International%20Paper%20Revenue%20and%20SMA.PNG)

According the mean/varaince value, p-value and critical value, simple moving avarage graph, I can conclude that this time series data is non-stationary. The next step need to do is differencing raw data and use auto-correlation to determine the optimal parameters(p,d,q).
<br>
<br>

**2. First and second-order differencing, Auto-correction(ACF), Partial Auto-correlation(PACF)**

Please see below result of first and second-order differencing with autocorrelation plots:

![Project3_Fianacial_Report_Analysis](Image/Autocorrection%20and%20Difference%20-%20Non-Seasonal.PNG)

<br>

Please second result of first and second-order differencing with partial autocorrelation plots:

![Project3_Fianacial_Report_Analysis](Image/Partial%20Autocorrection%20and%20Difference%20-%20Non-Seasonal.PNG)

Here is line graph of first order difference:
- Dark blue dash line is 3 years simple moving average 
- Sky blue dash line is 5 years simple moving average

![Project3_Fianacial_Report_Analysis](Image/Line%20Graph%20of%20First%20Difference.PNG)

<br>

In conclusion, we can see that first order difference performs better,  all value remian within acceptable boundaries(blue highlighed area). Second order difference did not improve a lot. From the graph of first order difference, simple moving average becomes less fluctuated and more stable. Consequently, first-order differencing is a good choice for the D parameter.
<br>
<br>

**3. Fit into Auto-ARIMA model, generate and visualize revenue forecast results**

Since I choose first order difference to run the model, the value of p is 1, d is 1, q is 0.

Here is the result after fitting auto-ARIMA mode. From this result, we can see that the best model is (0,1,0). the coeficient of sigma2 term is close to zero, also p-value is less than 0.05 (highly significant), which means this model fit well.

![Project3_Fianacial_Report_Analysis](Image//Auto-ARIMA%20Result.PNG)

Here is the graph of my forecasting result.
- blue line is training data movement, orange line is test data movement

Somehow test data forecasting amounts are flat and closed to straight line, which means something is wrong. It does not make sense, so I use second method ARIMA model function to test again.

![Project3_Fianacial_Report_Analysis](Image/Net%20Sales%20Forecast.PNG)

<br>

**4. Fit into ARIMA model, generate and visualize revenue forecast results**

This time I pick the value of p=4, d=1, q=2 to try if predictions will be better.

Here is the ARIMA result after fitting ARIMA function.
From this result, we can see that MA term L2 and AR Term L2 coeficient is clsoed to zero, and p-value are less than 0.05, which is good.

![Project3_Fianacial_Report_Analysis](Image/ARIMA%20result.PNG)

Please see below visualization of predictions output.
Test prediction looks more fluctuated now but it is still overpredicted, far from the actual result. That means the prediction value is still not accurate.

![Project3_Fianacial_Report_Analysis](Image/ARIMA%20Model%20Forecast.PNG)

That was the best I can do. I will try to run the model again with different parameters or using second order difference to fit into the model, run and test it until prediction looks more accurate.
=======
# International Paper Company Financial Report Analysis

For this project, I use machine learning to do revenue/net sales forecasting for International Paper Company from 2002 to 2022. 

(S)ARIMA Model, short for "Auto-Regressive Integrated Moving Average", is one of powerful statistcis models for time series analysis(to predict future points in the series). 

**Here are the two main concepts that are applied in this project:**

- ARIMA model: time series analysis for the prediction of revenue/net sales 
- Streamlit library: summarize project output for the preparation of presentation
<br>

**Please see the graph of financial (Net sales) performance from 1993 to 2022 quarterly data base:**
<br>

Obviously, for these recent years, there was a downtrend on revenue movement compared with the period betwwen 1993 and 2014. In 2020, it reached out to the lowest point during the hardest-hit season of covid-19.

![Project3_Fianacial_Report_Analysis](Image/Net%20Sales%20Performance.PNG)

Then I start applying ARIMA machine learning model after reviewing general net sale performace. I picked 20 years data only from 2002 to 2022 on time series data prediction.

**1. Use statistics concept to confirm whether original data is stationary or not.**

Here are the value of mean and variance, I split the data by five different parts to get the output of mean and variance.
![Project3_Fianacial_Report_Analysis](Image/Mean%20and%20Variance.PNG)

Here are the basic statistics result for hyperthesis testing:
<br>
<br>

![Project3_Fianacial_Report_Analysis](Image/P-value%20and%20critical%20value.PNG)

Here is the graph of actual net sale amounts with simple moving average performance:

![Project3_Fianacial_Report_Analysis](Image/International%20Paper%20Revenue%20and%20SMA.PNG)

According the mean/varaince value, p-value and critical value, simple moving avarage graph, I can conclude that this time series data is non-stationary. The next step need to do is differencing raw data and use auto-correlation to determine the optimal parameters(p,d,q).
<br>
<br>

**2. First and second-order differencing, Auto-correction(ACF), Partial Auto-correlation(PACF)**

Please see below result of first and second-order differencing with autocorrelation plots:

![Project3_Fianacial_Report_Analysis](Image/Autocorrection%20and%20Difference%20-%20Non-Seasonal.PNG)

<br>

Please second result of first and second-order differencing with partial autocorrelation plots:

![Project3_Fianacial_Report_Analysis](Image/Partial%20Autocorrection%20and%20Difference%20-%20Non-Seasonal.PNG)

Here is line graph of first order difference:
- Dark blue dash line is 3 years simple moving average 
- Sky blue dash line is 5 years simple moving average

![Project3_Fianacial_Report_Analysis](Image/Line%20Graph%20of%20First%20Difference.PNG)

<br>

In conclusion, we can see that first order difference performs better,  all value remian within acceptable boundaries(blue highlighed area). Second order difference did not improve a lot. From the graph of first order difference, simple moving average becomes less fluctuated and more stable. Consequently, first-order differencing is a good choice for the D parameter.
<br>
<br>

**3. Fit into Auto-ARIMA model, generate and visualize revenue forecast results**

Since I choose first order difference to run the model, the value of p is 1, d is 1, q is 0.

Here is the result after fitting auto-ARIMA mode. From this result, we can see that the best model is (0,1,0). the coeficient of sigma2 term is close to zero, also p-value is less than 0.05 (highly significant), which means this model fit well.

![Project3_Fianacial_Report_Analysis](Image//Auto-ARIMA%20Result.PNG)

Here is the graph of my forecasting result.
- blue line is training data movement, orange line is test data movement

Somehow test data forecasting amounts are flat and closed to straight line, which means something is wrong. It does not make sense, so I use second method ARIMA model function to test again.

![Project3_Fianacial_Report_Analysis](Image/Net%20Sales%20Forecast.PNG)

<br>

**4. Fit into ARIMA model, generate and visualize revenue forecast results**

This time I pick the value of p=4, d=1, q=2 to try if predictions will be better.

Here is the ARIMA result after fitting ARIMA function.
From this result, we can see that MA term L2 and AR Term L2 coeficient is clsoed to zero, and p-value are less than 0.05, which is good.

![Project3_Fianacial_Report_Analysis](Image/ARIMA%20result.PNG)

Please see below visualization of predictions output.
Test prediction looks more fluctuated now but it is still overpredicted, far from the actual result. That means the prediction value is still not accurate.

![Project3_Fianacial_Report_Analysis](Image/ARIMA%20Model%20Forecast.PNG)

That was the best I can do. I will try to run the model again with different parameters or using second order difference to fit into the model, run and test it until prediction looks more accurate.
>>>>>>> f53901a5cd5d4b26082d1dbad78fef4e9288578a
