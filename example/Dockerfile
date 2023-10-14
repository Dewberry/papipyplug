FROM python:3.11-alpine as prod

# currently, git must be installed to use the papipyplug
RUN apk add git

WORKDIR /plugin
COPY . .

RUN pip3 install -r requirements.txt

# Test the plugin
RUN chmod +x /plugin/entrypoint.sh
CMD ["./entrypoint.sh"]