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

for c in ["Strange Smell?", "Air Tastes Like", "Feng Shui of Surrounding Area"]:
 trainDf[c] = trainDf[c].astype("category")
 testDf[c] = testDf[c].astype("category")

#

explanatoryVars = ["Longitude", "Latitude", "Shortitude", "Deltitude", "Strange Smell?", "Air Tastes Like", "Feng Shui of Surrounding Area", "Sounds__Silence", "Sounds__Squelching", "Sounds__Buzzing", "Sounds__Skittering", "Sounds__Humming", "Local Value of Pi", "Murphy's Constant"]

trainDM = xgb.DMatrix(trainDf[explanatoryVars], label=trainDf["ZPPG Performance"], enable_categorical=True)
testDM = xgb.DMatrix(testDf[explanatoryVars], enable_categorical=True)

###

parameters={"max_depth":2, "learning_rate":0.1,  "objective":"reg:gamma"}

b = xgb.train(parameters, trainDM, 2000)

trainDf["PREDICTED"] = b.predict(trainDM)
testDf["PREDICTED"] = b.predict(testDM)

#print(trainDf.sort_values("PREDICTED"))
#print(trainDf[trainDf["PREDICTED"]>100])
print(testDf.sort_values("PREDICTED"))
print(testDf[testDf["PREDICTED"]>100])

###

parameters={"max_depth":2, "learning_rate":0.1,  "objective":"reg:squarederror"}

b = xgb.train(parameters, trainDM, 2000)

trainDf["PREDICTED"] = b.predict(trainDM)
testDf["PREDICTED"] = b.predict(testDM)

#print(trainDf.sort_values("PREDICTED"))
#print(trainDf[trainDf["PREDICTED"]>100])
print(testDf.sort_values("PREDICTED"))
print(testDf[testDf["PREDICTED"]>100])

###

parameters={"max_depth":10, "learning_rate":0.1,  "objective":"reg:squarederror"}

b = xgb.train(parameters, trainDM, 2000)

trainDf["PREDICTED"] = b.predict(trainDM)
testDf["PREDICTED"] = b.predict(testDM)

#print(trainDf.sort_values("PREDICTED"))
#print(trainDf[trainDf["PREDICTED"]>100])
print(testDf.sort_values("PREDICTED"))
pd.set_option('display.max_rows', None)
print(testDf[testDf["PREDICTED"]>90].sort_values("PREDICTED"))


