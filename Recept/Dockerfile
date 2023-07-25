# Dockerfile
# Set base image
FROM python:3.11.4


LABEL version="1.0"
LABEL description="TG"

# Set the working directory

# Copying the dependencies file
ADD requirements.txt .
ADD Action.py /Recept/
ADD bd.py /Recept/
ADD menu_upd.py /Recept/
ADD tgbot.py /Recept/


# Installing dependencies

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt





