#The code is written by Qifeng Zeng

FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask
# RUN pip install request
RUN pip install requests


USER nyu

COPY --chown=nyu:nyu . .

CMD [ "python", "./registration.py" ]
CMD [ "python", "./US.py" ]

