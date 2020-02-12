FROM node:latest

RUN mkdir app
WORKDIR /app
COPY . /app

COPY package*.json ./
#RUN npm install
RUN npm i -g @vue/cli
RUN npm i -g @vue/cli-service-global
RUN npm install

EXPOSE 8880
CMD [ "npm", "run" ,"serve" ,"-p" , "8880"]

