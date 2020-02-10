FROM node:10

RUN mkdir app
WORKDIR /app
COPY . /app

COPY package*.json ./
RUN npm install

EXPOSE 8880
CMD [ "npm", "run" ,"serve" ,"-p" , "8880"]

