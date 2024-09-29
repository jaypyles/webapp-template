# Build next dependencies
FROM node:latest as jsbuilder
WORKDIR /project

COPY package*.json ./

RUN npm install

COPY public /project/public
COPY src /project/src
COPY tsconfig.json /project/tsconfig.json
COPY tailwind.config.js /project/tailwind.config.js
COPY next.config.mjs /project/next.config.mjs
COPY postcss.config.js /project/postcss.config.js

RUN npm run build


