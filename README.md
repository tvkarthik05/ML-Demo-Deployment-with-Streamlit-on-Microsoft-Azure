# ML-Demo-Deployment-with-Streamlit-on-Microsoft-Azure
Demo app for deployment on Microsoft Azure using streamlit for different types of models i.e. Structured, CV, NLP
+ App consists of 2 parts - frontend (streamlit), backend (flask). Both communicate with each other to take the inputs and show the output
+ **The goal of this project is not to build model but DEPLOYMENT**

## Project Structure
+ backend - Contains the flask app. Run the "app.py" file to start the flask backend. Use the "request.py" file for testing it.
+ frontend - Contains the streamlit app. Run the "app.py" file to start the frontend.
+ data - Data used for training sample models
+ notebooks - The notebooks used for creating the tabular, cv & nlp models

## Prerequisites
+ Install docker - https://docs.docker.com/desktop/windows/install/
+ Install Azure CLI - https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli
+ Create Microsoft Azure Account - https://portal.azure.com/

## Steps for deployment on Azure
1. Build docker image for backend. Go into the backend folder using powershell and run the below command
	+ docker build --tag=<azure container registry name>/<image_name>:<tag_name> .
	e.g. - docker build --tag=acrpractice.azurecr.io/backend:v1.0 .
	
2. Run on local to test backend image
	+ docker run -t -i -p 80:80 acrpractice.azurecr.io/backend:v1.0
	
3. Need to push the docker image to Azure Container Registry(ACR). Follow the below steps,
	+ Login to azure - az login
	+ Set subscription of acr - az account set --subscription <Subscription ID>
	+ Login to acr - az acr login --name <ACR Login server>
	+ Tag the app to the acr(optional) - docker tag acrpractice.azurecr.io/backend:v1.0 acrpracticetest.azurecr.io/backend:v1.0
	+ Push to acr - docker push acrpractice.azurecr.io/backend:v1.0
	
4. Create an Azure Container Registry (ACI) and deploy the backend

5. The IP address obtained from the above ACI can be added in frontend (Line-8 in app.py) 

6. Run steps-1 to 4 for frontend as well and push the image to acr with name "frontend:v1.0"
	+ docker push acrpractice.azurecr.io/frontend:v1.0
