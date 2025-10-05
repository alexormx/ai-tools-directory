FROM node:20-alpine AS deps
WORKDIR /app
COPY frontend/package*.json frontend/
RUN cd frontend && npm ci

FROM node:20-alpine AS build
WORKDIR /app
COPY --from=deps /app/frontend/node_modules frontend/node_modules
COPY frontend frontend
WORKDIR /app/frontend
ENV NEXT_TELEMETRY_DISABLED=1
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app/frontend
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
COPY --from=build /app/frontend/.next ./.next
COPY --from=build /app/frontend/node_modules ./node_modules
COPY --from=build /app/frontend/public ./public
COPY --from=build /app/frontend/package.json ./package.json
EXPOSE 3000
CMD ["npm","run","start"]