FROM node:14-alpine
WORKDIR /frontend
ENV PATH /frontend/node_modules/.bin:$PATH
COPY . .
RUN npm install