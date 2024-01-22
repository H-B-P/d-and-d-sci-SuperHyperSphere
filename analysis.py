import pandas as pd
import numpy as np
import xgboost as xgb

trainDf = pd.read_csv("data.csv")
testDf = pd.read_csv("deployment_data.csv")

def depercent(x):
 return float(x[:-1])

trainDf["Sounds__Silence"] = trainDf["Weird Sounds"].str.contains("Silence")
trainDf["Sounds__Squelching"] = trainDf["Weird Sounds"].str.contains("Squelching")
trainDf["Sounds__Buzzing"] = trainDf["Weird Sounds"].str.contains("Buzzing")
trainDf["Sounds__Skittering"] = trainDf["Weird Sounds"].str.contains("Skittering")
trainDf["Sounds__Humming"] = trainDf["Weird Sounds"].str.contains("Humming")

trainDf["ZPPG Performance"] = trainDf["ZPPG Performance"].apply(depercent)
trainDf["ACTUAL"] = trainDf["ZPPG Performance"]

testDf["Sounds__Silence"] = testDf["Weird Sounds"].str.contains("Silence")
testDf["Sounds__Squelching"] = testDf["Weird Sounds"].str.contains("Squelching")
testDf["Sounds__Buzzing"] = testDf["Weird Sounds"].str.contains("Buzzing")
testDf["Sounds__Skittering"] = testDf["Weird Sounds"].str.contains("Skittering")
testDf["Sounds__Humming"] = testDf["Weird Sounds"].str.contains("Humming")

testDf["ZPPG Performance"] = testDf["ZPPG Performance"].apply(depercent)
testDf["ACTUAL"] = testDf["ZPPG Performance"]