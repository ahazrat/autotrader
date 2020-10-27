# autotrader
Automated trading of crypto tokens.

### Google Cloud Platform (GCP)
Login
- `gcloud auth login`
Change Project (optional)
- `gcloud config set project PROJECT_ID`
Test Google Cloud SDK
- `gcloud functions regions list`
Confirm configuraiton
- `gcloud config list`

### Deploy Cloud Function
Initial Deployment
- `gcloud functions deploy log_to_sheets --entry-point entry_point_function --runtime python38 --trigger-http --allow-unauthenticated`
- `gcloud functions deploy log_to_sheets --entry-point entry_point_function`
- Last known version: 12

### Invoke Cloud Function
- `gcloud functions call log_to_sheets --data '{"name":"Keyboard Cat"}'`

### Quick Deploy + Invoke
- `gcloud functions deploy log_to_sheets --entry-point entry_point_function && gcloud functions call log_to_sheets --data '{"name":"Keyboard Cat"}'`

### Google Sheets API
- Turn on the Google Sheets API
- Download the client configuration
- Review the GCP API Console: https://console.developers.google.com/?authuser=0&project=autotrader-1603817475954&pli=1


### Other Tools
Install the Local Functions Emulator (Node.js)
- `npm install -g @google-cloud/functions-emulator`
