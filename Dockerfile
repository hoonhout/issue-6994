FROM continuumio/miniconda3

WORKDIR /issue-6994

ADD . /issue-6994

RUN pip install --no-cache-dir -U pip && \
    pip install -e .
