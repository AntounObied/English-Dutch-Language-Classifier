# English-Dutch-Language-Classifier

To train the program, 4 arguments must be provided. The first argument of the program always pertains
to either training or predicting. If it is “train”, then the second argument must be the training file the
user wants to use. The training file contains a list of sentences, with the indication whether they are
English or Dutch at the start. The third argument specifies the hypothesis file name that the program
should write out. It is the model that is to be used for the prediction. The fourth and final argument is
the learning type, which could be Decision Tree (dt), or AdaBoost (ada).


train <file_to_train_from> <output_model_name> <ada or dt>


To predict the languages of a file, “predict” should be the first argument. The second should be the
name of the hypothesis file, or model, that the training algorithm wrote in the training step. The third
and final argument should be the name of the test file for which the languages the user wishes to be
identified. The main class will determine if the model is of type Decision Tree, or AdaBoost, and then call
the method that predicts the language to its appropriate instance type.


predict <model_name>
