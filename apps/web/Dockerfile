FROM node:20-alpine
WORKDIR /app
COPY package.json /app/package.json
COPY apps/web/package.json /app/apps/web/package.json
COPY packages/shared/package.json /app/packages/shared/package.json
RUN npm install
COPY . .
WORKDIR /app/apps/web
EXPOSE 3000
CMD ["npm", "run", "dev"]
