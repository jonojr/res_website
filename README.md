# res_website
Website for residential halls, including useful tools for its running

   Setup instructions:
   
    1. Install Docker (and docker-compose)
    2. Clone the repository
    3. Create .env and .env.db files based on the .example files given
    4. In this directory run the command 'docker-compose up'

The site will now be accessible from localhost:8000 in a local browser

If you want to build and run production locally, follow steps 1-3 then run the following command:

    sudo docker-compose -f docker-compose.prod.yaml up  --build

