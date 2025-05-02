# Deploying Browser-Use WebUI to Railway

This guide explains how to deploy the Browser-Use WebUI to Railway for production use.

## Requirements

1. A [Railway account](https://railway.app)
2. Git installed on your machine
3. Railway CLI (optional, for local development and deployment)

## Deployment Steps

### 1. Set Up a Railway Project

1. Log in to your Railway account at [railway.app](https://railway.app)
2. Create a new project by selecting "New Project" from the dashboard
3. Choose "Deploy from GitHub repo" option
4. Connect your GitHub account if not already connected
5. Select this repository from the list

### 2. Configure Environment Variables

After creating the project, you need to set up the environment variables:

1. Navigate to the "Variables" tab in your Railway project
2. Add your API keys and configuration variables
3. At minimum, you should add:
   - `OPENAI_API_KEY` (or another LLM provider key)
   - `CHROME_PERSISTENT_SESSION=true` (recommended for API usage)
   - Optionally add other variables from `.env.example`

### 3. Deploy

1. Go to the "Deployments" tab
2. Click "Deploy Now" to start the deployment process
3. Wait for the build and deployment to complete
4. Once deployed, Railway will provide you with a URL to access your application

### 4. Using Your Browser-Use WebUI API

Once deployed, you can access the API in the following ways:

1. **Web Interface**: Visit the URL provided by Railway
2. **VNC Access**: For monitoring browser interactions, access `https://your-railway-url/vnc.html`
3. **API Endpoints**: Your application is now accessible as an API service

## Important Notes

- Railway's free tier has limitations on usage. For production use, consider upgrading to a paid plan.
- The Docker container requires significant resources due to the browser operations. Choose appropriate instance sizes.
- Persistent browser sessions will consume more resources but provide better continuity between API requests.
- For security, do not commit any files with actual API keys. Always use environment variables in Railway.

## Troubleshooting

If you encounter issues:

1. Check the logs in the "Deployments" tab
2. Verify your environment variables are set correctly
3. Ensure you have chosen adequate resources for your deployment
4. For VNC access issues, confirm the VNC server is running correctly

## Resources

- [Railway Documentation](https://docs.railway.app)
- [Browser-Use Documentation](https://docs.browser-use.com) 