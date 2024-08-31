# Automated Plant Disease Recognition System Backend

pip3 install -r requirements.txt

python3 main.py

### labels

classes=['brinjal-athilacna-beetles',
'brinjal-fruitborer',
'brinjal-mites',
'brinjal-tobacco-mosaic-virus',
'chili-leaf-curl-complex',
'pumpkin-mosaic-virus']

### Docker image push into digital ocean container registry

doctl auth init

doctl registry login

docker tag <docker-image> registry.digitalocean.com/<regitry-name>/<docker-image-name>
docker tag agri-cure-image registry.digitalocean.com/agri-cure/agri-cure-image

docker push registry.digitalocean.com/<regitry-name>/<docker-image-name>
docker push registry.digitalocean.com/agri-cure/agri-cure-image
