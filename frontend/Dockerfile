FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
# Minimal SPA nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Serve built assets
COPY --from=build /app/dist /usr/share/nginx/html
# Healthcheck
HEALTHCHECK --interval=15s --timeout=3s --retries=5 CMD wget -qO- http://localhost/ || exit 1
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
