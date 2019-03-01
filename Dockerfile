# Base image
FROM openjdk:8-jdk-alpine as base
WORKDIR /usr/spiderlab/
RUN apk add git=2.20.1-r0 maven=3.6.0-r0 python3=3.6.8-r1
COPY ./scripts ./scripts

# # Build the tools
FROM base as tools
WORKDIR /usr/spiderlab/tools/
RUN git clone https://github.com/inf295uci-2015/primitive-hamcrest.git
RUN cd primitive-hamcrest && mvn package install

RUN git clone https://github.com/gousiosg/java-callgraph.git
RUN cd java-callgraph && mvn package

RUN git clone https://github.com/spideruci/tacoco.git
RUN cd tacoco && mvn package install

FROM tools
RUN git clone https://github.com/spideruci/blinky.git
RUN python3 ../scripts/change_blinky_config.py xile,frames
RUN cd blinky && mvn clean package install

WORKDIR /usr/spiderlab/