
#FROM Tells docker which image you base your image on
FROM python:3

ADD my_script.py /
#RUN tells Docker which additional commands to execute (this one is installing a lib which is required to run this particular script)
RUN pip install pystrich
#CMD tells Docker to execute the command when the image loads
CMD [ "python", "./my_script.py" ]

