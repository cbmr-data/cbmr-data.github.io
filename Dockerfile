FROM nginxinc/nginx-unprivileged:alpine
COPY root/ /usr/share/nginx/html
COPY esrum/build/html/ /usr/share/nginx/html/esrum/
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
