
FROM node:16.13.0

COPY ./ /notus-react-main

# set working directory
WORKDIR /notus-react-main

# add `/app/node_modules/.bin` to $PATH
ENV PATH /notus-reacr-main/node_modules/.bin:$PATH

# install app dependencies
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# start app
CMD ["npm", "start"]