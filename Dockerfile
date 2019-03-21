# Base image
FROM openjdk:8-jdk-alpine as base
WORKDIR /usr/spiderlab/
RUN apk add --no-cache git=2.20.1-r0 maven=3.6.0-r0 gradle=4.10.3-r0 python3=3.6.8-r1
COPY ./scripts ./scripts

# # Build the tools
FROM base as tools
WORKDIR /usr/spiderlab/tools/primitive-hamcrest/
RUN git clone https://github.com/inf295uci-2015/primitive-hamcrest.git .
RUN mvn package install

WORKDIR /usr/spiderlab/tools/java-callgraph/
RUN git clone https://github.com/gousiosg/java-callgraph.git .
RUN mvn package

WORKDIR /usr/spiderlab/tools/tacoco/
RUN git clone https://github.com/spideruci/tacoco.git .
RUN mvn package install

WORKDIR /usr/spiderlab/tools/blinky/
RUN git clone https://github.com/spideruci/blinky.git  .
RUN python3 ../../scripts/change_blinky_config.py xile,frames
RUN mvn package install

FROM tools
WORKDIR /usr/spiderlab/