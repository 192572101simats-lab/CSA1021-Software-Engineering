# Use the lightweight official Nginx image
FROM nginx:alpine

# Remove the default Nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy website files into the Nginx web root
COPY index.html style.css /usr/share/nginx/html/

# Nginx listens on port 80
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
