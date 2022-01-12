            
def create_prediction(model, x_test):
    """
    This function creates prediction score of our model, the yhat.
    Param:
        trained_model
        X_test
    """
    return model.predict(x_test)
    

def plot_confusion_matrix(yhat,y_predict):
    """
    This function plots the confusion matrix of the models.
    
    Params:
        Y_test
        Predictions
    Output:
        Confusion matrix
    
    
    """
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y, y_predict)
    ax= plt.subplot()
    sns.heatmap(cm, annot=True, ax = ax); #annot=True to annotate cells
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix'); 
    ax.xaxis.set_ticklabels(['True', 'False']); ax.yaxis.set_ticklabels(['True', 'False'])