import os
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
#these are all the imports that will possibley be needed
def loadData(where='desktop'):
    ##get training data in pandas dataframe from max's desktop
    if where=='desktop':
        os.chdir('C:\\Users\\maxwell\\Desktop\\')
        data=pd.read_csv("train(1).csv")# i see ages missing 
        print(data.head())#look at data to see if missing .i see cabin missing,age,
        return data
    else:
        data=pd.read_csv("train(1).csv")
        
data=loadData(where='asdf')
# i don't see any data times, i see a binary classiffication, i see some words in names, 6numerical variables
def exploratoryAnalysis(data):
    #create graphs of the numerical variables and decriptions of the columns
    desc=data.describe()
    dtpe=data.dtypes
    stdd=data.std()
    skew=data.skew()
    data.hist()
    plt.show()
    print('quartiles',desc,'dtypes',dtpe,'std',stdd,'skew',skew)
exploratoryAnalysis(data)
#there can be some data transformations here and variable selection
##compare distributions
def unusualDist(data): 
    #compare the disctributions of survived and died to the overall distribution
    #examining for irregularites
    cols=['SibSp','Age','Fare','Parch','Pclass']#usable columns
    for col in cols:
        vc=data[[col,'Survived']]
        vcc=vc[vc.Survived==1]
        vv=vcc[col].value_counts()
        print("ones",vv)
        vccc=vc[vc.Survived==0]
        v=vccc[col].value_counts()
        print("zeros",v)
        vv=vc[col].value_counts()
        print("normal",vv)
unusualDist(data)

data.fillna(-1,inplace=True)'


def splits(data):
    #split the data into training and cross validation sets, fill in na's with -1, drop the object and string columns
    def split_df(df, test_size=.3):
        from sklearn.cross_validation import train_test_split
        df.reset_index(level=0, inplace=True)# if many levels and manes for them use the column name
        train, test = train_test_split(df, test_size=test_size)
        # get out the split sets
    train,test=train, test = train_test_split(data, test_size=0.3)
    train.fillna(-1,inplace=True)
    test.fillna(-1,inplace=True)

    def sexcleaner(x):
        if x == 'Male':
            return 0
        else:
            return 1
    train.loc[:,'Sex']=train.loc[:,'Sex'].apply(sexcleaner)
    test.loc[:,'Sex']=test.loc[:,'Sex'].apply(sexcleaner)
    ytrain=train.Survived
    ytest=test.Survived
    train.drop(['Survived'],axis=1,inplace=True)
    test.drop(['Survived'],axis=1,inplace=True)
    train.drop(['Embarked','Ticket','Name','PassengerId','Cabin'],axis=1,inplace=True)
    test.drop(['Embarked','Ticket','Name','PassengerId','Cabin'],axis=1,inplace=True)
    #train.drop(['Cabin'],axis=1,inplace=True)
    #test.drop(['Cabin'],axis=1,inplace=True)
    xtest=test.iloc[:,:]
    xtrain=train.iloc[:,:]
    return xtrain,xtest,ytrain,ytest
##

xtrain,xtest,ytrain,ytest=splits(data)
def doLearn(xtrain,xtest,ytrain,ytest):
    # do the learning by creating an instancee of a sklearn class and fit it to the data
    # score the accuracy of the predictions
    clf=RandomForestClassifier()
    s=clf.fit(xtrain,ytrain).score(xtest,ytest)
    print('rf acc' , s)
    log=LogisticRegressionCV(verbose=6)
    ss=log.fit(xtrain,ytrain).score(xtest,ytest)
    print("logistic acc" , ss)
    svc=SVC()
    sss=svc.fit(xtrain,ytrain).score(xtest,ytest)
    print("svc acc",sss)
doLearn(xtrain,xtest,ytrain,ytest)


    
    
    
    
    
    