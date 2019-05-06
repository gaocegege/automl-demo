FROM tensorflow/tensorflow:1.5.0

COPY ./mnist.py /
COPY ./mnist.npz /tmp/
ENTRYPOINT ["python", "/mnist.py"]
