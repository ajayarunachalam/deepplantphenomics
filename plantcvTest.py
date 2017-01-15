from deepplantpheno import DPPModel

model = DPPModel(debug=True, load_from_saved=False)

# 3 channels for colour, 1 channel for greyscale
channels = 3

# Setup and hyperparameters
model.setBatchSize(128)
model.setNumberOfThreads(12)
model.setImageDimensions(32, 32, channels)

model.setProblemType('regression')
model.setTrainTestSplit(0.7)
model.setRegularizationCoefficient(0.004)
model.setLearningRate(0.001)
model.setWeightInitializer('normal')
model.setMaximumTrainingEpochs(700)

# Set image pre-processing steps
model.addPreprocessor('auto-segmentation')

# Load regression labels from CSV file
model.loadMultipleLabelsFromCSV('./data/danforth-sample/bbox-labels.csv')

# Load all VIS images from a Lemnatec image repository
model.loadLemnatecImagesFromDirectory('./data/danforth-sample')

# Begin training the regression model
model.beginTraining()