FROM node:22.14-alpine

WORKDIR /src

COPY package.json ./
COPY package-lock.json ./

RUN npm ci --only=production

COPY . .

RUN if [ -f .env.production ]; then cp .env.production .env; fi
