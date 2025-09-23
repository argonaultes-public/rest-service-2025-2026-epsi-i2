FROM maven:3.9.9-eclipse-temurin-17
COPY . .
RUN ["mvn", "-Dmaven.test.skip=true", "package"]
ENTRYPOINT ["java","-jar","/target/rest-service-0.0.1-SNAPSHOT.jar"]