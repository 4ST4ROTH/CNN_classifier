deep Classifier project
workflow
Update config.yaml
Update secrets.yaml [Optional]
Update params.yaml
Update the entity
Update the configuration manager in src config.
Update the components
Update the pipeline
Test run pipeline stage
run tox for testing your package
Update the dvc.yaml
run "dvc repro" for running all the stages in pipeline
img

STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://github.com/4ST4ROTH/CNN_classifier.git
MLFLOW_TRACKING_USERNAME=4ST4ROTH
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model