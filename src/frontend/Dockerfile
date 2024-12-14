# Build the React app
FROM node:16 AS build

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Serve the app with Nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
