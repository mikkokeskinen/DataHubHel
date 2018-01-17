# Download FranhoferIOSB SensorThingsServer war from Bintray and clone our custom Moquette server for FranhoferIOSB SensorThingsServer from github
FROM alpine/git as clone
WORKDIR /app
ADD https://dl.bintray.com/fraunhoferiosb/Maven/de/fraunhofer/iosb/ilt/SensorThingsServer/1.2/SensorThingsServer-1.2.war /app/
RUN git clone https://github.com/mikkokeskinen/datahubhel-moquette-server.git


# Copy java sources to /app/datahubhel-moquette-server directory and build the project with Maven
FROM maven:3.5-jdk-8-alpine as build
COPY --from=clone /app /app

WORKDIR /app/datahubhel-moquette-server
RUN mvn -Dmaven.test.skip=true -Dmaven.javadoc.skip=true package


FROM tomcat:8-jre8-alpine

EXPOSE 8080
EXPOSE 1883

# Add database drivers to Tomcat common classpath
ADD http://repo.maven.apache.org/maven2/org/postgresql/postgresql/9.4.1212/postgresql-9.4.1212.jar /usr/local/tomcat/lib/
ADD http://repo.maven.apache.org/maven2/net/postgis/postgis-jdbc/2.2.1/postgis-jdbc-2.2.1.jar /usr/local/tomcat/lib/

# Use our own Moquette server implementation with HTTP auth by unpacking the war and copying our
# solution to the WEB-INF/libs directory and referencing it in the SensorThingsService settings.
COPY ./SensorThingsService.datahubhel_moquette_server.xml /usr/local/tomcat/conf/Catalina/localhost/SensorThingsService.xml

RUN mkdir /usr/local/tomcat/webapps/SensorThingsService
COPY --from=clone /app/SensorThingsServer-1.2.war /app/
RUN unzip /app/SensorThingsServer-1.2.war -d /usr/local/tomcat/webapps/SensorThingsService

COPY --from=build /app/datahubhel-moquette-server/target/datahubhel-moquette-server-1.0-SNAPSHOT.jar /usr/local/tomcat/webapps/SensorThingsService/WEB-INF/lib/
