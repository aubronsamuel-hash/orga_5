FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
RUN npm install -g vite@5.2.8
ENV VITE_PORT=5173
CMD ["sh", "-c", "vite preview --host 0.0.0.0 --port ${VITE_PORT}"]
