## Use Apache Tika on Python
1. Ensure you got JDK installed
    - Go to CMD, type Java > Enter
    - If resulted error, most probably Java is not installed yet
2. Proceed with JDK installation
    - [Download and install any version of JDK you need](https://www.oracle.com/java/technologies/downloads/)
    - Make sure Java has installed successfully

3. Download Tika server
    - [Download any version of Tika server here](https://tika.apache.org/download.html)
    - E.g. Mirrors for tika-server-1.28.1.jar 

4. Run Tika server
    - Go to CMD > Change directory to where the jar file located
    - Paste ``` java -jar tika-server-1.28.1.jar ``` in CMD > Enter

5. Verify Tika is running
    - Go to http://localhost:9998/
    - If it's running then the Tika has started
    - [Refer here for more detailed documentation](https://cwiki.apache.org/confluence/display/TIKA/TikaServer#TikaServer-InstallationofTikaServer)
