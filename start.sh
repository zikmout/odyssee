echo "--------------- IS DOCKER WORKING ? ---------------\n"
docker info
echo "---------------------------------------------------\n"

echo "--------------- BUILDING DOCKER IMAGE ---------------\n"
docker build -t odyssee:t1 .
echo "-----------------------------------------------------\n"

echo "--------------- Now you can see the image ---------------\n"
docker images
echo "---------------------------------------------------------\n"

echo "--------------- Now lets run the image ---------------\n"
#docker run -it -v /home/zak/Projects/docker/mission03/shared:/home/zikmout/_shared -d -p 80:80 mission2:v1
docker run -it -v `pwd`/html:/var/www/html -d odyssee:t1
echo "------------------------------------------------------\n"

echo "--------------- And see the result of curl ---------------\n"
curl 127.0.0.2:80
echo "----------------------------------------------------------\n"

echo "-> To connect to the container type in: 'ssh -p 42 zikmout@172.17.0.2'\n"
