#!/bin/bash

# Print environment information for debugging
echo "Starting application with PORT=$PORT and HEALTH_PORT=$HEALTH_PORT"

# Start the health check server in the background
python healthcheck.py &

# Wait a moment for the health check server to start
sleep 2

# Start supervisord
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf