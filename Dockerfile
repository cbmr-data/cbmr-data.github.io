FROM nginx:alpine
COPY root/ /usr/share/nginx/html
COPY esrum/build/html/ /usr/share/nginx/html/esrum/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
