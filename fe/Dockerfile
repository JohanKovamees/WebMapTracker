# Use the official Nginx image as the base image
FROM nginx:latest

# Copy your frontend files to the Nginx HTML directory
COPY app.html register.html index.html style.css main.js /usr/share/nginx/html/
COPY custom.geo.json /usr/share/nginx/html/


# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the mime.types file
COPY mime.types /etc/nginx/mime.types

# Copy the ssl certs
COPY cert.pem /etc/nginx/cert.pem
COPY key.pem /etc/nginx/key.pem

# Expose the default Nginx port
EXPOSE 80
EXPOSE 443

# Run Nginx in the foreground to keep the container running
CMD ["nginx", "-g", "daemon off;"]
