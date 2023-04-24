# Use the official Nginx image as the base image
FROM nginx:latest

# Copy your frontend files to the Nginx HTML directory
COPY app.html register.html index.html style.css main.js /usr/share/nginx/html/

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the default Nginx port
EXPOSE 80

# Run Nginx in the foreground to keep the container running
CMD ["nginx", "-g", "daemon off;"]
