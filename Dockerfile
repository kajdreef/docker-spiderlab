# Base image
FROM openjdk:13-jdk-alpine as base
WORKDIR /usr/spiderlab/
RUN apk add --no-cache git=2.22.4-r0 maven=3.6.1-r0 gradle=5.4.1-r0 python3=3.7.7-r0 bash=5.0.0-r0

# # Build the tools
FROM base as tools
WORKDIR /usr/spiderlab/tools/primitive-hamcrest/
RUN git clone https://github.com/spideruci/primitive-hamcrest.git .
RUN mvn package install -DskipTests

WORKDIR /usr/spiderlab/tools/tacoco/
RUN git clone https://github.com/spideruci/tacoco.git .
RUN mvn package install -DskipITs -DskipTests

WORKDIR /usr/spiderlab/tools/spidertools/
RUN git clone https://github.com/kajdreef/spidertools.git  .
RUN pip3 install -e .

FROM tools
WORKDIR /usr/spiderlab/
COPY .spidertools.yml .spidertools.yml 
CMD bash