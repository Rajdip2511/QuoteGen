# Builder stage
FROM node:18 AS builder

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY . .

# Build the application
RUN npm run build

# Runner stage
FROM nginx:alpine

# Copy built files from builder stage
COPY --from=builder /app/.next /usr/share/nginx/html

# Expose port 3000
EXPOSE 3000

# Configure nginx to listen on port 3000
RUN echo 'server { \
    listen 3000; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html index.htm; \
        try_files $uri $uri/ /index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

# Start nginx
CMD ["nginx", "-g", "daemon off;"] 