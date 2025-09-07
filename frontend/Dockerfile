FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* ./
# Use npm ci when lockfile is present, otherwise fallback to npm install
RUN if [ -f package-lock.json ]; then \
      npm ci --no-audit --no-fund; \
    else \
      npm install --no-audit --no-fund; \
    fi
COPY . .
RUN npm run build

FROM node:20-alpine AS run
WORKDIR /app
ENV HOST=0.0.0.0 PORT=8080
COPY --from=build /app .
# vite preview serves dist
EXPOSE 8080
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "8080"]
