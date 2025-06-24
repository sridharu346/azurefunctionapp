# Azure Function App

A Python Azure Function App for testing purposes with automatic deployment via GitHub Actions.

## Function Details

- **Function Name**: `functiontesting`
- **Trigger**: HTTP Trigger
- **Authentication**: Function Level
- **Runtime**: Python 3.9

## Local Development

1. Install Azure Functions Core Tools
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `func start`

## Automatic Deployment Setup

This project is configured for automatic deployment to Azure using GitHub Actions.

### Prerequisites

1. **Azure Function App**: Create a Function App in Azure Portal
2. **GitHub Repository**: This repository should be connected to GitHub

### Setup Steps

1. **Create Azure Function App** (if not already created):
   ```bash
   az group create --name myResourceGroup --location eastus
   az storage account create --name mystorageaccount123 --location eastus --resource-group myResourceGroup --sku Standard_LRS
   az functionapp create --resource-group myResourceGroup --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name your-function-app-name --storage-account mystorageaccount123
   ```

2. **Get Publish Profile**:
   - Go to Azure Portal → Your Function App → Overview → Get publish profile
   - Download the publish profile file

3. **Add GitHub Secret**:
   - Go to your GitHub repository → Settings → Secrets and variables → Actions
   - Create a new secret named `AZURE_FUNCTIONAPP_PUBLISH_PROFILE`
   - Paste the entire content of the publish profile file

4. **Update Function App Name**:
   - Edit `.github/workflows/azure-functions-deploy.yml`
   - Change `your-function-app-name` to your actual Function App name

### Deployment

Once configured, every push to the `main` branch will automatically trigger deployment to Azure.

## Function Endpoint

After deployment, your function will be available at:
```
https://your-function-app-name.azurewebsites.net/api/functiontesting?code=YOUR_FUNCTION_KEY
```

## Testing

You can test the function by:
- Adding a `name` parameter: `?name=YourName`
- Sending a JSON body with a `name` field
- Calling without parameters to get the default response
